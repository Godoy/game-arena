# Arena (tema Convergência) — como continuar

Build: `./build.sh` (edgefade.py, patch18, patch19, patch20; entrada: index-v17.bak.html; saída: index.html para publicar e site/index.html de teste).
Publicado em https://github.com/Godoy/game-arena na pasta v2/ (v2/index.html).
Arte parada: art_final/ (mN criaturas, bN chefes, cN baús, altar, tex*, rock, tree). Animações: anim_final/<chave>.png + .json (h0–h4 heróis, b0–b2 chefes, m1–m8 criaturas).
Meta de cada atlas: fw,fh,cols,ax,ay,h,ifps,a:{idle,walk,atk[,cast]}.
addhero.py / addart.sh leem os blobs de /tmp/claude-tool-results/*/ (imagens trazidas do sandbox do Higgsfield via image_paths).

## Estado em 13/11
- Heróis, chefes e as 8 criaturas animados quadro a quadro (andar e atacar).
- patch20: mistura de quadros vizinhos ao andar (animDraw), respiração das criaturas paradas, esfumado das bordas cortadas nos ataques (edgefade.py marca meta.ef; animPrep aplica ao carregar).
- Interface: em retrato os botões ficam em bloco de 2 colunas à direita (Loja/Talentos, Poção/Picareta, Supremo/Habilidade); Fechar da árvore embaixo à direita (fixo); tocar fora da árvore fecha.
- Conferido: t18.py e shot4.py sem erros, `grep -c __d index.html` = 0.

- patch21 + idle_merge.py: nome "Arena Nexus"; parado em laço para os 5 heróis e 3 chefes (anim_final/<chave>i, vindos de idle_in/); golem m3 refeito com o corpo todo no quadro.
- No sandbox do Higgsfield: idle.py <chave> <url> gera o laço parado; imagens-base dos heróis em /home/user/anim/ref/hN.png.

- Duas versões do MESMO código: `./build.sh` = v2 (arte pintada, publicar em v2/index.html); `LITE=1 ./build.sh` = gráfico simples desenhado por código (publicar na raiz do repositório; cópia em lite/index.html). patch22 tira asas/auréola do desenho por código. A única diferença entre as duas é a arte embutida.

- patch23: visual da versão simples (lajes/grama/terra novas, bordas onduladas com cantos entre terrenos, sombra de bloco mais leve, árvores balançando). O dono e o filho preferem o traço simples da v1; a v2 pintada ficou com cara de 3D antigo.

- patch24: cenário por região na versão simples (pedra: coluna quebrada, cristais, árvore seca; terra: árvore de outono, cogumelo gigante, arbusto), pedras com 3 formatos, beirada do mapa irregular, pedras flutuando no vazio; heróis 7% maiores, poeira ao andar, ícones do menu sem estilhaços.

- patch25: criaturas com vida (respiram, esticam no ataque, recuam ao apanhar, surgem crescendo), estilhaços atrás do Guardião do Núcleo, golpe dos heróis com esticar/encolher, efeitos de corte/cone/anel com mais traço.

- patch26 (mecânica, as duas versões): Tornado do Monge mais forte (dano +33%, raio 120, 6 s, velocidade 78) e Monge sofre 25% menos dano dentro dele; Rajada da Caçadora prende numa rede (flag 3: criaturas 1,2 s, heróis 0,7 s, chefes não; bit 64 em bf) e ela salta 130 para trás; Precisão sem rede, Leque continua com lentidão; Julgamento do Paladino solta da rede.

- patch27: 6º herói, Zero (ideia do filho do dono, inspirado em criatura explosiva verde, desenho próprio de capuz, óculos e pavio). Corpo a corpo fraco (470 de vida, 24 de dano). Mina (5 s, até 3; invisível para inimigos; gatilho 46, explosão 120, 3× o ataque; +6% de dano por inimigo por 8 s, até +30%). TNT Gigante (60 s; 8× o ataque, raio 210, explode 1,4 s após o arremesso). Sem dano próprio nem em aliados. Evoluções: Mina Pesada, Campo Minado. Na v2 ele usa o desenho por código (sem arte pintada).

- DECISÃO (13/11 à noite): foco só na v1 (gráfico simples, `LITE=1 ./build.sh`, raiz do repositório). Não editar nem republicar a v2 por enquanto; o dono tende a ficar só com a v1.
- Ao criar herói novo, lembrar das listas por classe: CLS, SKIN, TAL, EVO e AIMS (mira dos botões), além do ramo em drawHero e do cartão hero<N> no HTML.

- patch28: empurrões/puxões de criaturas (c.kn), puxão de herói (800 px/s) e salto da Caçadora (H.dash, 130 px em 0,22 s) agora deslizam em vez de teleportar; corrigido o recebimento da rede (flag 3) em heróis de outros jogadores.

- patch29: 7ª heroína, Garra, a metamorfa (humana: lança, alcance 200; Bote do Raptor 10 s: vira raptor 6 s e salta, corpo a corpo, +30% andar/atacar, +15% dano; Rugido Alfa 60 s: raptor 8 s, 4× o ataque em 220, lentidão, acelera aliados). Forma no bit 128 de bf; H.rap/H.rapOn. Raptor de desenho próprio (o dono citou a Blue de Jurassic World como inspiração; não copiar a personagem).
- A fonte agora fica no repositório, pasta fonte/ (sem zip): copiar para cá ao retomar. Só a v1 é publicada (raiz).

- patch30: 8º herói, Sentinela (robô blindado; o dono citou RoboCop como inspiração, desenho e nome próprios). 540 de vida, tiro rápido e fraco (16 a cada 0,42 s, alcance 210), o mais lento (172). Raio Perfurante 8 s (4,2× o ataque em linha de 420, lentidão leve). Modo Cerco 60 s (6 s: +80% cadência, +70 alcance, -30% dano sofrido, metade da velocidade). bf 256 = cerco, 512 = escudo.

- patch31: 9º herói, Grude (monstro peludo de braços compridos; inspiração citada: Huggy Wuggy; desenho/nome próprios, tom amigável). 600 de vida, corpo a corpo de alcance 80. Abraço 9 s (puxa e aperta 3×, 1,1× o ataque cada; criaturas presas, heróis presos só no 1º aperto e lentos depois; H.hug). Mordidão 60 s (7× o ataque em cone curto; cura 15% se acertar).
- patch32: progresso entre partidas no aparelho (localStorage 'arena-nexus-meta'): conta com nível, maestria por herói, 3 missões do dia + 1 da semana, baú de fim de partida (moedas, 4 raridades), recordes, 12 conquistas, tela Perfil. Sem punição por faltar (só +50% na 1ª partida do dia). Gancho de teste: window.__end() no site/.
- PRÓXIMA RODADA combinada: loja para gastar moedas (skins/títulos), heróis a desbloquear (sem tirar os que o jogador já usa), desafio do dia com semente fixa, nível da conta ao lado do nome na sala, modo ondas.

- patch33: Zero virou herói de longe e frágil (400 de vida, alcance 200, bombinha com estilhaço de 40% em volta); Grude com braços curvados no abraço (bf 1024; apertos a cada 0,6 s) e efeito 'bite'; loja de visuais no Perfil (Eco 250, Prisma 400: paleta do herói com matiz girado, skinOf); heróis a liberar por 300 moedas (jogador novo começa com 4; quem já tinha save mantém os 9; OLDP); nível da conta na lista da sala (al) e visual equipado enviado na presença (sk).
- Falta da rodada: desafio do dia com semente fixa.

- patch34: puxão em heróis mais firme (janela 0,6 s, aviso 'puxado!', 0,3 s preso ao chegar; no teste de 2 jogadores o Agarre do Sombrio traz o alvo de 200 para 66); ranking final guarda quem saiu (endBoard); pedra quebra com 3 a 5 picaretadas (rkNeed pelo deco do tile); página inicial enxuta (cabeçalho com cartão de perfil, heróis em grade de 5 colunas, nome do jogador abaixo do Jogar). Teste de 2 jogadores: /work/tpull.py (copiado em fonte/ como t_pull.py).

## Ideias ainda não feitas
- Caçadora: companheiro animal domado (ideia do dono, não feita).
- Versão simples: redesenhar criaturas uma a uma; dar o mesmo movimento aos chefes; capa e cabelo dos heróis reagindo mais.
- Conferir no celular se Paladino e Mago de Gelo mudam de tamanho ao parar (escala do parado calculada pela caixa do quadro 0: 0,74 e 0,77).
- Parado dos chefes veio em resolução menor que o atlas principal (refazer com S maior no atlas.py se parecer borrado).
- Parado em laço para as 8 criaturas (hoje só respiração).
- Atlas em resolução maior para telas muito densas (S maior no atlas.py do sandbox; aumenta o arquivo).
- Em paisagem a árvore de talentos ainda rola (já rolava antes).
