#definição de funções
def achar_caminho(pos_wolf, matriz, auxiliar, N, M):
    """com ajuda de uma matriz auxiliar, calcula o caminho mais optimal para chegar no canto
    inferior direito da matriz"""
    #variáveis
    linha_atual = pos_wolf[0]
    coluna_atual = pos_wolf[1]
    movimentos_ate_aqui = auxiliar[linha_atual][coluna_atual]
    #cima, baixo, esquerda, direita
    movimentos_normais = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    movimentos_gancho = [[-2, 0], [2, 0], [0, -2], [0, 2]]

    #análise para movimentos normais
    auxiliar = olhar_vizinhos(movimentos_ate_aqui, movimentos_normais, linha_atual, coluna_atual, matriz, auxiliar, N, M)
    #análise para movimentos no gancho(apenas se o tile atual for um gancho)
    if matriz[linha_atual][coluna_atual] == 2:
       auxiliar = olhar_vizinhos(movimentos_ate_aqui, movimentos_gancho, linha_atual, coluna_atual, matriz, auxiliar, N, M)


    #checa se conseguiu chegar ou não e retorna a qtd de movimentos caso sim
    if auxiliar[N-1][M-1] != 9999:
        return matriz_auxiliar[N-1][M-1], True
    else:
        return matriz_auxiliar, False
def olhar_vizinhos(movimentos_ate_aqui, movimentos_disponiveis, linha_atual, coluna_atual, matriz, auxiliar, N, M):
        for movimento_horizontal, movimento_vertical in movimentos_disponiveis:
            #soma o movimento as coords atuais
            nova_linha = linha_atual + movimento_horizontal
            nova_coluna = coluna_atual + movimento_vertical
            
            #checa se ta dentro da matriz com o movimento
            if (0 <= nova_linha and nova_linha < N) and (0 <= nova_coluna < M):
                #checa o destino
                destino = matriz[nova_linha][nova_coluna]
                #se for 0, nem tenta
                if destino != 0:
                    #caminho furtivo ou gancho
                    if destino == 1 or destino== 2:
                        custo_movimento = 1
                    #inimigo
                    else:
                        custo_movimento = 3
                    #calcula o custo do movimento total até lá
                    movimento_total = movimentos_ate_aqui + custo_movimento
                    #se o mov menor que de todos já gravados, se torna o menor mov ate lá
                    if movimento_total < auxiliar[nova_linha][nova_coluna]:
                        auxiliar[nova_linha][nova_coluna] = movimento_total
                        #chama a função recursivamente a partir da nova coordenada
                        temp_pos_wolf = [nova_linha, nova_coluna]
                        achar_caminho(temp_pos_wolf, matriz, auxiliar, N, M)
        #retorna a matriz auxiliar adquirida para ter uma memória
        return auxiliar
#inputs
linhas = int(input())
colunas = int(input())
#constroi matrizes
matriz_jogo = []
matriz_auxiliar = []
for linha in range(linhas):
    #matriz jogo
    linha_formatada = input().split()
    linha_formatada = [int(elem) for elem in linha_formatada]
    matriz_jogo.append(linha_formatada)

    #matriz auxiliar
    linha_auxiliar = []
    for coluna in range(colunas):
        if [linha, coluna] == [0, 0]:
            linha_auxiliar.append(0)
        else:
            linha_auxiliar.append(9999)
    matriz_auxiliar.append(linha_auxiliar)

posicao_wolf = [0, 0]

#entra na função recursiva
print('=== SEKIRO: O RESGATE DE CESAR ===\nWolf deve resgatar CESAR!')
movimentos, conseguiu = achar_caminho(posicao_wolf, matriz_jogo, matriz_auxiliar, linhas, colunas)

#printa caso tenha conseguido ou não, e a qtd de movimentos se sim
if conseguiu:
    print(f'SUCESSO! Wolf resgatou o Cesar em {movimentos} movimentos!')
    if movimentos <= 4:
        print('PERFEITO! Verdadeiro Shinobi! Cesar está ORGULHOSO!!')
    elif movimentos < 8:
        print('BOM! Caminho eficiente! Mas você quase decepcionou Cesar')
    else:
        print('Wolf chegou, mas pode melhorar... Cesar está decepcionado, quase morreu de tédio!')
else:
    print('MORTE! Wolf não conseguiu resgatar Cesar... ele nunca saberá quem venceu Satoru Gojo ou Sukuna!')
