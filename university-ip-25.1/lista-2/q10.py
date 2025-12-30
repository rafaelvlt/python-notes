print('Bem amigos da Rede Globo, emoção no ar! Prepare o coração porque hoje é dia de decisão! É final de Copa do Mundo, mas não é futebol… é ping pong, meu amigo! A raquete vai cantar, a bolinha vai voar, e só um será campeão! Segura essa emoção porque vai começar!')

sacador_inicial = input()
sacador_atual = sacador_inicial
if sacador_inicial == 'hugo':
    proximo_sacador = 'lin'
else:
    proximo_sacador = 'hugo'

sets_hugo = 0
sets_lin = 0
set_n = 0

contador_acoes = 0

acao = ''
tiebreak = False
contagem_saques = 0
acabou_jogo = False
dominio_tiebreak = False


#main loop da partida
while not acabou_jogo:
    #entre sets
    set_n += 1
    print(f'Set {set_n}:')
    if tiebreak == True:
        print('Agora é hora da decisão! Vamos para o tie-break, quem errar, perde tudo! É emoção até o fim!')
    set_acabou = False
    
    pontos_hugo = 0
    pontos_lin = 0
    vai_a_dois = False

    #troca de sacador entre sets
    if set_n != 1:
        if sacador_atual == 'hugo':
            sacador_atual = 'lin'
            proximo_sacador = 'hugo'
        else:
            sacador_atual = 'hugo'
            proximo_sacador = 'lin'
    
    if tiebreak == True:
        if sacador_inicial == 'hugo':
            sacador_atual = 'hugo'
            proximo_sacador = 'lin'
        else:
            sacador_atual = 'lin'
            proximo_sacador = 'hugo'

    #codigo entre sets
    while not set_acabou:
        #acoes
        proxima_acao = ''
        acao = ''
        acoes_ponto = input()

        #contadores para condicionais
        contador_acoes = 0
        contador_letras = 0
        tamanho = len(acoes_ponto)

        #troca de sacador tiebreak
        if tiebreak == True:
            if contagem_saques % 2 == 1 and contagem_saques != 0:
                if sacador_atual == 'hugo':
                    sacador_atual = 'lin'
                    proximo_sacador = 'hugo'
                else:
                    sacador_atual = 'hugo'
                    proximo_sacador = 'lin'

        #codigo para partidas
        for char in acoes_ponto:
            dono_ponto = ''
            if char != '-':
                acao += char
                contador_letras += 1

            if char == '-' or contador_letras == tamanho:
                contador_letras += 1
                #descobrir jogador
                if contador_acoes % 2 == 0:
                    oponente = proximo_sacador
                    jogador_atual = sacador_atual    
                else:
                    oponente = sacador_atual
                    jogador_atual = proximo_sacador
                
                #saque
                if acao == 'saque' and contador_acoes == 0:
                    proxima_acao = 'neutra'
                    acao = ''
                elif contador_acoes == 1 and (acao == 'ataque' or acao == 'erro'):
                    dono_ponto = oponente
                    print(f'Uau, um ace! {oponente.capitalize()} solta o braço e deixa o adversário parado!')
                
                #defesa
                elif acao == 'defesa' and (proxima_acao == 'neutra' or proxima_acao == 'defensiva'):
                    proxima_acao = 'ofensiva'
                    acao = ''
                elif acao == 'defesa' and proxima_acao == 'ofensiva':
                    dono_ponto = oponente
                    print(f'{jogador_atual.capitalize()} tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.')
                
                #ataque
                elif acao == 'ataque' and (proxima_acao == 'ofensiva'or proxima_acao == 'neutra'):
                    proxima_acao = 'defensiva'
                    acao = ''
                
                #controle
                elif acao == 'controle' and (proxima_acao == 'neutra' or proxima_acao == 'ofensiva'):
                    proxima_acao = 'neutra'
                
                #erro ou falha
                elif acao == 'erro':
                    dono_ponto = oponente
                    acao = ''
                    proxima_acao = ''
                    print(f'{jogador_atual.capitalize()} se estica, tenta a defesa, mas não alcança — ponto para o adversário.')
                elif acao != 'defesa' and proxima_acao == 'defensiva':
                    dono_ponto = oponente
                    print(f'{oponente.capitalize()} acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!')
                
                else:
                    dono_ponto = oponente
                    print(f'{jogador_atual.capitalize()} se estica, tenta a defesa, mas não alcança — ponto para o adversário.')
                
                #pontuação e passada para próxima acao
                if dono_ponto != '':
                    if dono_ponto == 'hugo':
                        pontos_hugo += 1
                        print(f'Ponto para {dono_ponto.capitalize()}!')
                    if dono_ponto == 'lin':
                        pontos_lin += 1
                        print(f'Ponto para {dono_ponto.capitalize()}!')
                    print(f'Placar do {set_n} set : {pontos_hugo} x {pontos_lin}')
                    if tiebreak == True:
                        contagem_saques += 1
                    if pontos_hugo == 4 and pontos_lin == 4 and tiebreak == False:
                        vai_a_dois = True
                        print('O set está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva — é decisão na mesa!')
                    if pontos_hugo == 6 and pontos_lin == 6 and tiebreak == True:
                        vai_a_dois = True
                        print('O tie-break está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva, é a reta final da disputa! Quem será o grande campeão?')
                else:
                    contador_acoes += 1
                    acao = ''

                #codigo para fim de set
                if tiebreak == False and vai_a_dois == False:
                    if pontos_hugo == 5:
                        sets_hugo += 1
                        vencedor_set = 'hugo'
                        set_acabou = True
                    elif pontos_lin == 5:
                        sets_lin += 1
                        vencedor_set = 'lin'
                        set_acabou = True
                elif vai_a_dois == True and tiebreak == False:
                    if (pontos_hugo - pontos_lin) == 2:
                        sets_hugo += 1
                        vencedor_set = 'hugo'
                        set_acabou = True
                    elif (pontos_lin - pontos_hugo) == 2:
                        sets_lin += 1
                        vencedor_set = 'lin'
                        set_acabou = True
                
                if tiebreak == True:
                    if vai_a_dois == True:
                        if (pontos_hugo - pontos_lin) == 2:
                            sets_hugo += 1
                            vencedor_set = 'hugo'
                            set_acabou = True
                        elif (pontos_lin - pontos_hugo) == 2:
                            sets_lin += 1
                            vencedor_set = 'lin'
                            set_acabou = True
                    elif pontos_hugo == 7 or pontos_lin == 7:
                        if pontos_hugo == 7 and pontos_lin == 0:
                            sets_hugo += 1
                            vencedor_set = 'hugo'
                            set_acabou = True
                            dominio_tiebreak = True
                            print(f'Fim de tie-break! {vencedor_set.capitalize()} arrasa com um 7 a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!')
                        elif pontos_lin == 7 and pontos_hugo == 0:
                            sets_lin += 1
                            vencedor_set = 'lin'
                            set_acabou = True
                            dominio_tiebreak = True
                            print(f'Fim de tie-break! {vencedor_set.capitalize()} arrasa com um 7 a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!')
                        elif pontos_hugo == 7:
                            sets_hugo += 1
                            vencedor_set = 'hugo'
                            set_acabou = True
                        elif pontos_lin == 7:
                            sets_lin += 1
                            vencedor_set = 'lin'
                            set_acabou = True
                
                if set_acabou == True:
                    if pontos_hugo == 5 and pontos_lin == 0 and tiebreak == False:
                        print(f'Fim de set! Domínio total: 5 a 0, sem chance para o adversário — {vencedor_set.capitalize()} passeia na mesa')
                    elif pontos_lin == 5 and pontos_hugo == 0 and tiebreak == False:
                        print(f'Fim de set! Domínio total: 5 a 0, sem chance para o adversário — {vencedor_set.capitalize()} passeia na mesa')
                    else:
                        if dominio_tiebreak == False:
                            print(f'E o set vai para {vencedor_set.capitalize()}!')
                    print(f'Placar do jogo: {sets_hugo} x {sets_lin}')

    #codigo para fim de jogo
    if sets_hugo == 2 and sets_lin == 2:
        tiebreak = True
        contagem_saques = 0
    elif set_n >= 3 and sets_hugo == 3:
        acabou_jogo = True
        vencedor_jogo = 'hugo'
    elif set_n >= 3 and sets_lin == 3:
        acabou_jogo = True
        vencedor_jogo = 'lin'
    elif set_n == 5:
        if sets_hugo > sets_lin:
            acabou_jogo = True
            vencedor_jogo = 'hugo'
        else:
            acabou_jogo = True
            vencedor_jogo = 'lin'

if vencedor_jogo == 'hugo' and tiebreak == False:
    print('Hugo garantiu a vitória sem precisar de tie-break! Uma performance sólida e sem erros, ele dominou o jogo do início ao fim e se sagrou campeão do mundo!')
elif vencedor_jogo == 'hugo' and tiebreak == True:
    print('Hugo é o grande vencedor! Ele conquista o tie-break com uma performance impecável e leva a vitória!')
elif vencedor_jogo == 'lin' and tiebreak == True:
    print('Hugo lutou até o fim, mas no tie-break, o adversário levou a melhor. Uma derrota apertada, mas ainda assim, uma grande batalha!')
elif vencedor_jogo == 'lin' and tiebreak == False:
    print('Hugo não conseguiu segurar a pressão e acabou perdendo sem precisar do tie-break. Foi uma grande final, mas hoje não foi o seu dia. Vitória do chinês!')
