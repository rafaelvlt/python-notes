#convenção de index, 0 = yu, 1 = itd, 2 = suk, aplicavel a todas listas que tenham info de todos
vidas = [50, 50, 100]
output_sukuna = 25

#listas fixas
tecnicas = ['Santuário', 'Fala amaldiçoada', 'Manipulação do céu', 'Clarividência', 'Barreira inviolável']
tecnicas_dano = [75, 0, 50, 25, 25]
tecnicas_range = [1, 9999999999, 2, 1, 3]
movimentacao = ['Cima', 'Baixo', 'Esquerda', 'Direita']
#tecnicas
tecnicas_usadas = input()
tecnicas_usadas = tecnicas_usadas[54:].strip().split(', ')


#pega ordem da matriz e qtd katanas
matriz_katanas = input()
matriz_katanas = matriz_katanas.split()
matriz_katanas = [int(elem) for elem in matriz_katanas]

#pega coordenadas de personagens e katanas, divide em cada matriz
coordenadas_perso = []
coordenadas_katanas = []
for entrada in range(0, matriz_katanas[1]+3):
    coords = input()
    coords = coords.split('x')
    coords = [int(coord) for coord in coords]
    coords.reverse()
    if entrada < 3:
        coordenadas_perso.append(coords)
    else:
        coordenadas_katanas.append(coords)

#listas para katanas
katana_atual = ''
katanas_conhecidas_nome = []
katanas_conhecidas_coords = []

#game vars
jogo_terminou = False
contagem_turnos = 1
ignorar_sukuna = False
yuta_imunidade = 0

print('Yuta: Expansão de domínio - Puro Amor Mútuo')
while not jogo_terminou:
    acao = input()
    matriz_impressa = False
    #TURNOS DO YUTA
    if contagem_turnos == 1:
        #codigo da TAR
        if acao == "Técnica amaldiçoada reversa":
            distancia = max(abs(coordenadas_perso[0][0] - coordenadas_perso[2][0]), abs(coordenadas_perso[0][1] - coordenadas_perso[2][1]))
            if distancia >= 3:
                vidas[0] += 25
                if vidas[0] > 50:
                    vidas[0] = 50

        #movimentação
        if acao in movimentacao:
            if acao == 'Cima':
                nova_linha = coordenadas_perso[0][0] - 1
                if nova_linha >= 0:
                    coordenadas_perso[0][0] = nova_linha
            if acao == 'Baixo':
                nova_linha = coordenadas_perso[0][0] + 1
                if nova_linha < matriz_katanas[0]:
                    coordenadas_perso[0][0] = nova_linha
            if acao == 'Direita':
                nova_coluna = coordenadas_perso[0][1] + 1
                if nova_coluna < matriz_katanas[0]:
                    coordenadas_perso[0][1] = nova_coluna
            if acao == 'Esquerda':
                nova_coluna = coordenadas_perso[0][1] - 1
                if nova_coluna >= 0:
                    coordenadas_perso[0][1] = nova_coluna

            #checa se está em uma katana, se sim roda a lógica baseada no estado do yuta
            if coordenadas_perso[0] in coordenadas_katanas:
                    if katana_atual == '': #caso yuta não esteja segurando uma katana
                        if coordenadas_perso[0] in katanas_conhecidas_coords:
                            katana_atual = katanas_conhecidas_nome[katanas_conhecidas_coords.index(coordenadas_perso[0])]
                        else:
                            katana_atual = input()
                        if katana_atual == 'Santuário':
                            print('Yuta: Até mesmo o Sukuna vai ser pego desprevinido por uma técnica que ainda não me viu usar, então como certeza aquela... É essa aqui!')
                        if not coordenadas_perso[0] in katanas_conhecidas_coords:
                            coord_kat = coordenadas_perso[0].copy() #feito pq tava dando erro de ponteiro
                            katanas_conhecidas_coords.append(coord_kat)
                            katanas_conhecidas_nome.append(katana_atual)
                        coordenadas_katanas.remove(coordenadas_perso[0])
                    else: #caso yuta já tenha katana
                        if not coordenadas_perso[0] in katanas_conhecidas_coords:
                            tecnica_katana = input()
                        else:
                            index_conhecida = katanas_conhecidas_coords.index(coordenadas_perso[0])
                            tecnica_katana = katanas_conhecidas_nome[index_conhecida]
                        #se a katana do yuta for de tecnica mais forte, pega ela
                        if tecnicas_usadas.index(tecnica_katana) < tecnicas_usadas.index(katana_atual):
                            katana_antiga = katana_atual
                            katana_atual = tecnica_katana
                            if katana_atual == 'Santuário':
                                print('Yuta: Até mesmo o Sukuna vai ser pego desprevinido por uma técnica que ainda não me viu usar, então como certeza aquela... É essa aqui!')
                            if not coordenadas_perso[0] in katanas_conhecidas_coords: #se a katana n tiver na lista de conhecidas
                                coord_kat = coordenadas_perso[0].copy() #feito pq tava dando erro de ponteiro
                                katanas_conhecidas_coords.append(coord_kat)
                                katanas_conhecidas_nome.append(katana_antiga)
                            else:
                                index_conhecida = katanas_conhecidas_coords.index(coordenadas_perso[0])
                                katanas_conhecidas_nome[index_conhecida] = katana_antiga
                            
                        else: #se não, deixa ela lá
                            if not coordenadas_perso[0] in katanas_conhecidas_coords: #se a katana n tiver na lista de conhecidas
                                coord_kat = coordenadas_perso[0].copy() #feito pq tava dando erro de ponteiro
                                katanas_conhecidas_coords.append(coord_kat)
                                katanas_conhecidas_nome.append(tecnica_katana)
        #ATAQUE
        elif acao == "Atacar":
            #caso yuta tiver alguma katana, ele ataca com ela
            if katana_atual != '':
                index_tecnica = tecnicas.index(katana_atual)
                dano = tecnicas_dano[index_tecnica]
                alcance = tecnicas_range[index_tecnica]
                #katanas especiais
                if katana_atual == 'Fala amaldiçoada':
                    ignorar_sukuna = True
                elif katana_atual == 'Clarividência':
                    yuta_imunidade = 4
                #pega qual maior entre a distancia do yuta e sukuna em y ou x
                distancia = max(abs(coordenadas_perso[0][0] - coordenadas_perso[2][0]), abs(coordenadas_perso[0][1] - coordenadas_perso[2][1]))
                if distancia <= alcance:
                    vidas[2] -= dano
                    #katanas especiais
                    if katana_atual == 'Manipulação do céu':
                        print('Yuta: Fragmento de gelo fino')
                    elif katana_atual == 'Santuário':
                        print('Yuta: Ruptura\nSukuna: Essa é... A minha técnica!?')
                    elif katana_atual == 'Fala amaldiçoada':
                        print('Yuta: NÃO SE MOVA!')

                    katana_atual = ''
                    #coloca nova katana no mapa
                    nova_katana = input()
                    nova_katana = nova_katana.split('x')
                    nova_katana = [int(coordenada) for coordenada in nova_katana]
                    nova_katana.reverse()
                    #caso já haja uma katana na coordenada da nova katana ela é removida
                    if nova_katana in katanas_conhecidas_coords:
                        index_katana = katanas_conhecidas_coords.index(nova_katana)
                        katanas_conhecidas_coords.pop(index_katana)
                        katanas_conhecidas_nome.pop(index_katana)
                        coordenadas_katanas.append(nova_katana)
                    else:
                        coordenadas_katanas.append(nova_katana)
                        
            else:
                dano = 25
                alcance = 1
                distancia = max(abs(coordenadas_perso[0][0] - coordenadas_perso[2][0]), abs(coordenadas_perso[0][1] - coordenadas_perso[2][1]))
                if distancia <= alcance or alcance == 'inf':
                    vidas[2] -= dano
                    katana_atual = ''

    #TURNOS DO ITADORI
    elif contagem_turnos == 3:
        #codigo da TAR
        if acao == "Técnica amaldiçoada reversa":
            distancia = max(abs(coordenadas_perso[1][0] - coordenadas_perso[2][0]), abs(coordenadas_perso[1][1] - coordenadas_perso[2][1]))
            if distancia >= 3:
                if vidas[1] == 0:
                    print('Itadori: Essa é a última chance de derrotar o Sukuna e recuperar o Fushiguro aqui e agora! Não vacile! Cure-se! cure-se! Cure-se! Cure-se!')
                vidas[1] += 25
                if vidas[1] > 50:
                    vidas[1] = 50
        #caso vida for diferente de 0
        if vidas[1] != 0:
            #movimentação
            if acao == 'Cima':
                nova_linha = coordenadas_perso[1][0] - 1
                if nova_linha >= 0:
                    coordenadas_perso[1][0] = nova_linha
            elif acao == 'Baixo':
                nova_linha = coordenadas_perso[1][0] + 1
                if nova_linha < matriz_katanas[0]:
                    coordenadas_perso[1][0] = nova_linha
            elif acao == 'Direita':
                nova_coluna = coordenadas_perso[1][1] + 1
                if nova_coluna < matriz_katanas[0]:
                    coordenadas_perso[1][1] = nova_coluna
            elif acao == 'Esquerda':
                nova_coluna = coordenadas_perso[1][1] - 1
                if nova_coluna >= 0:
                    coordenadas_perso[1][1] = nova_coluna
            
            elif acao == "Atacar":
                dano = 25
                alcance = 1
                distancia = max(abs(coordenadas_perso[1][0] - coordenadas_perso[2][0]), abs(coordenadas_perso[1][1] - coordenadas_perso[2][1]))
                if distancia <= alcance:
                    vidas[2] -= 25
                    output_sukuna -= 10
                    if output_sukuna < 0:
                        output_sukuna = 0
    #TURNOS SUKUNA
    if contagem_turnos == 2 or contagem_turnos == 4:
        if yuta_imunidade > 0:
            yuta_imunidade -= 1
        if ignorar_sukuna:
            ignorar_sukuna = False
        else:
            if acao == "Técnica amaldiçoada reversa":
                ignorar_sukuna == ignorar_sukuna ##faz nada
            else:
                #movimentação
                if acao == 'Cima':
                    nova_linha = coordenadas_perso[2][0] - 1
                    if nova_linha >= 0:
                        coordenadas_perso[2][0] = nova_linha
                elif acao == 'Baixo':
                    nova_linha = coordenadas_perso[2][0] + 1
                    if nova_linha < matriz_katanas[0]:
                        coordenadas_perso[2][0] = nova_linha
                elif acao == 'Direita':
                    nova_coluna = coordenadas_perso[2][1] + 1
                    if nova_coluna < matriz_katanas[0]:
                        coordenadas_perso[2][1] = nova_coluna
                elif acao == 'Esquerda':
                    nova_coluna = coordenadas_perso[2][1] - 1
                    if nova_coluna >= 0:
                        coordenadas_perso[2][1] = nova_coluna

                #ataque
                elif acao == "Atacar":
                    #escolhe quem vai atacar
                    distancia_ate_yuta = max(abs(coordenadas_perso[0][0] - coordenadas_perso[2][0]), abs(coordenadas_perso[0][1] - coordenadas_perso[2][1]))
                    distancia_ate_itd = max(abs(coordenadas_perso[1][0] - coordenadas_perso[2][0]), abs(coordenadas_perso[1][1] - coordenadas_perso[2][1]))
                    if vidas[1] == 0:
                        if distancia_ate_yuta == 1:
                            if yuta_imunidade == 0:
                                vidas[0] -= output_sukuna
                                print('Sukuna: Ruptura')
                        elif distancia_ate_yuta <= 3:
                            if yuta_imunidade == 0:
                                vidas[0] -= int(output_sukuna/2 + 1) 
                                print('Sukuna: Desmantelar')
                    else:
                        if distancia_ate_yuta <= distancia_ate_itd:
                            if distancia_ate_yuta == 1:
                                if yuta_imunidade == 0:
                                    vidas[0] -= output_sukuna
                                    print('Sukuna: Ruptura')
                            elif distancia_ate_yuta <= 3:
                                if yuta_imunidade == 0:
                                    vidas[0] -= int(output_sukuna/2 + 1) 
                                    print('Sukuna: Desmantelar')
                        else:
                            if distancia_ate_itd == 1:
                                vidas[1] -= output_sukuna
                                print('Sukuna: Ruptura')
                            elif distancia_ate_itd <= 3:
                                vidas[1] -= int(output_sukuna/2 + 1)
                                print('Sukuna: Desmantelar')


    #codigos para vidas abaixos de 0
    for index in range(len(vidas)):
        if vidas[index] < 0:
            vidas[index] = 0
    #incrementa o turno e printa a matriz caso seja o ultimo
    contagem_turnos += 1
    if contagem_turnos > 4:
        contagem_turnos = 1
        
        #construtor da matriz jogo
        matriz_jogo = []
        for linha in range(matriz_katanas[0]):
            linha_matriz = []
            for coluna in range(matriz_katanas[0]):
                if [linha, coluna] == coordenadas_perso[0]:
                    linha_matriz.append('Y')
                elif [linha, coluna] == coordenadas_perso[1]:
                    linha_matriz.append('I')
                elif [linha, coluna] == coordenadas_perso[2]:
                    linha_matriz.append('S')
                elif [linha, coluna] in coordenadas_katanas:
                    linha_matriz.append('K')
                else:
                    linha_matriz.append('0')
            matriz_jogo.append(linha_matriz)

        #printa a matriz atual
        for linha in range(matriz_katanas[0]):
            linha_formatada = ' '.join(matriz_jogo[linha])
            print(linha_formatada)
        #printa as vidas
        print(f'Yuta: {vidas[0]}/50')
        print(f'Itadori: {vidas[1]}/50')
        print(f'Sukuna: {vidas[2]}/100')

        #flag de impressa no ultimo turno, reseta no inicio do while
        matriz_impressa = True

    #condições de vitoria
    if vidas[0] == 0 or vidas[2] == 0 or output_sukuna == 0:
        jogo_terminou = True

if not matriz_impressa:
        matriz_jogo = []
        for linha in range(matriz_katanas[0]):
            linha_matriz = []
            for coluna in range(matriz_katanas[0]):
                if [linha, coluna] == coordenadas_perso[0]:
                    linha_matriz.append('Y')
                elif [linha, coluna] == coordenadas_perso[1]:
                    linha_matriz.append('I')
                elif [linha, coluna] == coordenadas_perso[2]:
                    linha_matriz.append('S')
                elif [linha, coluna] in coordenadas_katanas:
                    linha_matriz.append('K')
                else:
                    linha_matriz.append('0')
            matriz_jogo.append(linha_matriz)

        #printa a matriz atual
        for linha in range(matriz_katanas[0]):
            linha_formatada = ' '.join(matriz_jogo[linha])
            print(linha_formatada)
        #printa as vidas
        print(f'Yuta: {vidas[0]}/50')
        print(f'Itadori: {vidas[1]}/50')
        print(f'Sukuna: {vidas[2]}/100')
#prints de vitorias
if vidas[0] == 0:
    print('Sukuna: Escama dracônica\nSukuna: Repulso\nSukuna: Díade de meteoros\n')
    print('Sukuna: Desmantelar')
if output_sukuna == 0:
    print('Yuta: Emissão máxima - Escada de Jacó!\nItadori: Acorde, Fushiguro!')
if vidas[2] == 0:
    print('Itadori: Sukuna, vamos colocar um fim nesse ciclo de maldições!!!')

