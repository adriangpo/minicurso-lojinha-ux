# Decisões

O que foi decidido e por quê, no estado final. Durante a preparação, este arquivo era a primeira coisa a conferir antes de rediscutir algo, por nós e pela IA que ajudou a construir tudo. O caminho até cada decisão está em `COMO-FOI-FEITO.md`.

## Escopo

- **O curso é sobre UX nos dois lados**, frontend e API. Temas puramente técnicos ficaram de fora (lista em `temas.md`).
- **A lojinha é a fonte da verdade.** O que a lojinha não tem não aparece em lugar nenhum do material: nem no roteiro, nem nas notas, nem na apostila.
- **22 temas**: 19 da primeira lista e mais 3 que entraram depois de uma rodada de ideias (Timeouts, Offline e conexão instável, Feedback de sucesso). Na mesma rodada entraram a abertura de Conceitos, o debate do botão desabilitado, a versão "sem paginação" e a diferença entre short e long polling. Cortado nessa rodada: "Desfazer em vez de Tem certeza?".
- **Cada tema leva uma etiqueta**: Frontend, API ou Frontend + API. A etiqueta aparece na lojinha, na folha, na apostila e nos slides, e é o resumo do curso: boa parte da UX é decidida fora da tela.

## Formato

- **Demonstração acima de slide.** Cada tema é mostrado funcionando na lojinha, com a versão ruim e a boa lado a lado. Ver o problema acontecer convence mais que ouvir falar dele.
- **Slides só na abertura e no fechamento**: Conceitos (UX, API, requisição, métodos, status codes) e os limites do Nielsen. Do bloco 1 em diante, tudo é explicado na lojinha, com o monitor e o botão "Ver código". O monitor já mostra a requisição indo e voltando, e menos troca entre slide e navegador mantém o ritmo em 3h30.
- **O que seria slide nos temas** (a comparação entre short polling, long polling e SSE, por exemplo) é falado em cima do monitor; o conteúdo está em `notas-tecnicas.md`.
- **Slides simples**: uma ideia por slide, começando pelo problema. Sem excesso de tópicos, ícones ou gradientes.
- **Ordem da aula**: a vida de uma ação do usuário, em 4 blocos (antes do clique, durante a espera, quando dá errado, rapidez de verdade). Cada tema termina, sempre que dá, puxando o seguinte ("tentar de novo" leva a Retries, que leva a idempotência).

## Público e duração

- Alunos de TI. Até 20 por turma, num laboratório.
- 3h30, com um intervalo de 20 minutos entre os blocos 2 e 3. Para caber o intervalo, o fechamento ficou com 10 minutos.
- Dois apresentadores, com os temas divididos entre os dois.

## Botão desabilitado (tema 1)

- O botão de envio **parece desabilitado enquanto o formulário não está completo**, mas usa `aria-disabled` em vez de `disabled` (com `disabled`, o clique nem dispara e o teclado pula o botão).
- **Erro só na hora certa**: um campo só mostra erro depois que o usuário entrou nele e saiu (blur). Se ele clicar no botão "desabilitado", aparecem os erros de todos os campos, o foco vai para o primeiro com erro e nada é enviado. Sem focar nada, nenhum erro aparece. Erro antes da hora parece bronca.
- O campo reserva o espaço da mensagem de erro, para o erro que aparece no blur não empurrar o que está embaixo bem na hora do clique.
- O campo pendente não é marcado só com cor: a mensagem fica embaixo do campo.
- Durante o envio, o botão também fica bloqueado, com "Enviando…", para evitar clique duplo.
- Existe a corrente contrária (o GOV.UK e outros recomendam não desabilitar). Por isso a turma vota entre desabilitar ou não depois de ver a versão com o botão sempre habilitado. A versão "Erro ao sair do campo" junta o melhor das duas, é a recomendada e fica **por último** no seletor: Só no servidor → Botão sempre habilitado → Erro ao sair do campo.

## Código das demos

- **Simples e correto acima de tudo**: o código é explicado linha por linha na frente da turma.
- Uma página por tema, com um arquivo por versão (ruim / boa). Nada de `if` misturando versões.
- Nada desnecessário: sem abstração antecipada, sem configuração extra.
- Componentes visuais prontos (Mantine) para o código de tela ficar curto.
- O que é infraestrutura da aula (monitor, controles, geração de fotos) fica separado do código das demos, para não aparecer no "Ver código".

## Stack

- **Frontend:** React + Vite + TypeScript + Mantine (com `@mantine/notifications` para o toast), TanStack Query, React Router.
- **API:** Node + Express 5 + TypeScript, Postgres 16 e MinIO (S3 local), tudo em Docker Compose.
- **MinIO:** imagem `pgsty/minio`, um fork mantido, porque a imagem oficial saiu do Docker Hub em 2025.
- **Cache:** TanStack Query na versão boa, mais uma versão com cache escrito na mão para mostrar o que a biblioteca faz por baixo.

## Monitor e controles do apresentador

- O monitor é uma rota do próprio front (`/monitor`), aberta em outra aba. O apresentador alterna entre a lojinha e o monitor.
- Duas visões: **barras crescendo no tempo** (faixas Usuário, Tela, Navegador, API e Banco) e **diagrama de sequência**. Um inspetor mostra status, headers, body e o SQL de cada requisição.
- Eventos do navegador chegam por `BroadcastChannel`; eventos da API e do banco chegam por SSE.
- **Em localhost tudo responde na hora**, então o monitor tem um painel para forçar o mundo real: latência (até "Travada", 30s, para o tema Timeouts), taxa de erro, "Expirar sessão agora", "Conexão da lojinha: Offline" e "Esquecer URLs assinadas". A lojinha fica limpa, sem botões de aula.
- **Offline pelo monitor, não pelo DevTools**: o controle faz `navigator.onLine` dar `false`, dispara os eventos `offline`/`online` de verdade e faz as chamadas falharem como sem rede. O código das demos é o mesmo que funciona com o Offline do DevTools, mas ninguém precisa abrir o DevTools na frente da turma.

## Como alguns temas são feitos

- **Race conditions:** cliques rápidos entre abas de categoria (Eletrônicos demora 2s, as outras 0,3s), e não uma busca por texto. Com busca, o tema se confundia com o Debounce, que resolve a busca na prática; com cliques, debounce não faz sentido.
- **Erros úteis:** `{ errors: [{ code, message, field }] }`, com um code único por campo também na validação (e não um `VALIDATION_ERROR` genérico), e o `field` também no `409`.
- **Upload:** Sem progresso → Short polling → Long polling → SSE. O processamento anda aos trancos, para o short polling mostrar respostas repetidas e etapas puladas. O long polling é uma pergunta só, que a API segura até o fim.
- **Timeouts:** versão ruim sem limite (o spinner gira até a API responder); versão boa com `AbortSignal.timeout(5000)`, mensagem clara e "Tentar de novo".
- **Clique duplo:** uma transferência por Pix (para quem e valor). Começou como uma compra e virou Pix no dia da primeira turma. A chave de idempotência é reservada antes de enviar o dinheiro, vale 30s, recusa a mesma chave com outro Pix (`422`) e avisa quando a primeira ainda está processando (`409`). A última versão bloqueia a mesma pessoa e o mesmo valor em menos de 15s.
- **Offline:** com os favoritos. Na versão ruim, sem conexão aparece "Algo deu errado" e a ação se perde. Na boa, um aviso de "sem conexão", a ação vai para uma fila no `localStorage` e é enviada quando a conexão volta. Reenviar é seguro porque `PUT` e `DELETE` são idempotentes.
- **Signed URL:** a versão boa assina "como se fosse o começo do período", e a URL fica igual durante uma hora. Na lojinha o período começa quando a API sobe, e o botão "Esquecer URLs assinadas" recomeça, para mostrar de novo o primeiro download só trocando de versão.
- **Layout shift e Lazy Loading:** as fotos levam um `?visita=` que muda a cada abertura da tela, porque o navegador guarda na memória da aba as imagens já mostradas, mesmo com `no-store`, e a troca de versão não baixava nada.
- **Feedback de sucesso:** adicionar ao carrinho em três versões: nada acontece, alerta que bloqueia a tela e toast discreto.

## Material

### Folha do aluno

- **Uma A4, só a frente:** título e uma frase de abertura, o mapa dos 22 temas nos 4 blocos (número, nome, etiqueta e uma linha pontilhada para anotar), o intervalo entre os blocos 2 e 3, e um rodapé com os contatos.
- **QR codes:** a apostila em destaque, ao lado do título (aponta direto para o PDF no GitHub Pages deste repositório); no rodapé, a lojinha, este repositório (para quem quiser dar um minicurso parecido) e um link de indicação do Claude. O link da apostila também vai escrito, encurtado, para quem não tiver leitor de QR.
- **Sem data e local**: a mesma folha serve para as duas turmas e para uma próxima edição.
- O mesmo estilo da apostila (Fira Sans e Fira Mono, um vermelho só como destaque).

### Apostila

- **Para quem assistiu e quem não assistiu.** Cada tema se explica sozinho e cita a demo da lojinha em notas de margem.
- **Sem prints e sem o código exato das demos.** Prints do monitor não ficam bons no papel. No lugar entram figuras desenhadas para a apostila (a "tela desenhada" e a linha do tempo) e código simplificado, que explica a ideia sem copiar o arquivo da demo.
- **Estilo:** Fira Sans e Fira Mono, fundo branco, `#b4321f` como única cor de destaque, coluna de notas na margem direita ("Na lojinha", "Na aula", "Ver também"), seções numeradas. Escolhido depois de comparar direções diferentes e referências de livros técnicos em PDF.
- **Estrutura de cada tema:** abertura; parágrafo de entrada (o que é); O problema (com a tela desenhada); Por que acontece (com a linha do tempo); A solução ("No front:" / "Na API:"); Cuidados, terminando num gancho para outro tema; No seu projeto.
- **Termo técnico usado em inglês fica em inglês** (header, body, skeleton, infinite scroll, promise). "Requisição" para o HTTP, nunca "pedido".
- **Ligação com o código:** cada bloco, figura e nota da apostila aponta para os arquivos da lojinha de onde saiu, e um script avisa quando o código mudou depois da última geração.
- Todas as regras estão em `03-material/apostila/ESTRUTURA.md`, que é a fonte única de como a apostila é feita.

### Slides

- PDF 16:9 em vez de .pptx: as fontes vão embutidas e o arquivo abre igual em qualquer notebook.
- 15 slides no estilo da apostila: abertura (conceitos, a requisição em 3 passos, métodos e status com rotas reais da lojinha, Nielsen, a ideia do curso, os 4 blocos, a saída para o monitor) e fechamento com os QR codes e os contatos.

### Versões

- Durante a preparação, toda alteração no material virou um arquivo novo (`vN-descricao`), sem sobrescrever nenhuma versão. Assim dava para comparar e voltar atrás.
- Neste repositório fica só a versão final de cada peça. A apostila final é a v12, feita depois das turmas para alinhar o texto com a lojinha.
