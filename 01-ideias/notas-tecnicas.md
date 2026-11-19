# Notas técnicas

Explicações que sustentam os temas mais delicados, no mesmo jeito que a [lojinha](https://github.com/adriangpo/lojinha-ux) faz. Servem de base para falar em cima do monitor e para responder perguntas.

## Limites de tempo de resposta (Jakob Nielsen)

| Tempo | O que o usuário sente |
|---|---|
| até 0,1s | Instantâneo: não precisa de feedback |
| até 1s | Percebe a espera, mas não perde o raciocínio |
| até 10s | Limite da atenção: precisa de indicador de progresso |
| mais de 10s | Vai fazer outra coisa: precisa de progresso real e aviso ao terminar |

Boa âncora para a abertura: quase todo tema do curso volta a algum desses números.

## Upload: as duas fases

1. **Envio dos bytes.** Quem sabe quanto já foi enviado é o navegador. O `fetch` não avisa o progresso do upload; o `XMLHttpRequest` avisa, pelo `xhr.upload.onprogress`.
2. **Processamento no servidor.** Só o servidor sabe o andamento. O worker grava o progresso no Postgres, o Postgres dispara `NOTIFY`, e a API, que escuta com `LISTEN`, repassa ao front.

Mostrar as duas fases deixa claro por que existe mais de um jeito de acompanhar o processamento. Na lojinha, o processamento anda aos trancos (pausas longas e rajadas), como na vida real.

## Short polling, long polling e SSE

Problema: o servidor tem uma novidade, mas no HTTP normal quem pergunta é sempre o cliente.

**Short polling.** O front pergunta de tempos em tempos e a API responde na hora, tenha novidade ou não.
```js
const intervalo = setInterval(async () => {
  const atual = await api(`/uploads/${id}`)
  setStatus(atual)
  if (atual.progresso === 100) clearInterval(intervalo)
}, 2000)
```
Na pausa do servidor, a resposta vem repetida; na rajada, a barra pula etapas e a novidade chega até 2s atrasada.

**Long polling.** O front pergunta uma vez e a API segura a resposta até o processamento terminar. Se passar de 30s sem terminar, a API responde como está e o front pergunta de novo: é isso que faz ser long *polling*.
```js
// GET /api/uploads/:id/resultado
const pronto = proximoAviso(id, 30_000, (status) => status.progresso === 100)
res.json((await pronto) ?? atual)
```
O custo: cada cliente esperando prende uma requisição aberta no servidor. E, como a resposta só diz "terminou", no meio do caminho não há porcentagem para mostrar.

**SSE (Server-Sent Events).** O front abre uma conexão e a API escreve nela a cada mudança.
```js
const fonte = new EventSource(`/api/uploads/${id}/eventos`)
fonte.onmessage = (mensagem) => {
  const atual = JSON.parse(mensagem.data)
  setStatus(atual)
  if (atual.progresso === 100) fonte.close() // sem isso, o EventSource reconectaria sozinho
}
```

| | Short polling | Long polling | SSE |
|---|---|---|---|
| Quem espera | O front, entre uma pergunta e outra | A API, segurando a resposta | Ninguém: a conexão fica aberta |
| Atraso da novidade | Até o intervalo inteiro (2s) | Quase nenhum | Quase nenhum |
| Requisições | Uma a cada 2s, mude ou não | Uma (mais uma a cada 30s sem terminar) | Uma só |
| Respostas "nada mudou" | A maioria | Só quando bate o limite de 30s | Nenhuma |
| Progresso no meio | Aos saltos | Não tem | Cada etapa |

No monitor, use o "Fixar para comparar" com o mesmo arquivo nas três versões: a diferença no número de requisições aparece sozinha.

## Timeouts

- O `fetch` não tem timeout: se a API travar, ele espera para sempre, e o spinner também.
- `AbortSignal.timeout(5000)` cancela a requisição depois de 5s. O `fetch` falha com um erro de nome `TimeoutError`, e o front mostra a mensagem certa ("O servidor está demorando mais que o normal.") com o botão "Tentar de novo".
- Quanto esperar volta ao Nielsen: depois de 10s o usuário já foi fazer outra coisa. Desistir antes disso é melhor que girar sem fim.
- Cancelar no front não para o servidor (o mesmo ponto do tema Race conditions). Por isso, repetir só é seguro se a operação for idempotente.

## Offline e conexão instável

1. **Saber que caiu:** `navigator.onLine` diz o estado atual; os eventos `offline` e `online` da `window` avisam quando muda. A lojinha mostra um aviso fixo: "Você está sem conexão. Pode continuar: o que você fizer será enviado quando a conexão voltar."
2. **Não perder a ação:** com ou sem conexão, a tela muda na hora e a ação entra numa fila guardada no `localStorage` (sobrevive a fechar a aba e voltar depois).
3. **Sincronizar:** no evento `online` e ao abrir a página, a fila é enviada em ordem, um envio por vez, e cada ação só sai da fila depois que a API confirma. Se cair no meio, o resto fica para a próxima vez.
4. **Reenviar sem duplicar:** a conexão pode cair no meio do envio, e a mesma ação vai de novo. Por isso ela precisa ser idempotente: `PUT /favoritos/7` e `DELETE /favoritos/7` dão no mesmo se chegarem duas vezes.

Para simular, use "Conexão da lojinha: Offline" no monitor. Ele faz `navigator.onLine` dar `false`, dispara os eventos de verdade e faz as chamadas falharem como sem rede. Vale só para as abas da lojinha, então o monitor continua mostrando tudo.

## Signed URL e cache de imagem

**O problema:** a signed URL carrega a assinatura e a data na própria query string. Se a API gera uma URL nova a cada requisição, cada F5 traz uma URL diferente, e para o navegador URL diferente é outro arquivo. Resultado: todas as imagens são baixadas de novo.

**Como a lojinha resolve:**
- **Assinatura fixa por período.** A API assina "como se fosse o começo do período" (`signingDate` do SDK da AWS), e durante uma hora a URL de cada foto é a mesma. Na lojinha, o período começa quando a API sobe, e o botão "Esquecer URLs assinadas" do monitor recomeça.
- **Cache-Control no arquivo:** cada foto é gravada no bucket com `Cache-Control: max-age=3600`, para o navegador poder guardar.
- **A validade do cache não pode passar da validade da URL.** A URL vale 2 horas a partir do começo do período, então sempre sobra pelo menos 1 hora, que é o tempo que a foto fica no cache.
