# Como foi feito

Este é o caminho que fizemos para montar o minicurso **Do Clique à API: UX de Verdade**, do convite até as duas turmas. Escrevemos para quem quer dar um minicurso e não sabe por onde começar. Dá para seguir os mesmos passos com outro tema, e todos os arquivos que usamos estão neste repositório.

Primeiro, a dica mais importante de todas: **faça.** Parece grande, dá frio na barriga, e é exatamente por isso que vale. Montar uma aula obriga você a entender o assunto num nível que só estudar não dá, e no fim você tem um material que é seu. Vai sem medo.

## Em números

- **3h30** de aula, com 20 minutos de intervalo, dada **duas vezes**: 19/10/2026 à tarde e 20/10/2026 à noite, na XX Semana de Tecnologia da Fatec Ourinhos.
- **Até 20 pessoas** por turma, num laboratório.
- **22 temas**, cada um com versão ruim e versão boa funcionando numa aplicação de verdade.
- **Uma lojinha** (React + Node + Postgres + MinIO) com um monitor que mostra as requisições acontecendo.
- **Mais de 17 versões** da folha do aluno, **12 versões** da apostila (65 páginas) e 15 slides.
- **Cerca de 10 dias** entre os primeiros arquivos (09/10) e a primeira turma (19/10).

## A linha do tempo

| Quando | O que aconteceu |
|---|---|
| Antes de tudo | O convite e a ideia: um minicurso sobre UX, e não só sobre design, mas sobre o que o frontend e a API fazem pela experiência de quem usa. |
| 09/10 a 11/10 | Começo da lojinha e escolha da stack. |
| 12/10 | Primeira versão da lojinha no GitHub, com as demos, o monitor e o botão "Ver código". |
| Até 17/10 | Demos refinadas tema por tema. No dia 17, uma rodada de ideias leva a lista de 19 para 22 temas. |
| 18/10 | O dia do material: roteiro fechado, slides só na abertura, folha do aluno (mais de 17 versões), apostila (da amostra de um tema só à versão completa de 65 páginas, 11 versões) e slides. |
| 19/10, manhã | Últimos ajustes nas demos (Pix no clique duplo, long polling, Offline pelo monitor). |
| 19/10, 13h30 | Turma A. |
| 20/10, 19h30 | Turma B. |
| Depois | Correção de um bug que apareceu na aula (cache no tema de signed URL), a v12 da apostila, alinhada com a lojinha, e organização deste repositório. |

## O passo a passo

### 1. Escolha um tema que dê para mostrar

O tema era UX. O recorte que virou o curso foi olhar para UX além do design, para o que o frontend e a API fazem pela experiência de quem usa: "UX não é só design. Metade dela é decidida na API". Isso deu uma frase para abrir e fechar a aula, e um critério para tudo o que viesse depois: **o tema entra se o usuário sente a diferença na tela.**

Escolha um assunto que você consiga **mostrar acontecendo**, e não só explicar. Se der para ver a versão ruim e a boa lado a lado, a aula praticamente se monta sozinha.

### 2. Liste muito, depois corte com critério

Começamos com uma lista grande e cortamos. O que ajudou a cortar:

- **Um critério claro**: só entra o que muda o que a pessoa vê. CORS, CI/CD, testes, segurança e outros ficaram de fora (a lista e o motivo estão em `01-ideias/temas.md`).
- **Uma etiqueta por tema**: Frontend, API ou Frontend + API. Ela organiza a cabeça de quem assiste e prova a ideia central do curso.
- **Uma ordem que conta uma história**: a vida de uma ação do usuário, em 4 blocos (antes do clique, durante a espera, quando dá errado, rapidez de verdade). Cada tema termina puxando o próximo, sempre que dá.
- **Uma lista de corte pronta**: os três temas que saem primeiro se o tempo apertar. Melhor decidir isso em casa do que no improviso.
- **Um backlog**: ideias boas que não cabiam ficaram anotadas. Três delas entraram depois (Timeouts, Offline e Feedback de sucesso), e uma foi cortada de vez.

### 3. Decida o formato antes de produzir qualquer coisa

A decisão que mais mudou o curso: **demonstração acima de slide.** Slides só na abertura (conceitos básicos e os limites de tempo do Nielsen) e no fechamento. Do primeiro tema em diante, tudo acontece na aplicação.

Faça a conta do tempo cedo. 210 minutos, menos 20 de intervalo, 20 de abertura e 10 de fechamento, sobram 160 para 22 temas: uns 7 minutos por tema. Esse número decide quanto cada demo pode ter.

### 4. Construa a demo primeiro, o material depois

A lojinha veio antes de qualquer slide ou apostila, porque tudo o resto descreve o que ela faz. O que funcionou:

- **Uma página por tema, um arquivo por versão.** Nada de `if` misturando a versão ruim e a boa. Na aula, o botão "Ver código" mostra exatamente o arquivo daquela versão.
- **Código curto e correto acima de tudo**, porque ele é explicado linha por linha na frente da turma.
- **Um monitor** em outra aba, que mostra cada requisição saindo do navegador, chegando na API e consultando o banco, como uma aba Network desenhada para a aula. É o que torna visível o que normalmente é invisível.
- **Controles do apresentador no monitor.** Em localhost tudo responde na hora, então nenhum problema de verdade aparece. Por isso o monitor força o mundo real: latência, taxa de erro, API travada, sessão expirada, sem conexão. A lojinha fica limpa, sem botões de aula.
- **Testar cada demo no navegador, clicando de verdade.** Não basta o código compilar: a demo tem que mostrar o problema de um jeito que a turma veja.

O código está em [github.com/adriangpo/lojinha-ux](https://github.com/adriangpo/lojinha-ux).

### 5. Escreva as decisões

Desde o começo, tudo o que era decidido ia para `01-ideias/decisoes.md`, com o porquê. Parece burocracia, mas é o que permite trabalhar rápido sem andar em círculo: antes de rediscutir algo, confere lá. Junto dele, `notas-tecnicas.md` guardou as explicações dos temas mais delicados, para responder perguntas da turma com segurança.

Isso fica ainda mais importante trabalhando com IA (passo 9).

### 6. Monte o roteiro com tempo por tema

O roteiro (`02-roteiro/roteiro.md`) tem, para cada tema: o problema, a solução, como fazer a demo e quanto tempo usar. E um ritmo fixo que se repete nos 22 temas: **mostrar o problema → explicar com o monitor e o código → mostrar a versão corrigida.** Com o ritmo fixo, a turma sabe o que esperar e os apresentadores não se perdem.

Coloque também os momentos de participação. O nosso foi o debate do botão desabilitado: a turma vê duas versões, vota se o botão deve ficar desabilitado ou não, defende o voto, e só então vê a terceira versão, que junta os dois lados.

### 7. Faça o material, uma peça de cada vez

**A folha do aluno** (`03-material/folha/`): uma A4 com o mapa dos 22 temas, linhas para anotar e QR codes para a apostila, a lojinha e este repositório. Foram mais de 17 versões até a final. Construir é iterar e melhorar aos poucos.

**A apostila** (`03-material/apostila/`), para quem assistiu e quem não assistiu. O caminho dela é o melhor exemplo de como o processo funciona:

1. **Amostra antes do todo.** A v1 tinha um tema só (Race conditions), em três estilos de figura, para escolher o estilo antes de fazer 22 temas.
2. **Direções lado a lado.** A v2 trouxe três direções de design. Nenhuma agradou, e isso também é resposta: ficou claro o que não queríamos.
3. **Referências reais em vez de descrever gosto.** A v3 partiu de livros técnicos em PDF (Eloquent JavaScript, Think Python, handouts no estilo Tufte) e tirou deles o que tinham em comum: texto corrido, seções numeradas, notas na margem, figuras com legenda.
4. **Um tema completo para aprovar** (v4 e v5) e a capa em opções (v6 e v7).
5. **As regras escritas num documento só**, o `ESTRUTURA.md`: medidas, cores, fontes, a ordem das seções de cada tema, como desenhar as figuras. A partir daí, cada tema novo seguiu as mesmas regras.
6. **A versão completa** (v8, 62 páginas) e **rodadas de feedback**: os ajustes eram anotados num arquivo e entravam todos juntos na versão seguinte (v9, v10, v11), em vez de uma versão por ajuste.
7. **Ligação com o código.** Cada trecho da apostila aponta para o arquivo da lojinha de onde saiu, e um script avisa quando o código mudou depois que a apostila foi gerada.

8. **A lojinha como fonte da verdade.** Depois das turmas, a v12 alinhou a apostila com o que a lojinha faz de verdade e tirou tudo o que a lojinha não tem.

Neste repositório fica só a versão final, a v12.

**Os slides** (`03-material/slides/`) vieram por último, quando já estava claro o que a demo não conseguia mostrar sozinha: 15 slides, no mesmo estilo da apostila, em PDF para abrir igual em qualquer notebook.

### 8. Prepare a dupla

Não fizemos um ensaio cronometrado do roteiro. O que fizemos foi uma passada pela lojinha inteira, página por página:

- o que falar em cada tema;
- que experiência real cada um tinha para contar ali ("já aconteceu comigo…" prende mais que qualquer definição);
- quem conduz cada página.

Dividir os temas deixou a aula com duas vozes e deu tempo para um preparar a próxima demo enquanto o outro falava. Se você vai apresentar em dupla, combinem também como passar a palavra de um para o outro.

### 9. Use IA, mas itere muito

Tudo neste repositório e na lojinha foi construído com o **Claude Code**: as demos, o monitor, a apostila, a folha, os slides e os scripts. Mas nada saiu de primeira. **"One-shot prompt" não existe**: foram mais de 17 versões da folha, 12 da apostila e muitas rodadas em cada demo até chegar no que queríamos.

O que fez a diferença:

- **Arquivos de contexto.** `decisoes.md`, `temas.md`, `roteiro.md` e `ESTRUTURA.md` eram lidos no começo de cada sessão. Sem isso, a IA rediscute o que já foi decidido e desfaz escolhas antigas.
- **Pedir amostra antes do todo.** Um tema antes da apostila inteira, três opções de capa antes de escolher uma.
- **Mostrar referências em vez de descrever gosto.** "Quero parecido com estes livros" funciona muito melhor que "quero bonito e profissional".
- **Feedback em rodadas**, anotado num arquivo, aplicado de uma vez numa versão nova.
- **Nunca sobrescrever uma versão.** Toda mudança vira um arquivo novo (`v9`, `v10`…). Dá para comparar, voltar atrás e ver o caminho.
- **Conferir de verdade.** Abrir a demo no navegador e clicar. Converter o PDF em imagens e olhar página por página. Ter scripts que avisam quando algo saiu do lugar.
- **O gosto é seu.** Em algumas versões, o resultado ficou "com cara de IA" (a combinação de fonte e cor que todo material gerado parece ter). Quem percebe isso e diz "não" é você. A IA acelera, mas quem decide o que fica bom é quem vai estar na frente da turma.

### 10. No dia

- Chegue cedo e teste **na tela da sala**, não só no seu monitor. O que é legível no notebook pode não ser na TV.
- Teste as demos **com o navegador "sujo"**, do jeito que ele vai estar na aula: depois de um ensaio, com cache, com abas abertas. O único bug que apareceu na aula foi esse: no tema de signed URL, as fotos já estavam no cache por causa de visitas anteriores, e trocar de versão não mostrava a diferença. Tínhamos que dar F5 toda hora. A correção (um botão no monitor que recomeça a demonstração) entrou depois.
- Tenha um jeito de **zerar tudo** entre um tema e outro. No nosso caso, o "Zerar" dos controles, que volta latência, erros e conexão ao normal.

## Se fôssemos fazer de novo

- **Congelar o código antes do material.** Mudamos demos na manhã da primeira turma, e a apostila ficou para trás (o tema 14 falava de uma compra; a demo tinha virado um Pix). Só a v12, depois das turmas, acertou isso. Teria sido melhor fechar o código um dia antes.
- **Começar o material impresso antes.** Folha, apostila e slides saíram todos num dia só. Deu certo, mas foi corrido.
- **Guardar a fonte de tudo.** As versões antigas da folha foram apagadas no caminho e, com elas, o HTML da versão final. Hoje temos só o PDF. Guarde a fonte junto do resultado.
- **Testar as demos como a turma vai ver**, com cache e estado de verdade, e não só com tudo zerado.

## Dicas para quem vai dar um minicurso

- **Faça.** Essa é a principal. Você aprende muito mais montando a aula do que assistindo a uma.
- **Vai sem medo.** Ninguém na sala espera perfeição. Espera alguém que goste do assunto e mostre algo de verdade.
- **Comece pelo que você já viveu.** As histórias reais ("já aconteceu comigo…") são o que a turma lembra depois.
- **Mostre, não só fale.** Se dá para ver o problema acontecendo, mostre.
- **Faça em dupla, se puder.** Dividir a aula alivia a pressão e deixa o ritmo melhor.
- **Escreva as decisões.** Você vai agradecer a si mesmo na terceira vez que alguém (ou a IA) perguntar "por que ficou assim?".
- **Publique tudo depois.** O material que você fez pode ser o ponto de partida de outra pessoa, como este repositório.

## Checklist para o seu minicurso

- [ ] Tema escolhido, com uma frase que resume a ideia do curso
- [ ] Lista de temas cortada, com etiquetas e uma ordem que conta uma história
- [ ] Lista do que sai primeiro se faltar tempo
- [ ] Formato decidido (quanto de slide, quanto de demo) e conta de tempo por tema
- [ ] Demos funcionando, testadas no navegador
- [ ] `decisoes.md` em dia
- [ ] Roteiro com tempo por tema e momentos de participação
- [ ] Folha do aluno, apostila e slides
- [ ] Passada completa com quem vai apresentar junto, com os temas divididos
- [ ] Teste na sala, na tela de verdade
- [ ] Material publicado

## Como reaproveitar este repositório

- **Para dar este mesmo curso:** siga `02-roteiro/roteiro.md`, rode a [lojinha](https://github.com/adriangpo/lojinha-ux) e use os slides, a folha e a apostila de `03-material/`.
- **Para fazer outro curso:** copie a estrutura (`01-ideias`, `02-roteiro`, `03-material`) e os arquivos de decisão. O `03-material/apostila/ESTRUTURA.md` serve de modelo para escrever as regras da sua apostila, e `03-material/ferramentas/` gera PDFs a partir de HTML, com QR codes e sumário com número de página.
