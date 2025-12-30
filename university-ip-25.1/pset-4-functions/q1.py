#declaração de funções
def calcular_distancia(coordenadas_do_objeto):
    distancia = 0.0
    distancia = (coordenadas[0]**2 + coordenadas_do_objeto[1]**2)**(1/2)
    return distancia

#fim da declaração de funções

#variáveis
qtd_objetos_detectados = int(input())
esferas = 0
distancia_prioritario = 99999999999999999999
ordem_deteccao = 0
#variáveis placeholders antes de serem adicionadas na lista
nome = ''
coordenadas = []
distancia = 0

#loop principal
for index in range(qtd_objetos_detectados):
    #pega o nome e vê se é algum especial
    nome = input()
    if nome != 'esfera':
        if nome == 'rocha':
            print("Radar: Rocha detectada! Bulma resmunga: 'Só um pedregulho cósmico... Sem valor para mim!'")
        elif nome == 'árvore':
            print("Radar: Árvore à vista! Bulma comenta: 'Interessante, mas não brilha como uma esfera. Próximo alvo!'")
        elif nome == 'nave':
            print("Radar: Sinal de nave! Bulma alerta: 'Pode ser Pilaf ou a Patrulha Vermelha! Melhor ficar atenta, mas o foco são as esferas!'")
        else:
            print(f"Radar: Detectado um(a) {nome}. Não parece ser uma esfera... Continuando a busca.")
    else:
        esferas += 1

    #coordenadas e calculo de distancia por função
    coordenadas.append(int(input()))
    coordenadas.append(int(input()))

    distancia = calcular_distancia(coordenadas)

    #checa prioridade de esferas
    if nome == 'esfera':
        if distancia < distancia_prioritario:
            distancia_prioritario = distancia
            ordem_deteccao = index + 1
    
    #reseta coordenadas
    coordenadas = []

#prints finais
if esferas >= 1:
    print(f"ALVO PRIORITÁRIO: Esfera | Distância: {distancia_prioritario:.2f}m | Detecção Original: {ordem_deteccao}°")
else:
    print("Radar varreu a área. Nenhuma esfera do dragão à vista desta vez!")
