#definição de funções
def interpretar_expressao(expressao):
    """recebe uma string com uma expressão em notação polonesa e retorna 0 ou 1, dependendo se for primo ou não"""
    resultado = 0
    pilha = []
    expressao = expressao.split(" ")
    expressao.reverse()
    for elemento in expressao:
        if elemento in "+-/*":
            if elemento == '+':
                pilha.insert(0, pilha[0] + pilha[1])
                pilha.pop(1)
                pilha.pop(1)
            elif elemento == '-':
                pilha.insert(0, pilha[0] - pilha[1])
                pilha.pop(1)
                pilha.pop(1)
            elif elemento == '*':
                pilha.insert(0, pilha[0] * pilha[1])
                pilha.pop(1)
                pilha.pop(1)
            elif elemento == '/':
                pilha.insert(0, pilha[0] // pilha[1])
                pilha.pop(1)
                pilha.pop(1)
        else:
            pilha.insert(0, int(elemento))
    resultado = pilha[0]
    return resultado

def prime_check(numero):
    """recebe um número e checa se é primo, retornando 1 ou 0 (string)"""
    if numero < 2:
        return '0'
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return '0'
    return '1'

def convertedor_binario(binario):
    """recebe uma string em binário e converte para decimal usando de potencias base 2"""
    resultado = 0
    index = 0
    for elemento in binario[::-1]:
        if elemento == '1':
            resultado += 2**index
        index += 1
    return resultado
def processar_coordenada(n):
    """função feita para receber todas expressões e processar a coordenada até o estado final"""
    resultado = 0
    entrada = input()
    binario_puro = ''
    while entrada != '':
        binario_puro += prime_check(interpretar_expressao(entrada))
        entrada = input()
    coordenada_pura = convertedor_binario(binario_puro)
    resultado = coordenada_pura % n
    return resultado, binario_puro
def esfera_mais_próxima(coordenadas, coord_goku):
    """pega a distancia euclidiana entre o goku e todas esferas pra definir qual a mais próxima"""
    esfera = []
    menor_distancia = 9999999
    for esfera_atual in coordenadas:
        distancia = ((esfera_atual[0] - coord_goku[0])**2 + (esfera_atual[1] - coord_goku[1])**2)**(0.5)
        if distancia < menor_distancia:
            menor_distancia = distancia
            esfera = esfera_atual
    return esfera
#fim de definição de funções

#inputs iniciais
ordem_matriz = int(input())
coordenadas_goku = input()
#transforma o input em uma lista com as coordenadas dadas como inteiro
coordenadas_goku = [int(coordenada) for coordenada in coordenadas_goku[1:-1].split(", ")]
#variáveis
recebido = input()
procurando = 'x'
coordenada_x = 0
coordenada_y = 0
binario_printado = ''
qtd_esferas = 1
distancias = []
coordenadas_esferas = []
print('🟠 Vamos conquistar as esferas do dragão! 🟠')
print('--------------------------------------------------------------------------')
print('')
buffer = input()
while recebido != 'Todos os bits foram decodificados':
    if recebido == '------------------------------------':
        print(f'As coordenadas da {qtd_esferas}ª esfera do dragão são: ({coordenada_x}, {coordenada_y})\n')
        coordenadas_esferas.append([coordenada_x, coordenada_y])
        qtd_esferas += 1
        recebido = ''
    elif procurando == 'x':
        coordenada_x, binario_printado = processar_coordenada(ordem_matriz)
        print(f'Coordenada x da {qtd_esferas}ª esfera do dragão obtida pelo código binário {binario_printado}: {coordenada_x}')
        procurando = 'y'
    elif procurando == 'y':
        coordenada_y, binario_printado = processar_coordenada(ordem_matriz)
        print(f'Coordenada y da {qtd_esferas}ª esfera do dragão obtida pelo código binário {binario_printado}: {coordenada_y}')
        procurando = ''
    if procurando == '':
        recebido = input()
        procurando = 'x'
else:
    print(f'As coordenadas da {qtd_esferas}ª esfera do dragão são: ({coordenada_x}, {coordenada_y})\n')
    coordenadas_esferas.append([coordenada_x, coordenada_y])

print('--------------------------------------------------------------------------\n')
#construtor da matriz
matriz_final = []
for linha in range(ordem_matriz):
    linha_construtor = []
    for coluna in range(ordem_matriz):
        if [linha, coluna] in coordenadas_esferas:
            linha_construtor.append('☆')
        elif [linha, coluna] == coordenadas_goku:
            linha_construtor.append('G')
        else:
            linha_construtor.append('.')
    matriz_final.append(linha_construtor)
#printa matriz
for linha in range(ordem_matriz):
    linha_formatada = ' '.join(matriz_final[linha])
    print(linha_formatada)
print('')

#trajetoria
mensagem = f'Trajetória completa de Goku: ({coordenadas_goku[0]}, {coordenadas_goku[1]})'
while len(coordenadas_esferas) > 0:
    mais_proxima = esfera_mais_próxima(coordenadas_esferas, coordenadas_goku)
    coordenadas_goku = mais_proxima
    mensagem += f' -> ({mais_proxima[0]}, {mais_proxima[1]})'
    coordenadas_esferas.remove(mais_proxima)
print(mensagem)
print('Missão cumprida! Conseguimos todas as esferas do dragão!🟠🐉')
