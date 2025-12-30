#definição de função
def encontrar_menor_caminho(posicao_aventureiro, posicao_alvo, mapa, custos, N, M):
    """acha o caminho mais curto até o alvo, retornando o custo em resistencia e a trajetoria"""
    linha_inicial = posicao_aventureiro[0]
    coluna_inicial = posicao_aventureiro[1]
    #cria mapa de custos
    mapa_de_custos = []
    for linha in range(N):
        linha_formatada = []
        for coluna in range(M):
            if [linha, coluna] == posicao_aventureiro:
                linha_formatada.append(0)
            else:
                linha_formatada.append(99999)
        mapa_de_custos.append(linha_formatada)
    #cria mapa de anteriores
    mapa_caminho = []
    for linha in range(N):
        linha_formatada = []
        for coluna in range(M):
            if [linha, coluna] == posicao_aventureiro:
                linha_formatada.append('inicio')
            else:
                linha_formatada.append(0)
        mapa_caminho.append(linha_formatada)
    trajetoria = []

    #utiliza algoritmo de djikastra para achar o custo minimo para cada entrada
    mapa_de_custos, mapa_caminho = buscar_caminho(linha_inicial, coluna_inicial, mapa, mapa_de_custos, mapa_caminho, custos, N, M)
    
    #checa a resistencia até chegar ao alvo
    linha_final = posicao_alvo[0]
    coluna_final = posicao_alvo[1]
    resistencia_final = mapa_de_custos[linha_final][coluna_final]

    if resistencia_final == 99999: #se o nao foi caminho encontrado
        return 99999, [] 
    else:
        #se foi encontrado, reconstroi a trajetória e retorna a resistencia até o caminho
        trajetoria = reconstruir_caminho(posicao_aventureiro, posicao_alvo, mapa_caminho, trajetoria)
        return resistencia_final, trajetoria
def buscar_caminho(linha_atual, coluna_atual, mapa, mapa_de_custos, mapa_caminho, custos, N, M):
    """função recursiva que utiliza do algoritmo de djikastris pra achar o custo em resistencia para chegar até um ponto"""
    movimentos_normais = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    resistencia_ate_aqui = mapa_de_custos[linha_atual][coluna_atual]

    for movimento_horizontal, movimento_lateral in movimentos_normais:
        #soma o movimento as coords atuais
        proxima_linha = linha_atual + movimento_horizontal
        proxima_coluna = coluna_atual + movimento_lateral

         #checa se ta dentro da matriz com o movimento
        if (0 <= proxima_linha and proxima_linha < N) and (0 <= proxima_coluna and proxima_coluna < M):
            #checa o destino
            proximo_ponto = mapa[proxima_linha][proxima_coluna]
            #se for #, nem tenta
            if proximo_ponto != '#':
                custo_passo = 0
                #caminhos seguros
                if proximo_ponto in ['S', 'K', 'G', '.']:
                    custo_passo = custos[0]
                #armadilha
                elif proximo_ponto == 'T':
                    custo_passo = custos[1]
                #esqueleto
                elif proximo_ponto == 'E':
                    custo_passo = custos[2]
                
                resistencia_total = resistencia_ate_aqui + custo_passo
                #se a resistencia é menor que de todos já gravados, se torna a menor resistencia ate lá
                if resistencia_total < mapa_de_custos[proxima_linha][proxima_coluna]:
                    mapa_de_custos[proxima_linha][proxima_coluna] = resistencia_total
                    mapa_caminho[proxima_linha][proxima_coluna] = [linha_atual, coluna_atual]
                    #chama a função recursivamente a partir da nova coordenada
                    buscar_caminho(proxima_linha, proxima_coluna, mapa, mapa_de_custos, mapa_caminho, custos, N, M)
    return mapa_de_custos, mapa_caminho
def reconstruir_caminho(posicao_inicial, posicao_final, mapa_caminho, trajetoria):
    """função usada para reconstruir a trajetoria de menor custo, retornando a trajetoria em uma lista"""
    #a partir da posicao final, vai refazendo o caminho de menor resistencia até chegar ao ponto inicial
    posicao_atual = posicao_final
    inicio = mapa_caminho[posicao_inicial[0]][posicao_inicial[1]]
    while posicao_atual != inicio:
        trajetoria.append(posicao_atual)
        posicao_atual = mapa_caminho[posicao_atual[0]][posicao_atual[1]]
    trajetoria.reverse()
    
    return trajetoria

def matriz_final(trajetoria_primeira, trajetoria_segunda, posicao_aventureiro, posicao_espada, posicao_altar, N, M):
    """recebe dados da trajetoria e posicoes e printa a matriz final"""
    #constroi o mapa final
    mapa_final = []
    for linha in range(N):
        linha_formatada = []
        for coluna in range(M):
            if [linha, coluna] == posicao_aventureiro:
                linha_formatada.append('S')
            elif [linha, coluna] == posicao_espada:
                linha_formatada.append('K')
            elif [linha, coluna] == posicao_altar:
                linha_formatada.append('G')  
            elif [linha, coluna] in trajetoria_primeira or [linha, coluna] in trajetoria_segunda:
                linha_formatada.append('*')
            else:
                linha_formatada.append('#')
        mapa_final.append(linha_formatada)
    
    #printa o mapa final
    for linha in range(N):
        linha_print = "".join(mapa_final[linha])
        print(linha_print)

    return 0

#fim das definições de funções

#input
linhas_e_colunas = input()
linhas_e_colunas = [int(elem) for elem in linhas_e_colunas.split()]
N = linhas_e_colunas[0]
M = linhas_e_colunas[1]
#variaveis de posicao
posicao_aventureiro = []
posicao_espada = []
posicao_altar = []
#construção do mapa
mapa = []
for linha in range(N):
    entrada = input()
    linha_formatada = [elem for elem in entrada]
    for char in linha_formatada:
        if char == 'S':
            posicao_aventureiro = [linha, linha_formatada.index(char)]
        elif char == 'K':
            posicao_espada = [linha, linha_formatada.index(char)]
        elif char == 'G':
            posicao_altar = [linha, linha_formatada.index(char)]
    mapa.append(linha_formatada)
resistencia_maxima = int(input())
#custos de energia
custos = input().split()
custos = [int(custo) for custo in custos]
reviver = int(input())
sucesso = False
renasceu = False

#caminho de S -> K
trajetoria_k = []
custo_ate_k = 0
custo_ate_k, trajetoria_k = encontrar_menor_caminho(posicao_aventureiro, posicao_espada, mapa, custos, N, M)
#caso não haja caminho, falha diretamente
if trajetoria_k == []:
    print("A escuridão sussurra derrota... Não há caminho.")
elif (resistencia_maxima - custo_ate_k) < 0:
    print('A alma definha... Resistencia esgotada.')
else:
    #caminho de K até G
    resistencia_atual = resistencia_maxima - custo_ate_k
    custo_k_ate_g = 0
    trajetoria_k_ate_g = []
    #entrar na recursão de K até G
    custo_k_ate_g, trajetoria_k_ate_g = encontrar_menor_caminho(posicao_espada, posicao_altar, mapa, custos, N, M)
    #caso não haja caminho valido
    if trajetoria_k_ate_g == []:
        print('A escuridão sussurra derrota... Não há caminho.')
    elif (resistencia_atual - custo_k_ate_g) >= 0: #caso consiga ir direto de S até G sem ser revivido
         print('Lamina Profanada recuperada! Altar alcançado!')
         custo_total = custo_ate_k + custo_k_ate_g
         #soma os caminhos de K e de k até G, removendo a dupla coordenada em K
         trajetoria_final = trajetoria_k + trajetoria_k_ate_g[1:]
         #formatação, coordenadas tem que ser invertidas pra ficar em x e y
         caminho_final = [f'({coord[1]},{coord[0]})' for coord in trajetoria_final]
         caminho_final = " -> ".join(caminho_final)
         sucesso = True
    elif reviver == 1: #caso possa reviver, revive
        resistencia_atual = resistencia_maxima
        custo_s_ate_g = 0
        trajetoria_s_ate_g = []

        custo_s_ate_g, trajetoria_s_ate_g = encontrar_menor_caminho(posicao_aventureiro, posicao_altar, mapa, custos, N, M)

        if (resistencia_atual - custo_s_ate_g ) < 0: #caso falhe mesmo com revive
            print('Mesmo renascido das cinzas, o destino era a derrota.')
        else: #sucesso com revive
            print('Com a ajuda dos deuses antigos, o altar foi alcançado!')
            custo_total = custo_s_ate_g
            sucesso = True
            renasceu = True
            #formatação, coordenadas tem que ser invertidas pra ficar em x e y
            caminho_espada = [f'({coord[1]},{coord[0]})' for coord in trajetoria_k]
            caminho_espada = " -> ".join(caminho_espada)
            caminho_altar = [f'({coord[1]},{coord[0]})' for coord in trajetoria_s_ate_g]
            caminho_altar = " -> ".join(caminho_altar)
    else: #se morreu no caminho de K até G e não tem revive
        print('A alma definha... Resistencia esgotada.')

if sucesso:
    print(f'Custo total de Resistencia: {custo_total}')
    if renasceu:
        print('Caminho:')
        print(caminho_espada)
        print('...revivido das cinzas em S...')
        print(caminho_altar)
        print('Visualização do Caminho:')
        matriz_final(trajetoria_k, trajetoria_s_ate_g, posicao_aventureiro, posicao_espada, posicao_altar, N, M)
    else:
        print('Caminho:')
        print(caminho_final)
        print('Visualização do Caminho:')
        matriz_final(trajetoria_final, [], posicao_aventureiro, posicao_espada, posicao_altar, N, M)
