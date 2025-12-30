print('Go! Go! Power Rangers!')
zords = input()
zords_e_niveis = zords.split('-') #retorna uma lista de todos elementos separados entre hífens
tamanho_lista = len(zords_e_niveis)
zordst1 = []
zordst2 = []
zordst3 = []
zordst1_niveis = []
zordst2_niveis = []
zordst3_niveis = []
terminar_luta = False

for elemento in zords_e_niveis:
    if elemento == 'robocin':
        print('Os rangers encontraram o zord lendário!!!! O Robocin!!!! Eles não precisam mais de outros zords!')
        terminar_luta = True

if not terminar_luta:
    #itera sobre os níveis, classificando os zords de acordo com nível e colocando em listas rankeadas
    #a lista de níveis está com mesmos índices da lista de nomes do rank
    for indice in range(1, tamanho_lista, 2):
        if int(zords_e_niveis[indice]) > 30:
            zordst1.append(zords_e_niveis[indice-1])
            zordst1_niveis.append(int(zords_e_niveis[indice]))
        elif int(zords_e_niveis[indice]) > 10:
            zordst2.append(zords_e_niveis[indice-1])
            zordst2_niveis.append(int(zords_e_niveis[indice]))
        elif int(zords_e_niveis[indice]) <= 10:
            zordst3.append(zords_e_niveis[indice-1])
            zordst3_niveis.append(int(zords_e_niveis[indice]))
    
    #ordenação dos zords por bubblesort, que compara elementos adjacentes e troca os de lugar, nesse caso em forma crescente
    #como os elementos são movidos em pares, a lista deve ser rodado pela qtd de vezes tamanho-1
    #zords tipo 1
    for tamanho in range(len(zordst1_niveis)): #loopa tamanho-1 vezes a lista
            for indice in range(len(zordst1_niveis)-1, 0, -1): #loopa do fim da lista até o inicio
                if zordst1_niveis[indice]>zordst1_niveis[indice-1]: #caso o segundo elem seja maior que o primeiro, troca os dois de lugar
                    #troca o nível e o nome de lugar para um estar mapeado ao outro da mesma forma, para isso precisa de variáveis temporárias para guardar o valor quando trocaddo
                    tempnivel = zordst1_niveis[indice] 
                    tempnome = zordst1[indice]
                    #realizando troca
                    zordst1_niveis[indice] = zordst1_niveis[indice-1]
                    zordst1_niveis[indice-1] = tempnivel
                    zordst1[indice] = zordst1[indice-1]
                    zordst1[indice-1] = tempnome
    #zords tipo 2
    for tamanho in range(len(zordst2_niveis)): 
            for indice in range(len(zordst2_niveis)-1, 0, -1): 
                if zordst2_niveis[indice]>zordst2_niveis[indice-1]: 
                    tempnivel = zordst2_niveis[indice]
                    tempnome = zordst2[indice]
                    zordst2_niveis[indice] = zordst2_niveis[indice-1]
                    zordst2_niveis[indice-1] = tempnivel
                    zordst2[indice] = zordst2[indice-1]
                    zordst2[indice-1] = tempnome
    #zords tipo 3
    for tamanho in range(len(zordst3_niveis)): 
            for indice in range(len(zordst3_niveis)-1, 0, -1): 
                if zordst3_niveis[indice]>zordst3_niveis[indice-1]: 
                    tempnivel = zordst3_niveis[indice]
                    tempnome = zordst3[indice]
                    zordst3_niveis[indice] = zordst3_niveis[indice-1]
                    zordst3_niveis[indice-1] = tempnivel
                    zordst3[indice] = zordst3[indice-1]
                    zordst3[indice-1] = tempnome
    #relatorio final para cada caso
    #ranger vermelho e verde
    if len(zordst1) >= 2:
        print(f'Zord do Ranger Vermelho: {zordst1[0]}')
        print(f'Zord do Ranger Verde: {zordst1[1]}')
    elif len(zordst1) == 1:
        print(f'Zord do Ranger Vermelho: {zordst1[0]}')
        print(f'Ranger Verde ficou sem zord!')
    else:
        print(f'Ranger Vermelho ficou sem zord!')
        print(f'Ranger Verde ficou sem zord!')
    #ranger rosa e preto
    if len(zordst2) >= 2:
        print(f'Zord da Ranger Rosa: {zordst2[0]}')
        print(f'Zord do Ranger Preto: {zordst2[1]}')
    elif len(zordst2) == 1:
        print(f'Zord da Ranger Rosa: {zordst2[0]}')
        print(f'Ranger Preto ficou sem zord!')
    else:
        print(f'Ranger Rosa ficou sem zord!')
        print(f'Ranger Preto ficou sem zord!')
    #ranger azul e amarela
    if len(zordst3) >= 2:
        print(f'Zord do Ranger Azul: {zordst3[0]}')
        print(f'Zord da Ranger Amarela: {zordst3[1]}')
    elif len(zordst3) == 1:
        print(f'Zord do Ranger Azul: {zordst3[0]}')
        print(f'Ranger Amarela ficou sem zord!')
    else:
        print(f'Ranger Azul ficou sem zord!')
        print(f'Ranger Amarela ficou sem zord!')
    
    #zords por tipo
    if len(zordst1) > 0:
        print('Zords do tipo 1: ', end='')
        for indice in range(len(zordst1)):
            if indice != (len(zordst1) -1):
                print(f'{zordst1[indice]}', end=', ')
            else:
                print(f'{zordst1[indice]}')
    else:
        print('Não temos nenhum zord do tipo 1 :(')

    if len(zordst2) > 0:
        print('Zords do tipo 2: ', end='')
        for indice in range(len(zordst2)):
            if indice != len(zordst2) - 1:
                print(f'{zordst2[indice]}', end=', ')
            else:
                print(f'{zordst2[indice]}')
    else:
        print('Não temos nenhum zord do tipo 2 :(')

    if len(zordst3) > 0:
        print('Zords do tipo 3: ', end='')
        for indice in range(len(zordst3)):
            if indice != len(zordst3) - 1:
                print(f'{zordst3[indice]}', end=', ')
            else:
                print(f'{zordst3[indice]}')
    else:
        print('Não temos nenhum zord do tipo 3 :(')

    if len(zordst1) >= 2 and len(zordst2) >= 2 and len(zordst3) >= 2:
        print('Os Rangers estão prontos para montar o Megazord e derrotar Rita!')
    else:
        print('Ai ai ai, essa não!! Não temos zords suficientes para formar o Megazord! Os ranger não vão conseguir derrotar Rita!')
