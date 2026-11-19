# Slides

`slides.pdf`: 15 slides em 16:9, feitos a partir de `slides.html`, no estilo da apostila (Fira Sans e Fira Mono, fundo branco, `#b4321f` como única cor de destaque, capa com a faixa vermelha). PDF em vez de .pptx: as fontes vão embutidas e o arquivo abre igual em qualquer notebook.

## Ordem

Abertura (slides 1 a 13): capa; "Qual foi o último app que te irritou?"; UX; API; a requisição em 3 passos (o passo atual em vermelho); métodos; status codes; limites de tempo do Nielsen; "UX não é só design. Metade dela é decidida na API."; os 4 blocos; a saída para a lojinha e o monitor.

Fechamento (slides 14 e 15): "A experiência do usuário é decidida nas duas pontas"; obrigado, com os QR codes da apostila, da lojinha e deste repositório, e os contatos.

## Por que tão poucos

Slides **só na abertura e no fechamento**. Do primeiro tema em diante, tudo é mostrado na lojinha e no monitor (ver `01-ideias/decisoes.md`). O último slide da abertura leva direto ao monitor, que mostra a mesma requisição do slide acontecendo de verdade.

Diretrizes que seguimos:

- Uma ideia por slide.
- Começar pelo problema, depois a solução.
- Código curto ou diagrama simples; nada de parágrafo.
- Fundo neutro, uma fonte e uma cor de destaque.
- O slide prepara a demo; não substitui.

## Gerar de novo

De dentro de `03-material/ferramentas` (ver `03-material/README.md`):

```bash
node gerar.mjs ../slides/slides.html ../slides/slides
```
