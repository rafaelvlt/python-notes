ordem_matriz = int(input())
matriz_jogo = []
#construtor da matriz jogo
for linha in range(ordem_matriz):
    #reseta a linha inicio de loop
    linha_matriz = []
    #constroi cada linha
    linha_bruta = input()
    linha_matriz = linha_bruta.split(' ')
    matriz_jogo.append(linha_matriz)

#armazena posição do homem aranha
for linha in range(ordem_matriz):
    for coluna in range(ordem_matriz):
        if matriz_jogo[linha][coluna] == 'H':
            posicao_linha = linha
            posicao_coluna = coluna
#game loop
jogo_acabou = False
dia = 1
timer_electro = 0
qtd_restaurados = 0
qtd_destruidos = 0
local_atual = ''
mensagem_dia = ''
while not jogo_acabou:
    comando = input()

    #seção de comandos de movimentos, todos são iguais, só mudam as condições para ser cima, baixo, etc
    if comando == 'Cima':
        #caso esteja não esteja fora dos limites segue normalmente
        if not posicao_linha-1 < 0:
            if matriz_jogo[posicao_linha-1][posicao_coluna] == 'X': #caso seja um X
                mensagem_dia = 'Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!'
            else:
                #lógica de local anterior
                matriz_jogo[posicao_linha][posicao_coluna] = '.'
                #salva o local atual antes do homem aranha
                local_atual = matriz_jogo[posicao_linha-1][posicao_coluna]
                posicao_linha -= 1
                matriz_jogo[posicao_linha][posicao_coluna] = 'H'
        else:
            mensagem_dia = 'Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!'
    elif comando == 'Baixo':
        #caso esteja não esteja fora dos limites segue normalmente
        if not posicao_linha+1 > ordem_matriz-1:
            if matriz_jogo[posicao_linha+1][posicao_coluna] == 'X': #caso seja um X
                mensagem_dia = 'Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!'
            else:
                #lógica de local anterior
                matriz_jogo[posicao_linha][posicao_coluna] = '.'
                #salva o local atual antes do homem aranha
                local_atual = matriz_jogo[posicao_linha+1][posicao_coluna]
                posicao_linha += 1
                matriz_jogo[posicao_linha][posicao_coluna] = 'H'
        else:
            mensagem_dia = 'Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!'
    elif comando == 'Esquerda':
    #caso esteja não esteja fora dos limites segue normalmente
        if not posicao_coluna-1 < 0:
            if matriz_jogo[posicao_linha][posicao_coluna-1] == 'X': #caso seja um X
                mensagem_dia = 'Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!'
            else:
                #lógica de local anterior
                matriz_jogo[posicao_linha][posicao_coluna] = '.'
                #salva o local atual antes do homem aranha
                local_atual = matriz_jogo[posicao_linha][posicao_coluna-1]
                posicao_coluna -= 1
                matriz_jogo[posicao_linha][posicao_coluna] = 'H'
        else:
            mensagem_dia = 'Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!'
    elif comando == 'Direita':
        #caso esteja não esteja fora dos limites segue normalmente
        if not posicao_coluna+1 > ordem_matriz-1:
            if matriz_jogo[posicao_linha][posicao_coluna+1] == 'X': #caso seja um X
                print('Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!')
            else:
                #lógica de local anterior
                matriz_jogo[posicao_linha][posicao_coluna] = '.'
                #salva o local atual antes do homem aranha
                local_atual = matriz_jogo[posicao_linha][posicao_coluna+1]
                posicao_coluna += 1
                matriz_jogo[posicao_linha][posicao_coluna] = 'H'
        else:
            mensagem_dia = 'Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!'
    #comando para fim de jogo
    elif comando == 'FIM': 
        #checa na matriz inteira quantos quarteirões corrompidos existem
        qtd_corrompidos = 0
        for linha in range(ordem_matriz):
            for coluna in range(ordem_matriz):
                if matriz_jogo[linha][coluna] == 'E':
                    qtd_corrompidos += 1
        if qtd_corrompidos != 0:
            print('Ainda existem quarteirões corrompidos! O Miranha não pode ir embora agora!')
            jogo_acabou = True
        else:
            jogo_acabou = True
    
    if jogo_acabou != True:
        #lógica para o local atual e mensagem especial
        if local_atual == '.': #incrementa o timer e printa mensagem
            mensagem_dia = 'O Electro está ganhando espaço!'
            timer_electro += 1

        elif local_atual == 'E':
            #checa na matriz inteira quantos quarteirões corrompidos existem
            qtd_corrompidos = 1
            for linha in range(ordem_matriz):
                for coluna in range(ordem_matriz):
                    if matriz_jogo[linha][coluna] == 'E':
                        qtd_corrompidos += 1

            #checa para ver qtd corrompidos, se houver mais de um, o jogo continua, se não, acaba
            if qtd_corrompidos > 0:
                mensagem_dia = 'O Miranha restaurou um quarteirão!'
                qtd_restaurados += 1
                timer_electro = 0

        #electro destruindo quarteirao
        if timer_electro == 3:
            timer_electro = 0
            corrompido_achado = False
            for linha in range(ordem_matriz):
                for coluna in range(ordem_matriz):
                    if matriz_jogo[linha][coluna] == 'E' and corrompido_achado != True:
                        matriz_jogo[linha][coluna] = 'X'
                        corrompido_achado = True
        #checagem de quarteiroes destruidos
        qtd_destruidos = 0
        for linha in range(ordem_matriz):
            for coluna in range(ordem_matriz):
                if matriz_jogo[linha][coluna] == 'X':
                    qtd_destruidos += 1



        
        #print do diário
        if jogo_acabou != True:
            print(f'Dia {dia}') #dia
            #matriz formatada por linhas
            for linha in range(ordem_matriz):
                linha_formatada = ' '.join(matriz_jogo[linha])
                print(linha_formatada)
            #posicao atual homem aranha
            print(f'Posição atual do Homem-Aranha: ({posicao_linha}, {posicao_coluna})')
            #quarteirões restaurados e destruidos
            print(f'Quarteirões restaurados: {qtd_restaurados} | Quarteirões destruídos: {qtd_destruidos}')
            #mensagem do dia e quebra de linha
            print(mensagem_dia) 
            print('')
            dia += 1

        #checagem corrompidos para fim de jogo
        qtd_corrompidos = 0
        for linha in range(ordem_matriz):
            for coluna in range(ordem_matriz):
                if matriz_jogo[linha][coluna] == 'E':
                    qtd_corrompidos += 1
        if qtd_corrompidos == 0 and qtd_restaurados > 0:
            print('Missão cumprida! Nova York está segura e o Miranha faz tudo novamente!')
            jogo_acabou = True
        if dia == 7 and qtd_corrompidos == 0:
            print('O Miranha não conseguiu restaurar a cidade a tempo, o Electro venceu!')
            jogo_acabou = True




