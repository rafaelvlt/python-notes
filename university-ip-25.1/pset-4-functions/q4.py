#definição de funções
def fusao(primeiro,segundo, falhas):
    """retorna nome da fusão, e se teve sucesso ou não, nessa ordem, trabalha a fusão para qtd de falhas de cada"""
    nome = ''
    tipo = ''
    #casos especiais
    if (primeiro == 'Goten' and segundo == 'Trunks') or (primeiro == 'Trunks' and segundo == 'Goten'):
        nome = 'Gotenks'
        tipo = 'perfeita'
        return nome, tipo
    elif (primeiro == 'Goku' and segundo == 'Vegeta') or (primeiro == 'Vegeta' and segundo == 'Goku'):
        nome = 'Vegito'
        tipo = 'perfeita'
        return nome, tipo
    #para cada qtd de falhas
    if falhas == 0:
        #primeiro
        if len(primeiro) <= 4:
            parte1 = primeiro[0]
            nome += parte1
        else:
            parte1 = primeiro[0:dividir_e_arredondar(len(primeiro))]
            nome += parte1
        #segundo
        if len(segundo) == 3:
            parte2 = segundo[-2:]
            nome += parte2
        elif len(segundo) <= 4:
            parte2 = segundo[-3:]
            nome += parte2
        else:
            parte2 = segundo[-(dividir_e_arredondar(len(segundo)))+1:]
            nome += parte2
    elif falhas == 1:
        #primeiro modificado
        if len(primeiro) <= 4:
            parte1 = primeiro[0:2]
            nome += parte1
        else:
            parte1 = primeiro[0:dividir_e_arredondar(len(primeiro))+1]
            nome += parte1
        #segundo
        if len(segundo) == 3:
            parte2 = segundo[-2:]
            nome += parte2
        elif len(segundo) <= 4:
            parte2 = segundo[-3:]
            nome += parte2
        else:
            parte2 = segundo[-(dividir_e_arredondar(len(segundo)))+1:]
            nome += parte2
    elif falhas == 2:
        #primeiro passo modificado
        if len(primeiro) <= 4:
            parte1 = primeiro[0:2]
            nome += parte1
        else:
            parte1 = primeiro[0:dividir_e_arredondar(len(primeiro))]
            nome += parte1
        #segundo
        if len(segundo) <= 4:
            parte2 = segundo[-3:]
            nome += parte2
        else:
            parte2 = segundo[-(dividir_e_arredondar(len(segundo))):]
            nome += parte2
    #checa o tipo de fusao
    nome = nome.capitalize()
    parte1 = parte1.lower()
    parte2 = parte2.lower()
    if len(nome) <= 3:
        tipo = 'imperfeita'
    elif (parte1[-1] in 'aeiou' and parte2[0] in 'aeiou') or (parte1[-1] not in 'aeiou' and parte2[0] not in 'aeiou'):
        tipo = 'imperfeita'
    else:
        tipo = 'perfeita'
    
    return nome, tipo

def calcular_poder(nome):
    """calcula poder baseado no nome, retorna poder(int)"""
    poder = 2000
    if len(nome) == 4:
        return poder
    else:
        for qtd in range(4, len(nome)):
            if qtd < 8:
                poder += 250
        else:
            return poder

def dividir_e_arredondar(numero):
    """divide e arredonda pra cima se for numero quebrado(sinceramente não lembro se existe built-in)"""
    if numero % 2 == 0:
        return numero // 2
    else:
        return (numero + 1) // 2
#fim def de funções
#listas
herois = ['Gohan','Goku','Goten','Kuririn','Piccolo','Tenshinhan','Trunks','Uub','Vegeta','Yamcha']
viloes = ['Babidi','Baby','Broly','Buu','Cell','Cooler','Frieza','Hit','Janemba','Zamasu']
#variáveis
acabou = False
usados = []
resultado_fusao = ''
tipo_fusao = ''
pontos_herois = 0
pontos_viloes = 0
falhas = 0
invalido = False
while not acabou:
    nome1 = input()
    print(f"{nome1} se elege para participar da fusão!")
    nome2 = input()
    print(f"{nome2} se elege para participar da fusão!")
    #checa se há repetido!
    if nome1 in usados:
        print(f'{nome1} já participou de uma fusão. Fusão inválida.')
        invalido = True
    if nome2 in usados:
        print(f'{nome2} já participou de uma fusão. Fusão inválida.')
        invalido = True
    #checa se ambos são do mesmo tipo, se não printa erro
    if not invalido:
        if (nome1 in herois and nome2 in viloes) or (nome1 in viloes and nome2 in herois):
            print("Heróis e vilões não se misturam! As auras dos dois participantes são incompatíveis.")
            invalido = True
    #herois
    if (nome1 in herois and nome2 in herois) and not invalido:
        while tipo_fusao != 'perfeita' and falhas < 3:
            resultado_fusao, tipo_fusao = fusao(nome1, nome2, falhas)
            if tipo_fusao != 'perfeita':
                falhas += 1
                print(f'A sincronização foi um desastre... {resultado_fusao} é uma fusão imperfeita!')
        else:
            if tipo_fusao == 'imperfeita':
                print("Aparentemente essa combinação é incompatível...")
            else:
                print(f"Fusão realizada com sucesso! {resultado_fusao} entra em combate para derrotar o exército de vilões!")
                usados.append(nome1)
                usados.append(nome2)
                pontos_herois += calcular_poder(resultado_fusao)
    #viloes
    elif (nome1 in viloes and nome2 in viloes) and not invalido:
        #loopa fusao até ver que é imcompatível ou falhar
        while tipo_fusao != 'perfeita' and falhas < 3:
            resultado_fusao, tipo_fusao = fusao(nome1, nome2, falhas)
            if tipo_fusao != 'perfeita':
                falhas += 1
                print(f"A sincronização foi um desastre... {resultado_fusao} é uma fusão imperfeita!")
        else:
            #fusao imperfeita
            if tipo_fusao == 'imperfeita':
                print("Aparentemente essa combinação é incompatível...")
            else: #fusao perfeita
                print(f"Fusão realizada com sucesso! {resultado_fusao} entra em combate com sede de destruir Satan City!")
                usados.append(nome1)
                usados.append(nome2)
                pontos_viloes += calcular_poder(resultado_fusao)
    #decide vencedor e termina loop
    if pontos_herois > 8000:
        print("O poder dos heróis... É mais de 8000! Eles derrotam os vilões e conseguem selar o portal.")
        acabou = True
    elif pontos_viloes > 8000:
        print("Os vilões são fortes demais! Satan City está em apuros!")
        acabou = True
    #reseta variáveis
    invalido = False
    falhas = 0
    tipo_fusao = ''
