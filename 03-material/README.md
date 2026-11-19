# Material

Os slides, a folha do aluno, a apostila e as ferramentas que geram os PDFs. As decisões sobre o material estão em `01-ideias/decisoes.md`, seção "Material".

| Pasta | O que tem |
|---|---|
| `slides/` | Os 15 slides da abertura e do fechamento (`slides.pdf`) e o HTML que gera o PDF |
| `folha/` | A folha do aluno (`folha.pdf`): uma A4 com o mapa dos 22 temas, linhas para anotar e os QR codes |
| `apostila/` | A versão final, v12: `apostila.pdf` e `apostila.html`, a fonte que gera o PDF. `ESTRUTURA.md` diz como a apostila é feita, e `fontes.lock.json` liga a apostila ao código da lojinha |
| `ferramentas/` | Os scripts que geram os PDFs |

O QR code da folha e o link `encurtador.com.br/vwap` apontam para `adriangpo.github.io/minicurso-lojinha-ux/03-material/apostila/apostila.pdf`. Por isso o `apostila.pdf` não muda de lugar; uma apostila nova substitui esse arquivo.

## Ferramentas

- `gerar.mjs`: abre um HTML no Chrome, troca os elementos `.qr` (atributo `data-url`) por QR codes e gera o PDF (e um `.png` de prévia).
- `paginar.py`: gera a apostila duas vezes, para preencher o sumário com os números de página, e grava o corte e a sangria da capa para a gráfica.
- `conferir-codigo.py`: avisa quando o código da lojinha mudou desde a última geração da apostila (ver `apostila/ESTRUTURA.md`, 7.1). Precisa da lojinha clonada em `04-apps/`, na raiz deste repositório.

Precisam do Google Chrome instalado, de Node e de internet (as fontes vêm do Google Fonts). O `paginar.py` precisa também de Python com `pip install pymupdf`.

```bash
cd 03-material/ferramentas
npm install            # só na primeira vez

# um PDF qualquer (slides, por exemplo)
node gerar.mjs ../slides/slides.html ../slides/slides

# a apostila inteira, com sumário
python paginar.py ../apostila/apostila.html
```

## Versões

Durante a preparação, toda alteração virou um arquivo novo (`vN-descricao`), sem sobrescrever nenhuma versão. Aqui fica só a versão final de cada peça: a apostila v12 e a folha final.
