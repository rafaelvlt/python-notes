#inputs para nomes de jogadores e setup importante
jogador_1 = input()
jogador_2 = input()
#caso ambos jogadores sejam lendários, printa o output desejado
if jogador_1 == 'Luis' or jogador_1 == 'Lavoisier' or jogador_1 == 'Joab' or jogador_1 == 'Renan':
    if jogador_2 == 'Luis' or jogador_2 == 'Lavoisier' or jogador_2 == 'Joab' or jogador_2 == 'Renan':
        print('Essa partida vai ser épica! O jogo vai ser emocionante!')

num_sets = int(input())
 
nivel_disputa = input()
if nivel_disputa == 'aprendizes':
    max_rebatidas = 1
elif nivel_disputa == 'básicos':
    max_rebatidas = 2
elif nivel_disputa == 'amostradinhos':
    max_rebatidas = 3

#contadores necessários para o funcionamento da partida
sets_jog1 = 0
sets_jog2 = 0

#loop principal de sets, quando o loop acabar, o jogo acaba
for n in range(0, num_sets):
    print(f'Iniciando o {n+1}º set')
    
    #flags e contadores que precisam ser atualizados entre sets
    terminar_set = False #flag para termino de set, evita usar break
    sacador = jogador_1
    adversario = jogador_2
    pontos_jog1 = 0
    pontos_jog2 = 0
    
    while not terminar_set: #loop de partida
        terminar_partida = False
        rebatidas = 0
        acao_inicial = input() #acao_inciial fora do loop funciona melhor, devido a só ser atualizada em caso de saque perfeito
        while not terminar_partida:
            if acao_inicial == 'saque':
                #para acao inicial da partida
                print(f'O saque é de {sacador}')
                quicou1 = input()
                quicou2 = input()
                #em qualquer input, se há rede o ponto é para o adversário
                if quicou1 == 'REDE' or quicou2 == 'REDE':
                    print('Vish, ainda bateu na rede')
                    if sacador == jogador_1:
                        pontos_jog2 += 1
                        sacador = jogador_2
                        adversario = jogador_1
                        terminar_partida = True
                    else:
                        pontos_jog1 += 1
                        sacador = jogador_1
                        adversario = jogador_2
                        terminar_partida = True
                        
                #saque perfeito, pega input de rebatida para não ter que fazer whie loop em caso de acao_inicial = rebatida
                elif quicou1 == 'SA':
                    if quicou2 == 'AO':
                        print('Um saque PERFEITO!!')
                        acao_inicial = input()
                    elif quicou2 == 'SA':
                        print(f'{sacador}, a bola quicou duas vezes na sua própria área! Que saque feio foi esse??')
                        if sacador == jogador_1:
                            pontos_jog2 += 1
                            sacador = jogador_2
                            adversario = jogador_1
                            terminar_partida = True
                        else:
                            pontos_jog1 += 1
                            sacador = jogador_1
                            adversario = jogador_2
                            terminar_partida = True
                #provavelmente dava pra fazer um or com abos quicou e daria certo, mas fica ai mais verbose
                elif quicou1 == 'AO':
                        if quicou2 == 'AO':
                            print(f'Boa, {sacador}! Deu ponto de graça pro oponente!! Agora quem saca é {adversario}')
                            if sacador == jogador_1:
                                pontos_jog2 += 1
                                sacador = jogador_2
                                adversario = jogador_1
                                terminar_partida = True
                            else:
                                pontos_jog1 += 1
                                sacador = jogador_1
                                adversario = jogador_2
                                terminar_partida = True
            #em caso de saque perfeito, a acao_inicial não muda para rebatida, e o while da partida volta para cá até ter um ponto
            if acao_inicial == 'rebatida':
                acao_valida = input() #acao de partida
                if acao_valida == 'oponente rebateu': #apenas incrementa rebatidas, até atingir a máxima, onde pega inputs de velocidade
                    rebatidas += 1
                    if rebatidas == max_rebatidas:
                        velocidade1 = int(input())
                        velocidade2 = int(input())
                        if velocidade1 < velocidade2:
                            pontos_jog1 += 1
                            sacador = jogador_1
                            adversario = jogador_2
                            terminar_partida = True
                        elif velocidade2 < velocidade1:
                            pontos_jog2 += 1
                            sacador = jogador_2
                            adversario = jogador_1
                            terminar_partida = True
                else:
                    #caso algum dos jogadores deixar a bola cair, o ponto vai para o oponente
                    if acao_valida == (jogador_1 + ' deixou a bola cair'):
                        pontos_jog2 += 1
                        sacador = jogador_2
                        adversario = jogador_1
                        terminar_partida = True
                    elif acao_valida == (jogador_2 + ' deixou a bola cair'):
                        pontos_jog1 += 1
                        sacador = jogador_1
                        adversario = jogador_2
                        terminar_partida = True

             #condição de vitória, diferença de 2 pontos e mais que 3 pontos no set
            if (pontos_jog1 - pontos_jog2) >= 2 and (pontos_jog1 >= 3):
                sets_jog1 += 1
                terminar_set = True
                terminar_partida = True
            elif (pontos_jog2 - pontos_jog1) >= 2 and (pontos_jog2 >= 3):
                sets_jog2 += 1
                terminar_set = True
                terminar_partida = True

#fim do jogo, compara quantidade de sets e printa o relatorio final
if sets_jog1 > sets_jog2:
    vencedor = jogador_1
else:
    vencedor = jogador_2
print(f"Depois de {num_sets} set(s) vibrante(s), o grande vencedor é {vencedor}!!")
print("Fim do jogo!")
