# Do Clique à API: UX de Verdade

Material completo de um minicurso de 3h30 sobre experiência do usuário vista dos dois lados: o que o **frontend** faz, o que a **API** faz e o que só funciona quando os dois trabalham juntos. São 22 temas, cada um mostrado funcionando numa lojinha de verdade, na versão ruim e na versão boa.

Apresentado na XX Semana de Tecnologia da Fatec Ourinhos, em duas turmas (19/10/2026 à tarde e 20/10/2026 à noite), por Adrian Gustavo de Paiva Oliveira e Pedro Ferreira.

**Quer dar um minicurso parecido?** Comece por [COMO-FOI-FEITO.md](COMO-FOI-FEITO.md): o passo a passo do que fizemos, como usamos IA, o que faríamos diferente e um checklist.

## Links rápidos

- **Apostila (PDF, 65 páginas):** [adriangpo.github.io/minicurso-lojinha-ux/03-material/apostila/apostila.pdf](https://adriangpo.github.io/minicurso-lojinha-ux/03-material/apostila/apostila.pdf)
- **Lojinha UX, o código das 22 demos:** [github.com/adriangpo/lojinha-ux](https://github.com/adriangpo/lojinha-ux)
- **Roteiro da aula:** [02-roteiro/roteiro.md](02-roteiro/roteiro.md)

## O que tem aqui

| Pasta | O que tem |
|---|---|
| [`COMO-FOI-FEITO.md`](COMO-FOI-FEITO.md) | O processo, do tema às duas turmas, para quem quer seguir os mesmos passos |
| [`01-ideias/`](01-ideias) | Os 22 temas e o que ficou de fora, as decisões tomadas (e por quê) e as notas técnicas |
| [`02-roteiro/`](02-roteiro) | O roteiro como foi apresentado: ordem, tempo e como demonstrar cada tema |
| [`03-material/`](03-material) | Os slides, a folha do aluno, a apostila (a versão final, v12), o guia de como a apostila é feita e as ferramentas que geram os PDFs |
| `04-apps/` | Não está aqui: é o repositório [lojinha-ux](https://github.com/adriangpo/lojinha-ux). Clone dentro desta pasta se for usar as ferramentas da apostila |

## Os 22 temas

| Bloco | Temas |
|---|---|
| 1. Antes do clique | Formulários e validação · Erros úteis · URL como estado |
| 2. Durante a espera | Estados da tela · Skeleton loading · Layout shift · Debounce e throttle · Race conditions e AbortController · Optimistic UI · Feedback de sucesso · Upload com progresso e tempo real |
| 3. Quando dá errado | Timeouts · Retries e exponential backoff · Clique duplo e idempotência · Rate limiting · Sessão expirada · Offline e conexão instável |
| 4. Rapidez de verdade | Caching · Imagens com signed URL e cache · Lazy loading · N+1 requests · Paginação e infinite scroll |

## Contato

- Adrian Gustavo de Paiva Oliveira: [linkedin.com/in/adriangpo](https://linkedin.com/in/adriangpo) · [github.com/adriangpo](https://github.com/adriangpo)
- Pedro Ferreira: [linkedin.com/in/pedro-ferreira021](https://linkedin.com/in/pedro-ferreira021) · [github.com/PedroFerreira3](https://github.com/PedroFerreira3)
