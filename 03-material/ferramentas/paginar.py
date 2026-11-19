# Uso (de dentro de 03-material/ferramentas): python paginar.py ../apostila/apostila.html
# Confere a apostila contra o código da lojinha (conferir-codigo.py, só avisa), gera o PDF,
# descobre em que página começa cada seção (pelos links do sumário), grava os números no objeto
# PAGINAS do HTML, gera de novo com o sumário preenchido e grava o apostila/fontes.lock.json.
import json, os, re, subprocess, sys
import fitz  # pip install pymupdf

html = sys.argv[1]
saida = html[:-5]

def gerar():
    subprocess.run(['node', 'gerar.mjs', html, saida], check=True, shell=(os.name == 'nt'))

def gravar_paginas(paginas):
    fonte = open(html, encoding='utf-8').read()
    nova = re.sub(r'/\*PAGINAS\*/.*?/\*FIM\*/', '/*PAGINAS*/' + json.dumps(paginas) + '/*FIM*/', fonte, flags=re.S)
    if nova != fonte:
        open(html, 'w', encoding='utf-8').write(nova)
    return nova != fonte

subprocess.run([sys.executable, 'conferir-codigo.py', html])

gerar()
paginas = {}
with fitz.open(saida + '.pdf') as pdf:
    for pagina in pdf:
        for link in pagina.get_links():
            if link.get('nameddest'):
                paginas.setdefault(link['nameddest'], link['page'] + 1)
if gravar_paginas(paginas):
    gerar()

# Páginas maiores que A4 (a capa com sangria): grava o corte (TrimBox) e a sangria (BleedBox)
# para a gráfica. A sobra é a mesma em cada borda.
with fitz.open(saida + '.pdf') as pdf:
    mudou = False
    for pagina in pdf:
        r = pagina.mediabox
        sobra = (r.width - 595.28) / 2
        if sobra > 1:
            pagina.set_bleedbox(r)
            pagina.set_trimbox(fitz.Rect(r.x0 + sobra, r.y0 + sobra, r.x1 - sobra, r.y1 - sobra))
            mudou = True
    if mudou:
        pdf.save(saida + '.tmp.pdf')
if mudou:
    os.replace(saida + '.tmp.pdf', saida + '.pdf')

subprocess.run([sys.executable, 'conferir-codigo.py', html, '--gravar'], stdout=subprocess.DEVNULL)
if os.path.exists(saida + '.png'):
    os.remove(saida + '.png')
print(json.dumps(paginas))
