#declaração de funções
def analisar_atributos(lista_de_atributos, personagem):
    """recebe um input e analisa a frase para descobrir de qual atributo fala e qual valor, retornando a lista de atributos com o valor alterado"""
    atributos = ['força', 'agilidade', 'ki', 'super saiyajin']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    argumento = input()
    argumento = argumento.lower()
    for atributo in atributos:
        if atributo in argumento:
            if atributo == 'força':
                valor = buscar_valor_atributo(argumento, numeros)
                lista_de_atributos[0] = valor
                print(f'Computando força de {personagem}: {valor}')
            elif atributo == 'agilidade':
                valor = buscar_valor_atributo(argumento, numeros)
                lista_de_atributos[1] = valor
                print(f'Computando agilidade de {personagem}: {valor}')
            elif atributo == 'ki':
                valor = buscar_valor_atributo(argumento, numeros)
                lista_de_atributos[2] = valor
                print(f'Computando Ki de {personagem}: {valor}')
            else:
                valor = buscar_valor_atributo(argumento, numeros)
                lista_de_atributos[3] = valor
                if valor != 0:
                    print(f'Computando Transformação Super Saiyajin de {personagem}: {valor}')
    return lista_de_atributos
def campo_de_batalha(posicao_C, posicao_A, personagem_C, personagem_A, N):
    """recebe coordenadas de ambos personagens(listas), nomes dos personagems e a ordem da matriz, printa a matriz do jogo"""
    campo = []
    #constroi a matriz pondo os personagens nela
    for linha in range(N):
        linha_construtor = []
        for coluna in range(N):
            if [linha, coluna] == posicao_C:
                linha_construtor.append(personagem_C[0])
            elif [linha, coluna] == posicao_A:
                linha_construtor.append(personagem_A[0])
            else:
                linha_construtor.append('0')
        campo.append(linha_construtor)
    #printa a matriz
    print('')
    for linha in range(N):
        linha_formatada = ' '.join(campo[linha])
        print(linha_formatada)
    print('')
def calcular_distancia(coordenadas_caesar, coordenadas_artur):
    """recebe as coordenadas dos personagens de artur e caesar(listas) e devolte a distancia euclidiana(int)"""
    distancia = ((coordenadas_caesar[0] - coordenadas_artur[0])**2 + (coordenadas_caesar[1] - coordenadas_artur[1])**2)**(0.5)
    return int(distancia)

def movimentacao(posicao, direcao, qtd_movimento, caracteristica, N):
    #pode tentar se mover para fora e também se mover mais do que consegue, fazer limite de movimentação
    """recebe variaveis para posicao atual(lista), direcao(str), desejo de movimento(int) e as caracteristicas do personagem(lista) e retorna a nova posicao(lista)"""
    
    if qtd_movimento > caracteristica[3]:
        qtd_movimento = caracteristica[3]
    #posicao[0] == linhas, posicao[1] = coluna
    if direcao == 'cima':
        posicao[0] -= qtd_movimento
        if posicao[0] < 0:
            posicao[0] = 0
    elif direcao == 'baixo':
        posicao[0] += qtd_movimento
        if posicao[0] < 0:
            posicao[0] = 0
            if posicao[0] > N-1:
                posicao[0] = N-1
    elif direcao == 'esquerda':
        posicao[1] -= qtd_movimento
        if posicao[1] < 0:
            posicao[1] = 0
    elif direcao == 'direita':
        posicao[1] += qtd_movimento
        if posicao[1] > N-1:
            posicao[1] = N-1
    return posicao
def buscar_valor_atributo(frase, lista_de_numeros):
    """busca por um inteiro em uma string, retornado seu valor numéricos"""
    valor = ''
    frase_dividida = frase.split()
    for palavra in frase_dividida:
        if palavra[0] in lista_de_numeros:
                for caracter in palavra:
                    if caracter in lista_de_numeros:
                        valor += caracter
                else:         
                    return int(valor)  
    return 0
def calcular_caracteristicas(lista_de_atributos):
    """pega lista de atributos e retorna uma lista de caracteristicas"""
    #vida
    caracteristicas = []
    vida = (lista_de_atributos[2] + lista_de_atributos[0]) * (1 + lista_de_atributos[3])
    ataque = (lista_de_atributos[0] * (1 + lista_de_atributos[3]) * 5)
    energia = (lista_de_atributos[2] * (1 + lista_de_atributos[3]))
    velocidade = (1 + lista_de_atributos[1]//100)
    caracteristicas = [vida, ataque, energia, velocidade]
    return caracteristicas
def socar(atacante, oponente):
    """recebe duas listas de caracteristicas, retorna a lista do oponente com a vida trocada"""
    oponente[0] -= atacante[1]
    if oponente[0] < 0:
        oponente[0] = 0
    return oponente
def ataque_de_ki(atacante, oponente, energia):
    """recebe duas listas de caracteristicas, retorna ambas com energia gasta e dano recebido"""
    if energia > atacante[2]:
        return atacante, oponente
    oponente[0] -= energia
    atacante[2] -= energia
    if oponente[0] < 0:
        oponente[0] = 0
    if atacante[2] < 0:
        atacante[2] = 0
    return atacante, oponente
def power_up(caracteristicas_personagem):
    """recebe lista de caracteristicas do personagem e dobra as caracteristicas"""
    caracteristicas_personagem[1] *= 2
    caracteristicas_personagem[2] *= 2
    return caracteristicas_personagem
def mostrar_atributos(atributos, personagem):
    """recebe lista de atributos e nome do personagem e printa no formato certo"""
    print(f'{personagem}: Força física: {atributos[0]}')
    print(f'Agilidade: {atributos[1]}')
    print(f'Ki: {atributos[2]}')
    if atributos[3] != 0:
        print(f'Transformação em Super Saiyajin: {atributos[3]}')
    print('')
#fim da declaração de funções

#variáveis
personagem_caesar = input()
personagem_artur = input()
print(f'Você sabe que {personagem_artur} é mais forte, nem tente dizer o contrário Caesar!\nNem venha Artur, {personagem_caesar} ganharia fácil numa luta.\n')

#indices: força = 0, agilidade = 1, ki = 2, super sayajin = 3
atributos_caesar = [0, 0, 0, 0]
atributos_artur = [0, 0, 0, 0]
#argumentos de características
for vez in range(0, 8):
    if vez % 2 == 0:
        atributos_caesar = analisar_atributos(atributos_caesar, personagem_caesar)
    else:
       atributos_artur = analisar_atributos(atributos_artur, personagem_artur)
#printa os atributos no formato pedido
print('')
mostrar_atributos(atributos_caesar, personagem_caesar)
mostrar_atributos(atributos_artur, personagem_artur)


#calcula caracteristicas pra cada, indices: vida = 0, ataque = 1, energia = 2, velocidade = 3
caracteristicas_caesar = calcular_caracteristicas(atributos_caesar)
caracteristicas_artur = calcular_caracteristicas(atributos_artur)

#variaveis loop de batalha
ordem_matriz = int(input())
acabou = False
posicao_caesar = [0, 0]
posicao_artur = [ordem_matriz-1, ordem_matriz-1]
sofreu_dano = ''
#decide quem começa
if atributos_caesar[1] < atributos_artur[1]:
    turno = personagem_artur
    oponente = personagem_caesar
else:
    turno = personagem_caesar
    oponente = personagem_artur
#começa simulação de batalha
print(f'Iniciando simulação de batalha: {personagem_caesar} VS {personagem_artur}!')
campo_de_batalha(posicao_caesar, posicao_artur, personagem_caesar, personagem_artur, ordem_matriz)
while not acabou:
    acao = input()
    if acao == 'mover':
        direcao = input()
        quantidade = int(input())
        if turno == personagem_caesar:
            posicao_caesar = movimentacao(posicao_caesar, direcao, quantidade, caracteristicas_caesar, ordem_matriz)
            if caracteristicas_caesar[3] > caracteristicas_artur[3]:
                print(f'{personagem_caesar} se move com uma agilidade impressionante! Será que seu oponente poderá acompanhar sua velocidade?')
        else:
            posicao_artur = movimentacao(posicao_artur, direcao, quantidade, caracteristicas_artur, ordem_matriz)
            if caracteristicas_artur[3] > caracteristicas_caesar[3]:
                print(f'{personagem_artur} se move com uma agilidade impressionante! Será que seu oponente poderá acompanhar sua velocidade?')
        campo_de_batalha(posicao_caesar, posicao_artur, personagem_caesar, personagem_artur, ordem_matriz)
        #checa quem tem a maior velocidade para printar


    elif acao == 'soco':
        if calcular_distancia(posicao_artur, posicao_caesar) <= 1:
            if turno == personagem_caesar:
                caracteristicas_artur = socar(caracteristicas_caesar, caracteristicas_artur)
                sofreu_dano = personagem_artur
                if caracteristicas_caesar[1] > caracteristicas_artur[1]:
                    print(f'{personagem_caesar} acerta um poderoso golpe! O oponente pode sentir o peso de cada ataque')
            else:
                caracteristicas_caesar = socar(caracteristicas_artur, caracteristicas_caesar)
                sofreu_dano = personagem_caesar
                if caracteristicas_artur[1] > caracteristicas_caesar[1]:
                    print(f'{personagem_artur} acerta um poderoso golpe! O oponente pode sentir o peso de cada ataque')
                    
    elif acao == 'ataque de ki':
        energia_ataque = int(input())
        if calcular_distancia(posicao_caesar, posicao_artur) <= 5:
            if turno == personagem_caesar:
                caracteristicas_caesar, caracteristicas_artur = ataque_de_ki(caracteristicas_caesar, caracteristicas_artur, energia_ataque)
                sofreu_dano = personagem_artur
            else:
                caracteristicas_artur, caracteristicas_caesar = ataque_de_ki(caracteristicas_artur, caracteristicas_caesar, energia_ataque)
                sofreu_dano = personagem_caesar
        print(f'{turno} está concentrando seu ki em um devastador ataque de energia!')
    elif acao == 'power up':
        conseguiu = input()
        print('A'*25 + 'H'*5+'!'*3)
        if conseguiu == 'sim':
            if turno == personagem_caesar:
                power_up(caracteristicas_caesar)
            else:
                power_up(caracteristicas_artur)

    #checks de fim de loop
    #fim por vida
    if caracteristicas_caesar [0] == 0 or caracteristicas_artur[0] == 0:
        acabou = True 
    else:
        #se nao acabou, printa quem tomou dano e a vida
        if sofreu_dano == personagem_caesar:
            print(f'{personagem_caesar} sofreu um ataque, e agora está com {caracteristicas_caesar[0]} de vida')
        elif sofreu_dano == personagem_artur:
            print(f'{personagem_artur} sofreu um ataque, e agora está com {caracteristicas_artur[0]} de vida')
    #fim por energia
    if caracteristicas_caesar [2] == 0 or caracteristicas_artur[2] == 0:
        acabou = True
    #printa se tiver um vencedor
    if acabou:
        print('TEMOS UM VENCEDOR!')
    #troca de turno
    if turno == personagem_caesar:
        turno = personagem_artur
    else:
        turno = personagem_caesar
    #reset de variável
    sofreu_dano = ''


#prints de fim de combate
#casos com vitoria energia sobrando
if caracteristicas_artur[0] == 0 and caracteristicas_caesar[2] > 0:
    print(f'{personagem_caesar} nem precisou se esforçar nessa luta, Artur! Da proxima vez vê se você escolhe um oponente realmente forte')
elif caracteristicas_caesar[0] == 0 and caracteristicas_artur[2] > 0:
    print(F'Essa luta nem deu pro gasto, já estava claro que {personagem_artur} ia ganhar!')
#casos vencedor sem energia
elif caracteristicas_artur[0] == 0 and caracteristicas_caesar[2] == 0:
    print(f'Ok, pode ter sido uma luta acirrada, mas {personagem_caesar} nunca desaponta!')
elif caracteristicas_caesar[0] == 0 and caracteristicas_artur[2] == 0:
    print(f'Foi uma boa luta, mas {personagem_artur} mostrou que era o melhor afinal!')
#casos esgotamento de energia
elif caracteristicas_artur[2] == 0:
    print(f'{personagem_caesar} faz qualquer luta parecer fácil, mas essa aqui fez o {personagem_artur} passar vergonha!')
elif caracteristicas_caesar[2] == 0:
    print(f'A diferença de poder era tanta que {personagem_artur} mal precisou encostar no {personagem_caesar} e já ganhou')
