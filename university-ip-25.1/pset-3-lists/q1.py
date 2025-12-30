lista_pronta = False
lista_de_compras = []
while not lista_pronta:
    instrucao = input()

    if instrucao == 'Anotar ingrediente':
        ingrediente = input()
        lista_de_compras.append(ingrediente)

    elif instrucao == 'Ingrediente Urgente!':
        ingrediente = input()
        lista_de_compras.insert(0, ingrediente)

    elif instrucao == 'Saci disse que já tem':
        ingrediente = input()
        #remove a primeira instancia do item dito
        lista_de_compras.remove(ingrediente)

    elif instrucao == 'Saci trocou a ordem':
        index_primeiro_item = int(input())
        index_segundo_item = int(input())
        #armazena os itens dados em variáveis
        primeiro_item = lista_de_compras[index_primeiro_item]
        segundo_item = lista_de_compras[index_segundo_item]
        #realiza a troca 
        lista_de_compras[index_primeiro_item] = segundo_item
        lista_de_compras[index_segundo_item] = primeiro_item

    elif instrucao == 'Organizar a lista':
        #recebe os nomes dos ingredientes para a troca
        ingrediente1 = input()
        ingrediente2 = input()
        #busca o index deles pelo nome
        index_primeiro_item = lista_de_compras.index(ingrediente1)
        index_segundo_item = lista_de_compras.index(ingrediente2)
        #armazena os itens dados em variáveis
        primeiro_item = lista_de_compras[index_primeiro_item]
        segundo_item = lista_de_compras[index_segundo_item]
        #realiza a troca 
        lista_de_compras[index_primeiro_item] = segundo_item
        lista_de_compras[index_segundo_item] = primeiro_item

    elif instrucao == 'Deixar para depois':
        ingrediente = input()
        #remove o ingrediente
        lista_de_compras.remove(ingrediente)
        #adiciona ao final da lista
        lista_de_compras.append(ingrediente)
    elif instrucao == 'Ler a lista para a vovó':
        #itera sobre todos itens da lista e se for o último, não adiciona vírgula e espaço
        for item in lista_de_compras:
            if item != lista_de_compras[-1]:
                print(f'{item}', end=', ')
            else:
                print(f'{item}')
    elif instrucao == 'E por hoje é só, pessoal!':
        lista_pronta = True

#relatório final
print('Pronto, vovó! A lista de compras para o bolo de Narizinho está pronta. Podemos ir ao mercado. A lista final é: ', end='')
for item in lista_de_compras:
    if item != lista_de_compras[-1]:
        print(f'{item}', end=', ')
    else:
        print(f'{item}')
