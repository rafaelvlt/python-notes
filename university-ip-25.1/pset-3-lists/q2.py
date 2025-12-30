caçada_terminou = False
#parametros iniciais
nivel_inicial = int(input())
qtd_criaturas = int(input())
exercito = []
nivel = nivel_inicial
combates_realizados = 0
while not caçada_terminou:
    nome_criatura = input()
    nivel_criatura = int(input())

    #caso de vitóriam nivel da criatura menor que Jin-Woo
    if nivel_criatura < nivel:
        resposta = input()
        #caso resposta for Erga-se, adiciona, caso não foi, não faz nada
        if resposta == 'Erga-se':
            exercito.append(nome_criatura)
            nivel += nivel_criatura//3
        combates_realizados += 1 
    elif nivel_criatura >= nivel:
        #termina caçada e printa a derrota
        caçada_terminou = True
        print(f'Jin-Woo foi derrotado por {nome_criatura}...')

    if combates_realizados == qtd_criaturas:
        #fim de loop
        caçada_terminou = True
        print('Jin-Woo sobreviveu à caçada, um verdadeiro Monarca das Sombras mesmo!')

#relatorio final
print('===== Exército das Sombras de Jin-Woo =====')
if len(exercito) == 0:
    print('Jin-Woo não conseguiu formar seu exército...')
else:
    #cria lista de criaturas já contabilizadas para não serem imprimidas 2x
    criatura_contabilizada = []
    for criatura in exercito:
        if criatura not in criatura_contabilizada:
            #se a criatura não for contabilizada antes, printa no formato correto, vendo quantas vezes ela aparece com .count()
            print(f'{criatura}: {exercito.count(criatura)}')
            criatura_contabilizada.append(criatura)
            


