# Estrutura da apostila

Documento interno, para quem for mexer na apostila: uma pessoa ou um agente de IA. Não vai para os alunos. Foi escrito durante a preparação, para que toda sessão nova de trabalho (nossa ou da IA) seguisse as mesmas regras sem precisar redescobrir nada.

Este arquivo é a fonte única de como a apostila é feita. **Regra de manutenção:** quando algo mudar aqui (uma medida, uma cor, a ordem das seções), a mudança vale para todos os temas já feitos, e eles precisam ser atualizados também. A exceção é quando a mudança for decidida como específica de um tema; nesse caso, ela é registrada na seção "Exceções por tema", no fim deste arquivo.

Histórico das decisões: `01-ideias/decisoes.md`, seção "Material". Referência atual: a apostila completa, `apostila/apostila.html` (v12, 65 páginas). Ela é o modelo-base: os temas novos ou refeitos seguem o HTML dela, e as figuras saem das funções `tela()` e `tempo()` que estão no fim do arquivo, que já aplicam as medidas deste documento.

---

## 1. Público e tom

- Quem assistiu e quem não assistiu. Cada tema se explica sozinho; as ligações com a aula ficam nas notas de margem.
- **A lojinha é a fonte da verdade.** Nenhuma tecnologia, solução, rota, número ou tela que a lojinha não tem. Dicas de cuidado são bem-vindas, desde que não digam que a lojinha faz algo que ela não faz.
- Português do Brasil. Texto corrido, frases diretas, exemplos concretos da lojinha.
- Proibido: emoji, ícones, caixinhas "Dica"/"Atenção", gradientes, cards com sombra, listas onde caberia um parágrafo, negrito no meio da frase, títulos como "Por que isso importa?" ou "Em resumo", texto genérico.
- Termo técnico novo aparece em itálico na primeira vez que é explicado (ex.: *race condition*). Depois, sem itálico.
- A requisição HTTP é sempre "requisição", nunca "pedido" (decidido na v10).
- Termo técnico que o programador usa em inglês fica em inglês, sem tradução: promise (não "promessa"), header, body, loop, render, background, skeleton, infinite scroll, signed URL, rate limiter. Itálico só quando o termo é explicado ali, pela regra de cima. Ficam em português os termos que o programador brasileiro também diz em português: requisição, resposta, estado, rota, fila, tentativa, evento, chamada.
- Os exemplos usam produtos e categorias que existem de verdade na lojinha (`04-apps/api/banco/02-produtos.sql`). Não inventar produto.

## 2. Estrutura de cada tema

Ordem fixa. "N" é o número do tema (1 a 22, a mesma ordem da folha do aluno e do roteiro).

1. **Abertura** — filete, "Tema N · Etiqueta" e o nome do tema (ver 4.3). Etiqueta: `Frontend`, `API` ou `Frontend + API`.
2. **Parágrafo de entrada, sem título** — o que é, em 2 ou 3 frases simples, sem jargão. Quem nunca ouviu o nome do tema precisa entender do que se trata.
3. **N.1 O problema** — um caso concreto da lojinha, contado do ponto de vista de quem usa, terminando no prejuízo para a pessoa (perdeu o formulário, comprou duas vezes, viu o resultado errado). É aqui que se responde "por que fazer"; não existe seção separada para isso. Leva a figura da **tela desenhada** (ver 5.1).
4. **N.2 Por que acontece** — o mecanismo por baixo (rede, navegador, servidor, banco). Leva a figura da **linha do tempo** (ver 5.2) quando ela ajudar.
5. **N.3 A solução** — o título diz onde ela mora: "No front: …" ou "Na API: …". Em tema `Frontend + API`, as duas, uma depois da outra (N.3 e N.4; as seções seguintes andam um número). Leva o código simplificado (ver 6).
6. **N.4 Cuidados** — o que a solução não resolve, quando não usar, custos. Entra sempre que houver algo real a dizer; não inventar cuidado para preencher.
   **Gancho para outro tema:** sempre que possível, Cuidados termina num gancho. O limite da solução leva ao tema que trata desse limite, citado pelo número e pelo nome no próprio texto, entre parênteses. Exemplo do tema 8: "Abortar um `POST` de compra não desfaz a compra: o pedido pode já ter sido gravado. Para ações que mudam dados, o caminho é outro (tema 14, Clique duplo e idempotência)." Se o tema seguinte na ordem for o que resolve, melhor ainda: a apostila passa a se ler como uma sequência, como a aula ("tentar de novo" leva a Retries, que leva a idempotência). O gancho fica no texto, não numa nota de margem.
   **Citações viram link:** toda citação de outro tema leva à seção dele no PDF, e só o nome do tema é clicável, nunca o "tema N": `(tema 4, <a class="ref" href="#t4">Estados da tela</a>)`. Quando o nome já está escrito no texto ("o skeleton (tema 5)"), o link fica nessa palavra; quando não está, a citação é completada para "(tema N, Nome)". O link aparece com um sublinhado fino em `#bbb`.
7. **N.5 No seu projeto** — sempre a última seção. Um teste de 2 ou 3 frases que a pessoa faz no próprio sistema, com o que observar.

Os números de seção são contínuos: se Cuidados não existir, "No seu projeto" vira N.4.

**Notas de margem** (ver 4.6), fora do texto principal, junto do parágrafo a que se referem:
- "Na lojinha," — quais versões a página do tema tem e como reproduzir;
- "Na aula," — o que o monitor mostrou;
- "Ver também" — ligação com outro tema, pelo número e nome.

**Limites por tema:**
- 2 a 3 páginas. A meta original era 1 a 2, mas na v9 os temas ficaram com 2 a 3 páginas, inclusive com sobras quase vazias, e decidimos não enxugar.
- No máximo 2 figuras.
- No máximo 2 blocos de código, de até umas 20 linhas cada, com no máximo 90 caracteres por linha (mais que isso estoura a caixa; quebre a linha ou encurte o comentário).
- Uma tabela, se o tema pedir uma comparação (ver 6.1).
- Cada tema começa em página nova.

## 3. Cores

| Nome | Valor | Onde |
|---|---|---|
| tinta | `#111` | texto, títulos, contornos e barras das figuras |
| acento | `#b4321f` | "Tema N · Etiqueta", números das seções (8.1), início das notas ("Na lojinha,"), o elemento errado/ruim das figuras. Nada mais. |
| cinza | `#666` | cabeçalho corrido, rótulos secundários das figuras, tracejado de cancelado |
| texto da nota | `#444` | notas de margem |
| legenda | `#333` | legendas das figuras |
| claro | `#d2d2d2` | barras de produto dentro das telas desenhadas |
| campo | contorno `#888`, fundo `#fff` | caixas de texto dentro das telas desenhadas |
| pontilhado | `#bbb` | faixa "na tela" vazia, na linha do tempo |
| fundo | `#fff` | a página inteira |

Fundo e bordas dos blocos de código: ver 6.

## 4. Página e tipografia

### 4.1 Página
- A4. Margens: 22 mm em cima, 18 mm à direita, 24 mm embaixo, 22 mm à esquerda.
- Área útil: 170 mm de largura. Dentro dela:
  - **coluna de texto:** 122 mm (à esquerda);
  - **espaço entre colunas:** 8 mm;
  - **coluna de notas:** 40 mm (à direita).
- Figuras e blocos de código ocupam a largura toda (170 mm), por cima da coluna de notas. Não colocar nota de margem na mesma altura de uma figura ou de um bloco de código.
- Em CSS: `body { padding-right: 48mm }`, e figuras/código com `margin-right: -48mm`.

### 4.2 Fontes (Google Fonts)
- **Fira Sans** (400, 500, 600 e itálico 400): texto, títulos, notas, legendas e texto dentro das figuras.
- **Fira Mono** (400, 500): todo código, em bloco e no meio do texto.
- Nenhuma outra fonte. A folha do aluno usa as mesmas desde a v12 (antes era IBM Plex).

### 4.3 Abertura do tema
- Filete de 0,5 pt em `tinta`, na largura toda (170 mm); 6 mm de espaço acima, 4 mm entre o filete e o texto.
- "Tema N · Etiqueta": Fira Sans 10 pt, peso 500, `acento`. Número sem zero à esquerda ("Tema 8").
- Nome do tema (h1): Fira Sans 22 pt, peso 600, entrelinha 1,15, `letter-spacing: -0.005em`, 1,5 mm abaixo da linha anterior.
- 9 mm de espaço até o parágrafo de entrada.

### 4.4 Texto
- Fira Sans 10,3 pt, entrelinha 1,5, `tinta`.
- Alinhado à esquerda (sem justificar), hifenização automática, sem recuo de parágrafo, 2,6 mm entre parágrafos.
- Pelo menos 3 linhas por parágrafo antes e depois de uma quebra de página (`orphans/widows: 3`).

### 4.5 Títulos de seção (h2)
- Fira Sans 12 pt, peso 600, `tinta`. 7 mm acima, 2 mm abaixo. Nunca fica sozinho no pé da página.
- Número "N.M" em `acento`, seguido de 3 mm de espaço: `8.1  O problema`.

### 4.6 Notas de margem
- Na coluna de notas (40 mm), alinhadas ao topo do parágrafo a que se referem.
- Fira Sans 8,4 pt, entrelinha 1,4, cor `#444`.
- Começam com "Na lojinha,", "Na aula," ou "Ver também" em `acento`, peso 500, sem itálico. O resto da frase segue normal.
- No máximo umas 4 linhas por nota, e no máximo 3 notas por tema.

### 4.7 Cabeçalho e rodapé
- Cabeçalho à esquerda: "Do Clique à API: UX de Verdade". À direita: "Tema N · Nome curto" (ex.: "Tema 8 · Race conditions"). Fira Sans 8,5 pt, `cinza`. Sem filete.
- Número da página no rodapé, à direita: Fira Sans 9 pt, peso 500, `tinta`.

## 5. Figuras

Sem prints da lojinha ou do monitor: as figuras são desenhadas para a apostila, em SVG, simplificando o que a tela e o monitor mostram. Dois tipos, sempre no mesmo desenho:

Regras gerais:
- Largura toda (170 mm), centralizadas, 6 mm acima e abaixo. Não quebram entre páginas.
- O SVG é desenhado num `viewBox` de 600 de largura; 1 unidade = 0,283 mm impresso. Os tamanhos abaixo estão nessas unidades.
- Texto das figuras em Fira Sans (a mesma do texto, não mono).
- Uma cor só para chamar atenção: `acento`, sempre no elemento errado/ruim. O resto em `tinta`, `cinza` e `claro`.
- Legenda embaixo, centralizada: "Figura N.M. Texto." em Fira Sans 8,8 pt, cor `#333`, 3 mm abaixo da figura. M conta as figuras dentro do tema (8.1, 8.2).
- O texto principal sempre menciona a figura ("A figura 8.2 mostra…") antes ou logo depois dela.

### 5.1 Tela desenhada (a "tela fake")
É o recurso principal: mostra o que a pessoa vê, em quadros lado a lado, cada um num momento.

- `viewBox="0 0 600 214"` (170 × 61 mm impressos) com a altura padrão do quadro; com quadro de 200, `0 0 600 226`.
- **3 quadros** por padrão, ou 2 quando cada quadro precisa de mais largura (texto longo, grade de imagens). 4 não cabem.
- Largura do quadro = (598 − 32 × (n − 1)) / n: 177,3 com 3 quadros, 283 com 2. Espaço de 32 entre quadros; o primeiro começa em x = 1; y = 24.
- Altura do quadro: 188; até 200 quando o conteúdo não couber (temas 1 e 16).
- Contorno de 1 em `tinta`, sem fundo, cantos retos.
- Acima de cada quadro, o momento ("1,0 s") ou o passo, em 11, `cinza`, centralizado, y = 12.
- Dentro do quadro (coordenadas relativas ao quadro):
  - campo de texto: retângulo 154 × 24 em (12, 12), contorno `#888` de 0,8, fundo branco; texto a 20 da borda, 12, `tinta`;
  - título/rótulo da tela: em (12, 60), 11, peso 500, `tinta`;
  - linhas de produto: barras 154 × 12, `claro`, começando em y = 72, uma a cada 18;
  - abas, quando houver (no lugar do campo de texto): nomes em 10,5 na linha y = 28, a partir de x = 12, com uns 12 de espaço entre um nome e outro; a aba marcada em `tinta`, peso 500, com um traço de 2 em `tinta` embaixo (y = 34, da largura do nome); as outras em `cinza`; uma linha de 1 em `claro` de x = 12 a 166 em y = 35. Mostrar só as abas que cabem (no tema 8: Eletrônicos, Livros, Casa);
  - carregando: "Carregando…" em 11, `cinza`, no lugar do título, sem linhas de produto;
  - botões, quando houver: retângulo de altura 24, contorno `tinta` 1, fundo branco, texto 11 peso 500 centralizado; botão desabilitado com contorno `#bbb`, fundo `#f1f2f4` e texto `#999`.
- Os elementos ficam empilhados de cima para baixo, a partir de y = 12, com 8 de espaço entre um e outro (4 em listas compactas). Além dos de cima, a função `tela()` tem:
  - campo com rótulo (9,5, `cinza`, acima) e com erro (contorno `acento` e a mensagem embaixo em 9,5, `acento`); campo vazio mostra a dica em `#999`;
  - endereço da página: faixa de 18 em `#f1f2f4` com a URL em 9, `cinza`;
  - texto solto: 10, `cinza` (ou `tinta`), uma linha a cada 13;
  - aviso: caixa de contorno 0,8 (`tinta`, ou `acento` quando é o erro ruim), primeira linha em 9,5 peso 500;
  - spinner: círculo de raio 11 em `claro` com um quarto em `tinta`, espessura 2,5;
  - skeleton: cards de altura 34 com contorno `claro` e dois blocos `#e3e3e3` (55% e 28% da largura);
  - card de produto: altura 34, contorno `claro`, nome em 10 e preço em 9,5 `cinza`;
  - item de lista: texto em 10 com filete `claro` embaixo; à direita, um coração desenhado (vazio ou cheio em `tinta`, nunca em vermelho) ou uma palavra curta;
  - foto: retângulo `#e9e9e9`;
  - grade de fotos: 3 ou 4 colunas na proporção 4:3; as que não foram baixadas ficam tracejadas em `#bbb`, e uma linha tracejada marca o "fim da tela";
  - barra de progresso: rótulo em 9,5, barra de 8 com contorno `tinta` e preenchimento `tinta`, legenda em 9 `cinza`.
- Por cima do quadro, quando precisar: o cursor (seta branca com contorno `tinta`), o toast (caixa no canto de baixo à direita, 9 pt) e o modal (o quadro escurece 10% e uma caixa branca com contorno `tinta` aparece por cima).
- Mensagens de erro de campo ficam em `acento` mesmo na versão boa, porque é assim que a tela de verdade mostra; o contorno vermelho do quadro continua reservado para a versão ruim.
- **O quadro errado/ruim:** contorno em `acento` com espessura 1,6, e o texto que está errado em `acento`, peso 600. Só um quadro por figura fica em `acento`.
- Esboço, não maquete: sem logo, sem ícone, sem imagem de produto, sem sombra, sem cor além das listadas.

### 5.2 Linha do tempo
É a figura técnica: mostra o que acontece por baixo, como o monitor da aula, só com o essencial.

- Largura de 600; a altura sai do número de painéis e linhas (a função `tempo()` calcula). Em geral, dois painéis: ruim em cima, boa embaixo.
- Coluna de rótulos: x de 0 a 70 (cabe um nome como "Eletrônicos" em 10,5); pode crescer até uns 180 quando os rótulos forem longos, como rotas ("GET /produtos/7/comentarios"). Área do tempo: do fim da coluna até x = 574. A escala é escolhida por tema para o eixo caber nesse trecho, e as barras devem terminar antes de uns 80% do eixo, para o texto do fim caber.
- Requisições em sequência, que não se sobrepõem, podem dividir a mesma linha (as perguntas do polling, as tentativas do retry).
- Outros tipos de barra: falha esperada na versão boa em cinza `#9a9a9a`; resposta que veio do cache com só o contorno `tinta`, fundo branco; evento instantâneo (uma tecla, uma novidade no servidor) como um traço vertical de 1,5.
- Na faixa "na tela", a espera ("carregando") fica tracejada em `#bbb` com texto `cinza`; quando a espera é o problema, tracejada em `acento`.
- Título do painel ("Sem cancelamento"): 11,5, peso 600, `tinta`.
- Uma linha por requisição, a cada 22 de altura. Rótulo à esquerda em 10,5.
- Barra da requisição: altura 8, `tinta`; a requisição que causa o problema em `acento`.
- Texto ao fim da barra (ordem de chegada, status): 10, `cinza` (em `acento` se for a barra errada).
- Requisição cancelada: linha tracejada (4 3), espessura 1,5, `cinza`, do envio até o cancelamento, seguida de "cancelada" (ou "cancelada no clique em X") e com o rótulo da linha em `cinza`.
- Faixa "na tela" embaixo de cada painel: retângulos de altura 18 com contorno `tinta` 0,9 e o conteúdo escrito dentro (10, centralizado); o trecho errado preenchido com `acento` e texto branco; antes da primeira resposta, linha pontilhada (2 3) em `#bbb`.
- Eixo: linha `tinta` 0,8, marcas de 4, rótulos em 10, `cinza`, com vírgula decimal ("0,5 s").
- Espera de propósito (backoff, Retry-After), quando aparecer: barra tracejada em `cinza`, mesma altura da barra normal.

## 6. Código

- O código da apostila é **simplificado**: explica a ideia em poucas linhas e não copia o arquivo da demo. Sem caminho de arquivo. Mas segue a mesma solução da demo (mesma API, mesmos nomes de rota quando fizer sentido), para quem abrir a lojinha reconhecer.
- Nomes de variáveis e funções em português, como na lojinha (`controle`, `buscar`, `mostrarProdutos`).
- JavaScript puro primeiro; se o tema tiver uma forma típica em React, um segundo bloco com ela.
- Comentários curtos no fim da linha, só onde explicam algo que o texto não explicou.

**Bloco de código** (como um bloco de markdown no GitHub):
- Largura toda (170 mm), 3,5 mm acima e 4 mm abaixo. Não quebra entre páginas.
- Fundo `#f6f8fa`, borda de 0,6 pt em `#d8dde3`, cantos arredondados de 4 px, espaço interno de 3,5 mm em cima e embaixo e 4 mm dos lados.
- Fira Mono 8,4 pt, entrelinha 1,5.
- **Rótulo do lado:** todo bloco começa com uma linha curta que diz onde aquele código roda: `API · Servidor`, `Frontend · Navegador` (JavaScript ou React), `Frontend · HTML`, `Frontend · CSS`, `Terminal` e, para exemplos que não são código, `Na rede`. Rótulos encurtados na v11. Vai no atributo `data-lado` do `pre` e é desenhado pelo CSS: Fira Sans 7,8 pt, peso 500, `cinza`, com um filete de 0,5 pt em `#d8dde3` embaixo, separando do código.
- Cores de sintaxe (paleta clara do GitHub), aplicadas pelo highlight.js 11.9.0 (cdnjs) na hora de gerar o PDF:
  - palavras-chave (`let`, `async`, `if`, `return`, `new`): `#cf222e`;
  - nomes de função: `#8250df`;
  - textos entre aspas: `#0a3069`;
  - números, propriedades, atributos: `#0550ae`;
  - comentários: `#6e7781`, itálico;
  - o resto: `tinta`.

**Código no meio do texto** (`fetch`, `abort()`): Fira Mono a 0,86 do tamanho do texto, fundo `#f1f2f4`, cantos de 3 px, 1 mm de espaço dos lados.

### 6.1 Tabelas
- Só para comparações que ficariam confusas em texto (no tema 11: short polling, long polling e SSE).
- Largura toda (170 mm), Fira Sans 9 pt, entrelinha 1,4. Sem linhas verticais e sem fundo.
- Filete de 0,5 pt em `tinta` em cima e embaixo do cabeçalho e no fim da tabela; filete de 0,3 pt em `claro` entre as linhas.
- Cabeçalho em peso 600, alinhado à esquerda.

## 7. Arquivos e geração

- Pastas: este arquivo, a fonte `apostila.html` e o `apostila.pdf` ficam em `03-material/apostila/`. O `apostila.pdf` é o endereço do QR code da folha e não muda de lugar. Durante a preparação, cada mudança virou um arquivo novo `vN-descricao`; aqui fica só a versão final.
- PDF gerado com `03-material/ferramentas/gerar.mjs` (Chrome + Playwright), rodando de dentro de `ferramentas/`: `node gerar.mjs ../apostila/apostila.html ../apostila/apostila`. O `.png` que ele cria é só prévia; pode apagar.
- A apostila inteira é gerada com `python paginar.py ../apostila/apostila.html` (também de dentro de `ferramentas/`; precisa do `pymupdf`). Ele roda a conferência com o código (ver 7.1), gera o PDF, lê em que página começa cada seção pelos links do sumário, grava os números no objeto `PAGINAS` do HTML e gera de novo, com o sumário preenchido. No fim, grava o `apostila/fontes.lock.json`.
- As figuras são descritas no objeto `FIGURAS`, no fim do HTML, e desenhadas pelas funções `tela()` e `tempo()` dentro de cada `[data-fig]`; o highlight.js roda no mesmo momento.
- Cada seção tem um `data-cab` com o texto do cabeçalho; o script cria uma página nomeada para cada uma, para o cabeçalho mostrar o tema certo. Os temas também levam `data-tema`, `data-bloco`, `data-etiqueta` e `data-nome`, de onde saem o sumário e as listas das aberturas de bloco.
- O PDF sai com links internos (sumário clicável) e marcadores, montados pelo Chrome a partir dos `h1` e `h2` (`outline: true` no `gerar.mjs`).
- Antes de entregar: gerar o PDF, converter as páginas em imagem e conferir se nada estoura (código passando da caixa, nota batendo em figura, título sozinho no pé da página).

### 7.1 Ligação com o código da lojinha

A apostila acompanha o código das demos sem mexer nele. Os caminhos começam em `04-apps/`, que é o repositório [lojinha-ux](https://github.com/adriangpo/lojinha-ux) clonado dentro deste (`git clone https://github.com/adriangpo/lojinha-ux 04-apps`; a pasta está no `.gitignore`). Nenhum marcador vai para os arquivos de `04-apps`, porque eles são mostrados na aula. A ligação fica toda no HTML da apostila.

- Cada bloco de código, figura e nota "Na lojinha" de um tema tem um `id` e um `data-fonte` com os arquivos de origem, a partir da raiz do projeto e separados por espaço: `<pre id="t08-codigo-1" data-fonte="04-apps/web/src/temas/race-condition/CliquesComCancelamento.tsx">`. Ids: `tNN-codigo-M`, `tNN-figura-M` e `tNN-versoes`.
- O que apontar: no código, o arquivo da versão boa de onde a ideia saiu (e a rota da API, quando o bloco é de servidor); na figura, todos os arquivos da pasta do tema, mais a rota da API se houver; na nota de versões, `04-apps/web/src/temas.ts` mais os mesmos da figura. Todo bloco tem equivalente na lojinha (seção 1): o que a lojinha não faz não entra.
- `python conferir-codigo.py ../apostila/apostila.html`, de dentro de `ferramentas/`, faz duas checagens e só avisa:
  - blocos com o atributo `data-literal` (copiados do arquivo, não simplificados): cada linha precisa existir, na mesma ordem, nos arquivos de origem, sem contar espaços nas pontas, linhas vazias e linhas de reticências (`...` ou `// ...`) que marcam corte. Hoje nenhum bloco é literal, porque o código da apostila é simplificado (seção 6); a checagem fica pronta para quando houver;
  - todo o resto: compara o hash de cada arquivo de origem com o `apostila/fontes.lock.json`, gravado na última geração, e lista os arquivos que mudaram com os ids da apostila que dependem deles. Arquivo de origem que sumiu também aparece.
- O `paginar.py` roda a conferência antes de gerar e grava o `fontes.lock.json` depois. Depois de revisar o que a conferência apontou, basta gerar de novo.

## 8. Partes fora dos temas

Ordem: capa, como usar a apostila, sumário, os limites de tempo, os 4 blocos (cada um com sua abertura e seus temas), checklist, como rodar a lojinha, referências.

**Capa** (a "faixa", opção 3 da v7). Página sem margem, sem cabeçalho e sem número.
- Faixa `acento` de 210 × 205 mm no topo, com espaço interno de 22 mm em cima, 18 à direita, 16 embaixo e 22 à esquerda. Dentro, em branco: "Apostila do minicurso" (10 pt, peso 500) no topo; o título "Do Clique à API: / UX de Verdade" em duas linhas (54 pt, peso 600, entrelinha 1,02, `letter-spacing: -0.02em`) encostado no pé da faixa; embaixo, a frase da folha do aluno em 14 pt, peso 300, branco a 88%, largura máxima de 145 mm, 9 mm abaixo do título.
- Pé branco (o resto da página), com 18 mm à direita, 20 embaixo e 22 à esquerda. Alinhados ao pé: à esquerda os nomes (Adrian Gustavo de Paiva Oliveira e Pedro Ferreira, 10 pt, peso 500); à direita "Lojinha UX", "o código das demos" e o endereço do repositório (8,5 pt, `cinza`, alinhados à direita) e o QR da lojinha de 24 mm.
- Sem data e sem local, como na folha.
- **Sangria:** a página da capa tem 216 × 303 mm (3 mm a mais em cada borda) e o conteúdo é deslocado 3 mm, ficando no mesmo lugar em relação ao corte. Por isso, no CSS, a faixa tem 208 mm de altura e espaço interno de 25/21/16/25 mm, e o pé tem 21/23/25 mm. A faixa vermelha cobre a sangria de cima e dos lados. O `paginar.py` grava no PDF o TrimBox (corte, 210 × 297) e o BleedBox (a página inteira) de toda página maior que A4. As outras páginas continuam A4, sem sangria, porque não têm nada impresso até a borda.

**Páginas de texto fora dos temas** (como usar, sumário, limites de tempo, checklist, como rodar, referências): mesma página, abertura e notas dos temas, com "Antes de começar" ou "Para levar" no lugar de "Tema N · Etiqueta".
- Sumário: uma página só, no modelo do LaTeX. Entradas de primeiro nível (como usar, limites de tempo, cada bloco como "Bloco N  Nome", checklist, como rodar, referências) em 10,3 pt peso 600, com o número da página em peso 600 e sem pontilhado, 3,6 mm acima. Os temas recuados 15 mm, em 10 pt, entrelinha 1,55, número do tema em `acento`, pontilhado espaçado (". . .") em `#999` até o número da página. O sumário ocupa a largura toda (170 mm). Cada linha é um link para a seção.
- Limites de tempo: uma figura com a escala de 0,1 s, 1 s e 10 s e os temas de cada faixa.
- Checklist: os 22 temas como pergunta, numa lista com caixinha de 3,6 mm, número em `acento` e filete `claro` entre os itens, agrupados por bloco.
- Referências: lista simples, título em 9,6 pt e endereço embaixo em Fira Mono 8 pt `cinza`, sem `https://`.

**Abertura de bloco**: página própria, sem cabeçalho e com número. Texto começando 60 mm abaixo da margem: "Bloco N" (11 pt, `acento`, peso 500), o nome do bloco (34 pt), um parágrafo em 12 pt peso 300 e a lista dos temas do bloco (número em `acento`, nome e etiqueta em `cinza`), com filete de 0,5 pt em cima.

## Pendências

Nenhuma. A v12, feita depois das turmas, alinhou a apostila com a lojinha: o tema 14 passou a ser o Pix, o long polling do tema 11 ficou igual ao da demo, os controles novos do monitor entraram e saiu tudo o que a lojinha não tem (WebSocket, Redis como alternativa, code splitting, `aspect-ratio`, `statement_timeout`).

## Como trabalhar na apostila (para uma pessoa ou um agente novo)

- Leia este arquivo inteiro e a seção "Material" de `01-ideias/decisoes.md`. Abra a versão atual (`apostila.html` e `apostila.pdf`; hoje a v12).
- Rodadas de feedback: os ajustes chegam aos poucos. Anote cada um num arquivo temporário, com status, e aplique todos numa única versão nova, gerada quantas vezes precisar até a rodada acabar. Não crie uma versão por ajuste.
- Para mudar algo: edite `apostila.html` e rode `python paginar.py ../apostila/apostila.html` de dentro de `03-material/ferramentas/`. O PDF sai em `apostila.pdf`, no mesmo lugar.
- O `paginar.py` mostra a conferência com o código (7.1). Se ela listar arquivos que mudaram, revise os trechos indicados antes de entregar. Quando uma demo muda, o tema da apostila é refeito em cima do código novo.
- Elementos novos: todo bloco de código, figura e nota "Na lojinha" de tema precisa de `id` e `data-fonte` (7.1), todo bloco de código precisa de `data-lado` (6) e toda citação de outro tema precisa de link (item 6 da seção 2).
- Confira o PDF antes de entregar: converta as páginas em imagem (pymupdf) e olhe tudo, em especial código passando da caixa (no máximo 90 caracteres por linha; conte com um script, porque o comentário alinhado à direita estoura fácil), figura com texto sobreposto, sumário com mais de uma página e a última página das referências.
- Mudou uma regra? Atualize este arquivo e aplique em todos os temas, a não ser que ela seja exceção de um tema.
- Não mexa no código da lojinha para acomodar a apostila: a apostila é que acompanha o código.

## Exceções por tema

- **Tema 2, Erros úteis:** a etiqueta é `API`, mas o tema tem uma seção "No front: o texto sai do code" (2.4) depois da solução na API, porque o argumento do tema é o front decidir o texto pelo code. Decidido em 2026-10-18.
