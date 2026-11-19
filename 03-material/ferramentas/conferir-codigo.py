# Uso (de dentro de 03-material/ferramentas): python conferir-codigo.py ../apostila/apostila.html [--gravar]
# Confere se a apostila ainda bate com o código da lojinha (o repositório lojinha-ux clonado em 04-apps). Só avisa, não muda nada,
# a não ser com --gravar, que grava os hashes atuais em apostila/fontes.lock.json.
#
# Cada bloco de código, figura e nota de versões da apostila tem um id e um data-fonte com os
# arquivos de origem (caminhos a partir da raiz do projeto, separados por espaço).
#  a) Blocos com data-literal: cada linha do trecho precisa existir, na mesma ordem, nos arquivos
#     de origem (sem contar espaços nas pontas, linhas vazias e linhas de reticências).
#  b) Todo o resto: o hash de cada arquivo de origem é comparado com o fontes.lock.json, gravado
#     na última geração. Os arquivos que mudaram aparecem com os ids da apostila que dependem deles.
import hashlib, html as h, json, os, re, sys

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
TRAVA = os.path.join(RAIZ, '03-material', 'apostila', 'fontes.lock.json')
RETICENCIAS = re.compile(r'^(//|#|/\*|<!--)?\s*(\.\.\.|…)\s*(\*/|-->)?$')


def elementos(fonte):
    for m in re.finditer(r'<(\w+)([^>]*\bdata-fonte="([^"]*)"[^>]*)>', fonte):
        tag, attrs, fontes = m.group(1), m.group(2), m.group(3).split()
        id_ = re.search(r'\bid="([^"]+)"', attrs)
        codigo = None
        if tag == 'pre':
            fim = fonte.index('</pre>', m.end())
            codigo = h.unescape(re.sub(r'<[^>]+>', '', fonte[m.end():fim]))
        yield (id_.group(1) if id_ else '(sem id)'), fontes, 'data-literal' in attrs, codigo


def linhas_uteis(texto):
    return [l.strip() for l in texto.splitlines() if l.strip() and not RETICENCIAS.match(l.strip())]


def conferir_literal(id_, fontes, codigo):
    origem = []
    for f in fontes:
        caminho = os.path.join(RAIZ, f)
        if os.path.exists(caminho):
            origem += linhas_uteis(open(caminho, encoding='utf-8').read())
    faltando, i = [], 0
    for linha in linhas_uteis(codigo):
        try:
            i = origem.index(linha, i) + 1
        except ValueError:
            faltando.append(linha)
    if faltando:
        print(f'  {id_} ({" ".join(fontes)}): {len(faltando)} linha(s) não estão no código, ou fora de ordem:')
        for l in faltando:
            print(f'      {l}')
    return not faltando


def hash_de(f):
    caminho = os.path.join(RAIZ, f)
    if not os.path.exists(caminho):
        return None
    return hashlib.sha256(open(caminho, 'rb').read()).hexdigest()


def main():
    html = sys.argv[1]
    itens = list(elementos(open(html, encoding='utf-8').read()))
    ok = True

    print('Conferência apostila x código')
    inexistentes = sorted({f for _, fs, _, _ in itens for f in fs if hash_de(f) is None})
    for f in inexistentes:
        ok = False
        ids = [i for i, fs, _, _ in itens if f in fs]
        print(f'  arquivo de origem não existe: {f} (usado em {", ".join(ids)})')

    literais = [(i, fs, c) for i, fs, lit, c in itens if lit]
    for i, fs, c in literais:
        ok = conferir_literal(i, fs, c) and ok

    atuais = {f: hash_de(f) for _, fs, _, _ in itens for f in fs if hash_de(f)}
    if not os.path.exists(TRAVA):
        print('  fontes.lock.json ainda não existe: nada para comparar (ele é gravado na geração).')
    else:
        antigos = json.load(open(TRAVA, encoding='utf-8'))['arquivos']
        mudaram = sorted(f for f in atuais if antigos.get(f) != atuais[f])
        if mudaram:
            ok = False
            print(f'  {len(mudaram)} arquivo(s) mudaram desde a última geração. Revisar:')
            for f in mudaram:
                ids = [i for i, fs, _, _ in itens if f in fs]
                print(f'    {f}{"  (novo na apostila)" if f not in antigos else ""}')
                print(f'      {", ".join(ids)}')
    print(f'  {len(itens)} trechos ligados ao código, {len(literais)} literais, {len(atuais)} arquivos.'
          + (' Tudo em dia.' if ok else ''))

    if '--gravar' in sys.argv:
        json.dump({'apostila': os.path.basename(html), 'arquivos': dict(sorted(atuais.items()))},
                  open(TRAVA, 'w', encoding='utf-8'), indent=1)
        print('  fontes.lock.json gravado.')


if __name__ == '__main__':
    main()
