numero_rodadas = int(input())
print('Vamos dar início à disputa!!! TOMADA!!!')

vencedor_tomada = input()
if vencedor_tomada == "Jaob":
    print('Jaob veio de Catende e está pronto para vencer!!!')
elif vencedor_tomada == "Luvusier":
    print('Nada se cria, tudo se transforma, então Luvusier irá se transformar em um vencedor!!!')


jogador = vencedor_tomada
pontos_jaob = 0
pontos_luv = 0
terminar_partida = False
contador = 1
vencedor = ''
venceu_baralho = ''
while contador <= numero_rodadas and terminar_partida == False:

    print(f'COMEÇA A {contador}ª RODADA!')
    objeto_acertado = input()
    print(f'{jogador} jogou a bolinha no(a) {objeto_acertado}!')
    while objeto_acertado == 'mesa':
        #troca de jogador
        if jogador == 'Jaob':
            jogador = 'Luvusier'
        else:
            jogador = 'Jaob'
        objeto_acertado = input()
        print(f'{jogador} jogou a bolinha no(a) {objeto_acertado}!')

    #adicionou pontos
    if objeto_acertado == 'Baralho de UNO' or objeto_acertado == 'Armário de Homero e Elena' or objeto_acertado == 'Peça de Dominó' or objeto_acertado == 'Baralho de Coup Desaparecido':
        if jogador == 'Jaob':
            vencedor = 'Jaob'
            if objeto_acertado == 'Baralho de UNO':
                pontos_jaob += 2
            elif objeto_acertado == 'Armário de Homero e Elena':
                pontos_jaob += 3
            elif objeto_acertado == 'Peça de Dominó':
                pontos_jaob += 3
            elif objeto_acertado == 'Baralho de Coup Desaparecido':
                pontos_jaob += 100
                terminar_partida = True
                venceu_baralho = 'Jaob'
            print(f'{jogador} teve uma grande pontaria e acertou {objeto_acertado}! Agora está com {pontos_jaob} pontos.')
            if venceu_baralho == 'Jaob':
                print(f'{jogador} achou o Coup!!! Ele merece a vitória sem dúvidas!')

        elif jogador == 'Luvusier':
            vencedor = 'Luvusier'
            if objeto_acertado == 'Baralho de UNO':
                pontos_luv += 2
            elif objeto_acertado == 'Armário de Homero e Elena':
                pontos_luv += 3
            elif objeto_acertado == 'Peça de Dominó':
                pontos_luv += 3
            elif objeto_acertado == 'Baralho de Coup Desaparecido':
                pontos_luv += 100
                terminar_partida = True
                venceu_baralho = 'Luvusier'
            print(f'{jogador} teve uma grande pontaria e acertou {objeto_acertado}! Agora está com {pontos_luv} pontos.')
            if venceu_baralho == 'Luvusier':
                print(f'{jogador} achou o Coup!!! Ele merece a vitória sem dúvidas!')
    #tirou pontos
    elif objeto_acertado == 'Projetor' or objeto_acertado == 'Computador' or objeto_acertado == 'Cabeça do Amiguinho' or objeto_acertado == 'Nada':
        if jogador == 'Jaob':
            vencedor = 'Luvusier'
            if objeto_acertado == 'Projetor':
                pontos_jaob -= 2
            elif objeto_acertado == 'Computador':
                pontos_jaob -= 3
            elif objeto_acertado == 'Cabeça do Amiguinho':
                pontos_jaob -= 5
            elif objeto_acertado == 'Nada':
                pontos_jaob -= 1

            #checa para ver se pontos estão negativos
            if pontos_jaob < 0:
                pontos_jaob = 0
            print(f'{jogador} teve mãos de alface e acertou o(a) {objeto_acertado}. Agora está com {pontos_jaob} pontos.')

        elif jogador == 'Luvusier':
            vencedor = 'Jaob'
            if objeto_acertado == 'Projetor':
                pontos_luv -= 2
            elif objeto_acertado == 'Computador':
                pontos_luv -= 3
            elif objeto_acertado == 'Cabeça do Amiguinho':
                pontos_luv -= 5
            elif objeto_acertado == 'Nada':
                pontos_luv -= 1

            #checa para ver se pontos estão negativos
            if pontos_luv < 0:
                pontos_luv = 0
            print(f'{jogador} teve mãos de alface e acertou o(a) {objeto_acertado}. Agora está com {pontos_luv} pontos.')

    #troca de jogador
    jogador = vencedor
    contador += 1

#resultados
print('\nTEMOS O RESULTADO DA PARTIDA!')
if terminar_partida == False:
    if pontos_jaob > pontos_luv:
        print(f'Jaob deu orgulho à Catende e ganhou a disputa com {pontos_jaob} pontos!')
    elif pontos_luv > pontos_jaob:
        print(f'A química está em festa, Luvusier ganha a disputa com {pontos_luv} pontos!')
    else:
        print('Jaob usou a sua autoridade como monitor-chefe e ganhou a disputa mesmo com o empate!')
else:
    if venceu_baralho == 'Jaob':
        print(f'Jaob deu orgulho à Catende e ganhou a disputa com {pontos_jaob} pontos!')
    elif venceu_baralho == 'Luvusier':
        print(f'A química está em festa, Luvusier ganha a disputa com {pontos_luv} pontos!')

