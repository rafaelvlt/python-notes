def forja(lista_de_armas, lista_de_aprimoramentos):
    """percorre a lista de armas e envia cada uma para a função bigorna, que realiza
    os aprimoramentos e retorna uma arma final, arma final essa que é concatenada em uma lista de armas finais
    e quando nao há mais armas para dar upgrade, é enviada para a chamada de função"""
    #condição de término
    if len(lista_de_armas) == 0:
        return []
    
    #listas mutáveis
    arma_atual = lista_de_armas[0]
    resto_lista = lista_de_armas[1:]
    aprimoramento_atual = lista_de_aprimoramentos[0]
    resto_aprimoramento = lista_de_aprimoramentos[1:]

    #envia para o aprimoramento
    arma_inicial = []
    arma_final = bigorna(arma_atual, aprimoramento_atual, arma_inicial)
    print(f'{arma_final[0]} aprimorado!')
    #loop recursivo
    return [arma_final] + forja(resto_lista, resto_aprimoramento)
    

def bigorna(arma_atual, aprimoramentos, arma_inicial):
    """itera recursivamente sobre a lista de aprimoramentos aplicando eles a arma específica
    retorna a arma em seu estado final após aprimoramentos"""
    arma_atual[2] = int(arma_atual[2])
    if len(aprimoramentos) == 0:
        return arma_atual
    
    afinidades = ['físico', 'mágico', 'fogo', 'dourado', 'oculto']
    #se acabou de chegar na bigorna, vira a arma_inicial
    aprimoramento_atual = aprimoramentos[0]
    resto_aprimoramentos = aprimoramentos[1:]
    #separa atributos, tipo, afinidade extra.
    tipo_da_arma = arma_atual[1]
    afinidade_extra = arma_atual[3]
    atributos_base = arma_atual[4:]

    #checa se é uma subslista, se sim itera sobre ela nessa mesma função, recursivamente
    if isinstance(aprimoramento_atual, list):
        #arma antes da troca de afinidades, para caso de reversão
        arma_inicial = arma_atual.copy()
        #troca de atributo
        if afinidades.index(afinidade_extra) <= 3:
            afinidade_nova = afinidades[afinidades.index(afinidade_extra)+1]
            arma_atual[3] = afinidade_nova 
        else:
            arma_atual[3] = afinidades[0]
        arma_atual = bigorna(arma_atual, aprimoramento_atual, arma_inicial)
        afinidade_extra = arma_atual[3]
    #upgrade para cada tipo de atributo
    if aprimoramento_atual == 'S':
        if 'força' in atributos_base:
            arma_atual[2] += 1
        if afinidade_extra == 'fogo':
            arma_atual[2] += 1
    if aprimoramento_atual == 'D':
        if 'destreza' in atributos_base:
            arma_atual[2] += 1
        if afinidade_extra == 'físico':
            arma_atual[2] += 1
    if aprimoramento_atual == 'I':
        if 'inteligência' in atributos_base:
            arma_atual[2] += 1
        if afinidade_extra == 'mágico':
            arma_atual[2] += 1
    if aprimoramento_atual == 'F':
        if 'fé' in atributos_base:
            arma_atual[2] += 1
        if afinidade_extra =='dourado':
            arma_atual[2] += 1
    if aprimoramento_atual == 'A':
        if 'arcano' in atributos_base:
            arma_atual[2] += 1
        if afinidade_extra == 'oculto':
            arma_atual[2] += 1
    #aprimoramneto se é do mesmo tipo que a arma
    if aprimoramento_atual == '+' and tipo_da_arma == 'normal':
        arma_atual[2] += 3
    if aprimoramento_atual == '-' and tipo_da_arma == 'especial':
        arma_atual[2] += 5

    #reversão
    if aprimoramento_atual == 'R':
        print("Hmm, não acho que isso vai funcionar...")
        print(f'{arma_atual[0]}: {arma_atual[2]} -> {arma_inicial[2]}') 
        print(f'Afinidade revertida para {arma_inicial[3]}')
        return bigorna(arma_inicial, resto_aprimoramentos, arma_inicial)
    
    #loop recursivo
    return bigorna(arma_atual, resto_aprimoramentos, arma_inicial)
 
def receber_armas(lista):
    """recebe dados de cada arma utilizando recursão, retorna uma lista de listas com armas em cada entrada"""
    entrada = input()
    if entrada == 'finalizar':
        return lista
    else:
        entrada = entrada.split(' - ')
        lista.append(entrada)
        return receber_armas(lista)
def receber_aprimoramentos(aprimoramentos, quantidade):
    """recebe os aprimoramentos para cada arma utilizando recursão, retorna uma lista de listas com aprimoramentos para cada arma"""
    if quantidade == 0:
        return aprimoramentos
    else:
        entrada = eval(input())
        aprimoramentos.append(entrada)
        return receber_aprimoramentos(aprimoramentos, quantidade-1)
def inventario(armas, fogo, fe, normal):
    """imprime o inventário, retorna qtd de armas de fogo, armas de fé e armas de outros tipos, nessa ordem"""
    arma_atual = armas[0]
    resto_armas = armas[1:]
    #prints
    print(f'- {arma_atual[0]}: {arma_atual[2]}')
    print(f'- afinidade: {arma_atual[3]}')
    if arma_atual[3] == 'fogo':
        print('Fogo... é uma das fraquezas da Malenia!!!')
        fogo += 1
    elif arma_atual[3] == 'dourado':
        print('É, não acho que uma arma de fé vá me ajudar muito...')
        fe += 1
    else:
        normal += 1

    #caso base
    if len(resto_armas) == 0:
        return fogo, fe, normal
    #caso recursivo
    else:
        return inventario(resto_armas, fogo, fe, normal)

#fim da declaração de funções

#inicio do programa
print("Não aguento mais morrer para a Malenia, Blade of Miquella...\nVou refazer minha build!\n")

#lista mutáveis e variáveis
lista_de_armas = []
lista_de_aprimoramentos = []
armas_finais = []
armas_fogo = 0
armas_fe = 0
armas_normal = 0
#chamadas de funções para recebimento e aprimoramento das armas
lista_de_armas = receber_armas(lista_de_armas)
lista_de_aprimoramentos = receber_aprimoramentos(lista_de_aprimoramentos, len(lista_de_armas))
armas_finais = forja(lista_de_armas, lista_de_aprimoramentos)

#imprime inventário e pega tipo de armas
print("Inventário:")
armas_fogo, armas_fe, armas_normal = inventario(armas_finais, armas_fogo, armas_fe, armas_normal)
print('')

#mensagem final
if armas_fogo > armas_fe and armas_fogo > armas_normal:
    print('Muitas armas de fogo, ela não vai ter chance!')
elif armas_fe > armas_fogo and armas_fe > armas_normal:
    print('Acho que vou ter que refazer meus aprimoramentos...')
else:
    print('Analisando meu inventário agora, acho que consigo vencer, pode vir, Malenia, Blade of Miquella!!')
