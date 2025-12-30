#atributos ataque e defesa
print('------- Início do Treino -------')

ataque = 0
defesa = 0
erros = 0
quantidade_bolas = int(input())

for i in range(0, quantidade_bolas):
    errou = False
    bola_lançada = input()
    golpe_executado = input()
    if bola_lançada == 'Defesa':
        if golpe_executado == 'Push':
            defesa += 5
        elif golpe_executado == 'Chop':
            defesa += 10
        elif golpe_executado == 'Errou':
            errou = True
            erros += 1
            defesa -= 10
    if bola_lançada == 'Ataque':
        if golpe_executado == 'Topspin':
            ataque += 5
        elif golpe_executado == 'Smash':
            ataque += 10
        elif golpe_executado == 'Errou':
            errou = True
            erros += 1
            ataque -= 10
    if errou == False:
        print(f'Você conseguiu rebater uma bola de {bola_lançada}! Golpe executado: {golpe_executado}.')
    else:
        print('Você errou! Levanta a cabeça que ainda tem mais.')
if ataque < 0:
    ataque = 0
if defesa < 0:
    defesa = 0
if ataque > defesa:
    print('Ter um bom jogo ofensivo será fundamental para ganhar o InterCin!')
elif defesa > ataque:
    print('Defesa ganha campeonatos! Agora sim estou preparado.')
elif ataque == defesa:
    print('Foi um treino equilibrado.')

if erros > 0:
    print('Infelizmente não foi um treino perfeito, mas pude melhorar muito.')
#relatorio final
print('------- Atributos -------')
print(f'Ataque: {ataque}\nDefesa: {defesa}')

