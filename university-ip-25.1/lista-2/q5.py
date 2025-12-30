quantidade_atletas = int(input())
atleta_1 = ''
pontos_1_suspeito = 0
atleta_2 = ''
pontos_2_suspeito = 0
atleta_3 = ''
pontos_3_suspeito = 0

for i in range(1, quantidade_atletas+1):
    pontos = 0
    vogais = 0
    escondendo = True

    nome_atleta = input()
    posicao = int(input())
    ranking = int(input())
    velocidade = float(input())

    
    if quantidade_atletas > 2:
        print(f'COMEÇANDO A {i}ª RODADA DE INVESTIGAÇÃO')
        #vogais
        for i in nome_atleta:
            if i in 'aeiouAEIOU':
                vogais += 1
        if (vogais % 2) == 0:
            pontos += 10
        else:
            pontos += 5
        #posição
        if posicao >= 45 and posicao <= 135:
            pontos += 10
            escondendo = False
            print(f'{nome_atleta} estava em posição estratégica para pegar o troféu... muito suspeito!')
        elif posicao >= 225 and posicao <= 315:
            pontos += 5
        else:
            pontos += 2

        #ranking
        if ranking <= 10:
            pontos += 10
            escondendo = False
            print(f'{nome_atleta} é um dos melhores do mundo... e também um dos principais suspeitos!')
        elif ranking <= 50:
            pontos += 5
        else:
            pontos += 2

        #velocidade
        if velocidade > 140:
            pontos += 10
            escondendo = False
            print(f'Alta velocidade detectada! {nome_atleta} pode ter fugido rapidamente com o troféu!')
        elif velocidade >= 100:
            pontos += 5
        else:
            pontos += 2
        
        if escondendo == True:
            print(f'Hum, esse {nome_atleta} sei não viu... Deve tá escondendo alguma coisa.')
        
        #suspeitos por pontos, sempre que um suspeito ultrapassa outro, o outro eh mandado pra baixo
        if pontos > pontos_1_suspeito:
            atleta_2 = atleta_1
            pontos_2_suspeito = pontos_1_suspeito
            atleta_1 = nome_atleta
            pontos_1_suspeito = pontos
        elif pontos > pontos_2_suspeito:
            atleta_3 = atleta_2
            pontos_3_suspeito = pontos_2_suspeito
            atleta_2 = nome_atleta
            pontos_2_suspeito = pontos
        elif pontos > pontos_3_suspeito:
            atleta_3 = nome_atleta
            pontos_3_suspeito = pontos
    else:
        if atleta_1 == '':
            atleta_1 = nome_atleta
        elif atleta_2 == '':
            atleta_2 = nome_atleta
 

#fora do loop
else:
    if quantidade_atletas == 2:
        print(f'Caso encerrado: {atleta_1} e {atleta_2} roubaram o troféu!')
    elif quantidade_atletas == 1:
        print(f'Não há dúvidas... {atleta_1} é o culpado!')
    else:
        print('\nRESULTADOS DAS INVESTIGAÇÕES:\n')
        print(f'Os 3 principais suspeitos são:\n1. {atleta_1} - {pontos_1_suspeito} pontos\n2. {atleta_2} - {pontos_2_suspeito} pontos\n3. {atleta_3} - {pontos_3_suspeito} pontos\n')
        #quem roubou
        if pontos_1_suspeito == pontos_2_suspeito:
            print(f'Que absurdo... {atleta_1} e {atleta_2} roubaram o troféu juntos!')
        else:
            print(f'Mistério resolvido: O culpado é {atleta_1}! Ele roubou o troféu de Calderano.')
