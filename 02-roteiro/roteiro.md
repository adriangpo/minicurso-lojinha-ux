# Roteiro

O roteiro como foi apresentado na XX Semana de Tecnologia da Fatec Ourinhos, em duas turmas com a mesma aula:

- **Turma A:** 19/10/2026, das 13h30 às 17h00.
- **Turma B:** 20/10/2026, das 19h30 às 23h00.

Cada turma teve até 20 pessoas, num laboratório com um computador por aluno, e dois apresentadores. A tela da sala (uma TV) mostrava o notebook dos apresentadores.

Total: 3h30 (210 minutos), com intervalo de 20 minutos no meio. A ordem segue a vida de uma ação do usuário: antes do clique, durante a espera, quando dá errado e o que deixa tudo rápido. Os tempos de cada tema são o plano que usamos para não estourar as 3h30.

Slides só na abertura e no fechamento (`03-material/slides/`). Do bloco 1 em diante, tudo acontece na [lojinha](https://github.com/adriangpo/lojinha-ux), com o monitor aberto em outra aba.

Cada tema segue o mesmo ritmo: **mostrar o problema na lojinha → explicar com o monitor e o "Ver código" → mostrar a versão corrigida.** Para comparar, usar o "Fixar para comparar" do monitor: rodar a versão ruim, fixar, rodar a boa.

| Tempo | Bloco | Temas |
|---|---|---|
| 20 min | Abertura | Conceitos (slides), limites de tempo do Nielsen, apresentação da lojinha e do monitor |
| 30 min | 1. Antes do clique | Formulários e validação (com o debate do botão desabilitado), Erros úteis, URL como estado |
| 50 min | 2. Durante a espera | Estados da tela, Skeleton, Layout shift, Debounce e Throttle, Race conditions, Optimistic UI, Feedback de sucesso, Upload com progresso e tempo real |
| 20 min | Intervalo | |
| 45 min | 3. Quando dá errado | Timeouts, Retries e backoff, Clique duplo e idempotência, Rate Limiting, Sessão expirada, Offline e conexão instável |
| 35 min | 4. Rapidez de verdade | Caching, Imagens com signed URL, Lazy Loading, N+1, Pagination vs Infinite Scroll |
| 10 min | Fechamento | Resumo, links e perguntas |

---

## Antes da aula

- **Preparação dos apresentadores.** Não fizemos um ensaio cronometrado. Fizemos uma passada pela lojinha inteira, tema por tema: o que falar em cada página, que experiência real de cada um dava para contar ali ("já aconteceu comigo…"), e quem conduz cada página. Dividir os temas entre os dois deixou a aula com duas vozes e deu tempo para um preparar a próxima demo enquanto o outro falava.
- **Na sala, antes de a turma chegar:** subir a lojinha (`npm run banco` e `npm run dev`), abrir a lojinha e o monitor em abas separadas, conferir se o texto fica legível na TV, zerar os controles do monitor e deixar a folha do aluno em cada lugar.
- **Folha do aluno** (`03-material/folha/folha.pdf`): uma A4 com o mapa dos 22 temas, linhas para anotar e os QR codes da apostila, da lojinha e deste repositório.

## Abertura — 20 min

Slides 1 a 13 de `03-material/slides/slides.pdf`.

- Pergunta para a turma: "Qual foi o último app que te irritou? Por quê?" (3 min)
- **Conceitos** (10 min). Bem breve, só o necessário para começar: o que é UX, o que é API, o caminho Navegador → API → Banco, a requisição em 3 passos, os métodos (GET, POST, PUT, DELETE) e os status codes (2xx, 4xx, 5xx), com rotas reais da lojinha.
- Os limites do Nielsen: 0,1s, 1s e 10s (4 min).
- A ideia do curso: UX não é só design. Metade dela é decidida na API.
- Os 4 blocos e a saída dos slides (3 min): abrir a lojinha e o monitor e fazer uma requisição de verdade. É a mesma requisição do slide, agora acontecendo.

## Bloco 1 — Antes do clique — 30 min

**Formulários e validação** · Frontend · 14 min
- Problema: o usuário preenche, clica e espera o servidor dizer que faltou um campo. E o oposto também incomoda: erro aparecendo antes de a pessoa chegar no campo parece bronca.
- Solução: erro só depois de sair do campo; o botão parece desabilitado (`aria-disabled`), mas o clique nele mostra todos os erros e leva ao primeiro; nada é apagado.
- Demo, do pior para o melhor: Só no servidor → Botão sempre habilitado → Erro ao sair do campo.
- **Debate** (8 min): depois da versão com o botão sempre habilitado e os erros aparecendo ao clicar (a linha do GOV.UK), perguntar: "desabilitar o botão ou não?". A turma vota e defende o voto. Aí mostrar a última versão, que junta os dois lados: o botão cinza avisa que falta algo, mas continua clicável e explica o quê; e nenhum erro aparece antes da hora (passar pelos campos com Tab, clicar no botão sem preencher nada).

**Erros úteis** · API · 8 min
- Problema: a API responde `500` ou `{"erro": "invalid"}` e o front mostra "Algo deu errado".
- Solução: status certo (`422` quando o dado não passa, `409` quando bate com algo que já existe) e erro customizado, no formato que se usa em projeto de verdade: `{ "errors": [{ "code": "PRODUCT_NAME_TAKEN", "message": "...", "field": "nome" }] }`. O code é único e estável: o front mapeia o code para a mensagem em português (pode ser a chave de tradução) e usa o field para colocar cada mensagem embaixo do campo certo. Se chegar um code que o front não conhece, ele mostra a message da API.
- Demo: mesmo formulário, sem validação no front. Cadastrar vazio (`422`, três erros com code) e depois um dado que só o servidor sabe validar ("Teclado mecânico", nome já em uso: `409 PRODUCT_NAME_TAKEN`). Abrir a resposta no inspetor do monitor e mostrar o mapa code → mensagem no "Ver código".

**URL como estado** · Frontend · 8 min
- Problema: filtra, dá F5 e perde tudo; não dá para mandar o link para alguém.
- Demo: aplicar filtros, dar F5, copiar o link e abrir em outra aba.

## Bloco 2 — Durante a espera — 50 min

**Estados da tela** · Frontend · 5 min
- Problema: tela branca enquanto carrega, tela branca quando falha, tela branca quando não tem nada.
- Demo: taxa de erro em 100% no monitor; depois, buscar "xyz". A mesma lista nos quatro estados.

**Skeleton Loading** · Frontend · 4 min
- Problema: spinner no meio da tela vazia parece mais lento do que é.
- Demo: latência de 1s, spinner vs skeleton.

**Layout shift** · Frontend · 4 min
- Problema: a imagem carrega, empurra o conteúdo e o usuário clica no botão errado.
- Demo: latência aleatória; tentar clicar em "Comprar" enquanto as imagens carregam. Depois, com espaço reservado.

**Debounce e Throttle** · Frontend · 6 min
- Problema: uma requisição por tecla.
- Demo: digitar na busca e ver no monitor uma requisição por tecla; com debounce, uma só, 400ms depois de parar de digitar. Throttle como contraste no scroll.

**Race conditions e AbortController** · Frontend · 6 min
- Problema: o usuário clica em Eletrônicos e logo depois em Casa. A resposta de Eletrônicos é mais lenta, chega por último e sobrescreve a de Casa: a aba diz Casa e a lista mostra eletrônicos.
- Demo: sem latência no monitor, clicar em Eletrônicos (a API sempre demora 2s) e logo em Casa (0,3s); a corrida embaixo da lista mostra a resposta errada ganhando. Depois, com AbortController: cada clique cancela a requisição anterior. Com cliques, debounce não faz sentido, e a turma não confunde os dois temas.
- Ponto extra (aparece no monitor): o navegador cancela, mas a API continua trabalhando e responde 200 mesmo assim. Cancelar no front não para o servidor.

**Optimistic UI** · Frontend + API · 5 min
- Problema: clicar em favoritar e esperar para o coração ficar vermelho.
- Demo: latência de 1s; favoritar na hora. Com erro em 100%, o coração volta e aparece um aviso.

**Feedback de sucesso** · Frontend · 5 min
- Problema: o usuário clica, a ação funciona, mas nada na tela diz isso. Ele clica de novo ou sai achando que falhou. O outro extremo: um alerta que trava a tela só para dizer "Sucesso!".
- Solução: confirmação discreta (toast), que some sozinha e não interrompe o que o usuário está fazendo.
- Demo: adicionar ao carrinho nas três versões: nada acontece, alerta que bloqueia e toast.

**Upload com progresso e tempo real** · Frontend + API · 15 min
- Problema: barra parada em 100% enquanto o servidor processa, sem o usuário saber o que está acontecendo.
- Fase 1: progresso do envio (navegador).
- Fase 2: progresso do processamento, de três jeitos. O processamento anda aos trancos (pausas longas e rajadas), como na vida real:
  - **Short polling:** o front pergunta a cada 2s. Muitas respostas vêm repetidas ("nada mudou") e etapas rápidas passam sem aparecer.
  - **Long polling:** o front pergunta uma vez e a API segura a resposta até o processamento terminar. O nome é parecido com o anterior, mas o comportamento muda muito.
  - **SSE:** uma conexão só; a API avisa a cada mudança (Postgres LISTEN/NOTIFY). A aba Rede do painel lista cada mensagem que chega.
- Demo: subir o mesmo arquivo (~10 MB) nas versões Sem progresso → Short polling → Long polling → SSE, fixando cada uma no monitor para comparar o número de requisições.
- Fechar comparando os três jeitos: requisições, atraso da novidade e progresso no meio do caminho (ver `01-ideias/notas-tecnicas.md`).

## Intervalo — 20 min

## Bloco 3 — Quando dá errado — 45 min

**Timeouts** · Frontend + API · 7 min
- Problema: a API travou e o spinner gira para sempre. O usuário não sabe se espera ou desiste.
- Solução: depois de alguns segundos, o front desiste (`AbortSignal.timeout`), explica o que houve e oferece "Tentar de novo".
- Demo: latência "Travada" no monitor; a versão ruim gira até a API responder, 30s depois; a boa desiste em 5s.
- Ligação: "tentar de novo" é o próximo tema.

**Retries e exponential backoff** · Frontend + API · 8 min
- Problema: a API falha uma vez e o usuário vê erro; ou o front tenta de novo sem parar e piora a situação.
- Demo: taxa de erro em 50% ou 100%; as tentativas com 1s, 2s, 4s aparecem na linha do tempo.
- Ligação: tentar de novo só é seguro se a operação for idempotente. É o próximo tema.

**Clique duplo e idempotência** · Frontend + API · 8 min
- Problema: clicou duas vezes, mandou dois Pix.
- O tema é uma transferência por Pix (para quem e valor), em quatro versões:
  - **Sem proteção:** cada clique em Transferir manda um Pix.
  - **Botão travado:** o front bloqueia o botão durante o envio, com "Enviando…". Resolve o clique duplo, mas não o retry nem a rede caindo no meio.
  - **Chave de idempotência:** a API reserva a chave antes de mandar o dinheiro. Os cliques extras voltam `409` na hora; a mesma chave com outro valor dá `422`; "Repetir o último envio" devolve o mesmo Pix até a chave expirar (30s) e depois cria outro.
  - **Pix duplicado:** a mesma pessoa e o mesmo valor em menos de 15s são bloqueados (`409` com `Retry-After`) até a janela passar. Protege contra o usuário que repete a transferência sem perceber, mesmo com uma chave nova a cada envio.
- Demo: clicar várias vezes em Transferir em cada versão e olhar o monitor.

**Rate Limiting** · API · 6 min
- Problema: a API cai por excesso de requisições, ou bloqueia sem explicar.
- Demo: aplicar o cupom várias vezes (limite: 5 em 10s), nas versões Sem limite → 429 sem explicação → Com Retry-After. Na última, o front mostra "tente novamente em X segundos".

**Sessão expirada** · Frontend + API · 6 min
- Problema: preencher um formulário longo, a sessão expirar e perder tudo.
- Demo: preencher, clicar em "Expirar sessão agora" no monitor e salvar. Na versão boa, o front pede login num modal e o formulário continua preenchido.

**Offline e conexão instável** · Frontend + API · 10 min
- Problema: no metrô, o usuário favorita um produto, aparece "Algo deu errado" e a ação se perde.
- Solução: avisar que está sem conexão (eventos `online` e `offline` do navegador), guardar a ação numa fila no `localStorage` (sobrevive a fechar a aba e voltar depois) e enviar sozinho quando a conexão voltar. Reenviar é seguro porque favoritar é `PUT` e desfavoritar é `DELETE`, que são idempotentes: mandar duas vezes dá no mesmo (ligação com os métodos da abertura e com o tema de clique duplo).
- Demo: no monitor, "Conexão da lojinha: Offline"; favoritar e desfavoritar alguns produtos; voltar para Online e ver a fila sendo enviada. O controle do monitor tem o mesmo efeito do Offline do DevTools (`navigator.onLine` fica `false` e os eventos disparam de verdade), sem precisar abrir o DevTools na frente da turma.

## Bloco 4 — Rapidez de verdade — 35 min

**Caching** · Frontend + API · 9 min
- Problema: voltar para a lista e esperar tudo carregar de novo.
- Demo: trocar de categoria e voltar, nas versões Sem cache → Cache na mão → TanStack Query → Cache HTTP. No Cache HTTP, a API nem aparece no monitor por 10s.

**Imagens com signed URL e cache** · Frontend + API · 7 min
- Problema: cada refresh gera signed URLs novas e todas as imagens são baixadas de novo.
- Demo: clicar em "Esquecer URLs assinadas" no monitor e alternar entre as versões (ou dar F5). "URL nova a cada vez" baixa as 12 fotos toda vez; "URL reaproveitada" baixa só na primeira e depois usa o cache.
- Na aula, esse botão ainda não existia. A versão reaproveitada assinava pelo começo da hora, então qualquer visita anterior na mesma hora deixava as fotos no cache, e trocar de versão não mostrava a diferença: era preciso dar F5 toda hora. O botão foi a correção que entrou depois das duas turmas.

**Lazy Loading** · Frontend · 5 min
- Demo: lista com 200 imagens; o contador de imagens e MB baixados no topo, com e sem `loading="lazy"`.

**N+1** · API · 6 min
- Problema: a página do produto faz uma requisição para o produto, outra para o vendedor, uma por comentário…
- Demo: linha do tempo com 15 requisições vs 1 endpoint que entrega o que a tela precisa.

**Pagination vs Infinite Scroll** · Frontend + API · 8 min
- Problema: sem paginação, a API manda tudo de uma vez; a tela demora e o banco trabalha à toa. Lembra o N+1: muito trabalho para mostrar pouco.
- Depois: páginas numeradas vs infinite scroll e quando usar cada um. Paginação por cursor na API para não pular nem repetir itens.
- Demo: sem paginação primeiro (ver o tamanho da resposta no monitor); depois, "Simular: alguém publicou agora" e rolar: o offset repete um item, o cursor não.

## Fechamento — 10 min

Slides 14 e 15 de `03-material/slides/slides.pdf`.

- Percorrer o menu da lojinha, bloco por bloco: os 22 temas com as etiquetas Frontend / API / Frontend + API.
- Mensagem final: a experiência do usuário é decidida nas duas pontas.
- Os QR codes da apostila, da lojinha e deste roteiro, e os contatos.
- Perguntas.
