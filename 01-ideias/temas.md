# Temas

22 temas, separados por onde a solução mora. Antes deles, uma abertura curta de **Conceitos** (UX, API, requisição, métodos, status codes e os limites do Nielsen), a única parte com slides.

Na aula, a ordem não é esta: os temas seguem a vida de uma ação do usuário, em 4 blocos (ver `02-roteiro/roteiro.md`). Esta lista agrupa pelo lado que resolve, que é como cada tema ganhou a sua etiqueta.

## Frontend

- **Formulários e validação**: erro só depois que o usuário sai do campo (ou clica no botão), botão com cara de desabilitado (`aria-disabled`) que, clicado, mostra todos os erros e leva ao primeiro; nada é apagado. Com debate: desabilitar o botão ou não? A turma vota, e a última versão junta o melhor das duas.
- **Estados da tela**: loading, erro, vazio e sucesso; o estado vazio deve orientar o usuário, não só dizer "nada encontrado".
- **Skeleton Loading**: a percepção de velocidade importa tanto quanto a velocidade real.
- **Layout shift**: o botão que muda de lugar na hora do clique porque uma imagem carregou acima dele; reservar espaço evita o salto.
- **Debounce e Throttle**: debounce na busca (uma requisição quando o usuário para de digitar, não uma por tecla) e throttle no scroll.
- **Race conditions e AbortController**: o usuário clica em Eletrônicos e logo depois em Casa; a resposta de Eletrônicos chega por último e a aba Casa mostra eletrônicos. Cancelar a requisição anterior resolve.
- **Feedback de sucesso**: o usuário precisa saber que a ação funcionou: toast discreto, nem silêncio nem alerta que trava a tela.
- **Lazy Loading**: baixar as imagens só quando forem aparecer na tela (`loading="lazy"`).
- **URL como estado**: filtros e busca na URL para não perder nada no F5, no voltar ou ao compartilhar o link.

## API

- **Erros úteis**: status codes corretos (`422` dado inválido, `409` conflito) e erro customizado: `{ errors: [{ code, message, field }] }`, com um code único por erro (ex.: `PRODUCT_NAME_TAKEN`). O front mapeia o code para a mensagem (dá até para usar como chave de tradução) e coloca cada uma embaixo do campo certo.
- **Rate Limiting**: proteger a API contra excesso de requisições e responder `429` com "tente novamente em X segundos", em vez de um erro genérico.
- **N+1 requests**: a API deve entregar o que a tela precisa; a tela não deveria fazer 15 requisições para montar uma página.

## Frontend + API

- **Clique duplo e idempotência**: num Pix, o front trava o botão durante o envio e a API usa uma chave de idempotência para que dois envios iguais não virem duas transferências. Por último, o bloqueio de Pix duplicado (mesma pessoa e mesmo valor em pouco tempo).
- **Optimistic UI**: atualizar a interface antes da resposta do servidor e desfazer se der erro.
- **Timeouts**: o spinner não pode girar para sempre; depois de alguns segundos, mostrar mensagem e opção de tentar de novo.
- **Retries e exponential backoff**: tentar de novo quando a API falha por um momento, sem sobrecarregar o servidor nem incomodar o usuário.
- **Offline e conexão instável**: avisar que caiu a conexão, guardar o que o usuário fez e sincronizar quando voltar.
- **Pagination vs Infinite Scroll**: primeiro o problema de não paginar (tudo de uma vez); depois vantagens, desvantagens, performance e UX de páginas e infinite scroll; do lado da API, paginação por cursor para não pular nem repetir itens.
- **Caching**: mostrar o dado que já existe e atualizar por trás; evitar dado velho e buscar de novo só quando precisa.
- **Imagens com signed URL e cache**: a API devolve a mesma signed URL durante um período, para o navegador reaproveitar a imagem em vez de baixar tudo a cada refresh.
- **Sessão expirada**: o usuário não pode perder o formulário preenchido porque o login expirou.
- **Upload com progresso e tempo real**: a barra de progresso do envio e o progresso do processamento por short polling, long polling e SSE (com Postgres LISTEN/NOTIFY), e o que muda entre os três.

## Se precisar cortar

Primeiros a sair, nesta ordem: URL como estado, Lazy Loading, Pagination vs Infinite Scroll. Ter essa ordem decidida antes da aula evita escolher no improviso quando o tempo aperta.

## Ficaram de fora

CORS, Web Storage (comparação técnica), CI/CD, variáveis de ambiente, pirâmide de testes, observabilidade, SSR/CSR/SSG, code splitting como tema próprio, XSS/CSRF/SQL Injection, webhooks, feature flags, API contracts, acessibilidade como tema próprio e "Desfazer em vez de Tem certeza?". Motivo: o curso é sobre o que o usuário sente, nos dois lados. Temas puramente técnicos, que não mudam o que a pessoa vê na tela, ficaram para outro curso.
