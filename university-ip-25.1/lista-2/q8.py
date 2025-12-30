print('A partida de revanche de Hugo Calderano contra a China, Potência Mundial do Tênis de Mesa, está prestes a começar!')

nacionalidade_atleta = input()
nome_atleta = input()
while nacionalidade_atleta != 'Chinês':
    print(f'O {nome_atleta} não poderá disputar a partida, pois sua nacionalidade não é chinesa!')
    nacionalidade_atleta = input()
    nome_atleta = input()
print(f'{nome_atleta} foi convocado para vingar o massacre feito durante o mundial de Tênis de Mesa!')

pontos_hugo = 0
pontos_adv = 0
empate = False

ponto_extra = False
while not (pontos_hugo - pontos_adv) >= abs(3):
    numero_adversario = int(input())
    numero_hugo = int(input())
    ponto_extra = False

    #checar o maior
    if numero_hugo > numero_adversario:
        maior = 'Hugo'
    elif numero_hugo < numero_adversario:
        maior = nome_atleta
    else:
        maior = 'Empate'
        empate = True

    #pontos
    if maior == 'Hugo':
        pontos_hugo += 1
        if numero_hugo >= (numero_adversario * 2):
            pontos_hugo += 1
            ponto_extra = True
        if ponto_extra == True:
            print('Que bela jogada, essa merece ponto extra!')
        else:
            print('Hugo Calderano marcou um ponto de maneira esplendida!')
    elif maior == nome_atleta:
        pontos_adv += 1
        if numero_adversario >= (numero_hugo * 2):
            pontos_adv += 1
            ponto_extra = True
        if ponto_extra == True:
            print('Que bela jogada, essa merece ponto extra!')
        else:
            print('Vamos Hugo, não deixe ele vencer!')  
    elif maior == 'Empate':
        pontos_hugo += 1
        print('A bola bateu na rede e felizmente caiu no lado adversário!!! Hugo marca mais um ponto!')

#fim da partida
if pontos_hugo == 3:
    print('Hugo Calderano mostrou o porquê ele é o atual campeão mundial, uma partida relâmpago!')
elif pontos_hugo > 3 and pontos_hugo <= 10:
    print('Não demorou muito, mas o resultado era esperado, Hugo Calderano vence!')
elif pontos_hugo > 10:
    print('Demorou, mas o previsto aconteceu! Hugo Calderano não deixa dúvidas do porquê ele é o Campeão Mundial!')

print(f'Placar Final: {pontos_hugo}x{pontos_adv}\n')

#maquete
print('Aqui está o merecido prêmio de Hugo Calderano:')
comprimento = pontos_adv
largura = pontos_hugo
if comprimento % 2 == 0:
    comprimento -= 1
if comprimento <= 2:
    comprimento = 3
#comprimento sempre tem 2 espaços reservados para bases(larguras)
for i in range(0, largura):
    print('-', end='')
else:
    print('')
for i in range(0, comprimento-2):
    for j in range(0, largura): 
        if j == 0 or j == (largura-1):
            print('|', end='')
        elif i == ((comprimento // 2 + 1) - 2):
            print('#', end='')
        else:
            print(' ', end='')
    print('')
for i in range(0, largura):
    print('-', end='')

