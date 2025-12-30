alfabeto_padrao = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alfabeto_modificado = ['k', 'q', 'f', 'm', 'x', 'e', 't', 'z', 'r', 'h', 'v', 'n', 'd', 'l', 'j', 'a', 's', 'u', 'y', 'b', 'g', 'w', 'p', 'o', 'i', 'c']

qtd_times = int(input())
equipes = []
equipe_inimiga = [110, 'general kregg', 100, 'conquista', 90, 'anissa']
teen_team = ['rex splode', 'duplikate', 'atom eve', 'robot']

for time in range(qtd_times):
    equipes.append([])

#loop de acao até ser recebido fim
times_terminaram = False
while not times_terminaram:
    acao = input()
    if acao == 'adicionar':
        print('Quem será o próximo integrante do time?')
        heroi = input()
        index_time = int(input())

        #lógica para decodificar nome do heroi
        heroi_codificado = heroi.split(' - ')
        nome_decodificado = ''
        for letra in heroi_codificado[0]:
            if letra in alfabeto_modificado:
                nome_decodificado += alfabeto_padrao[alfabeto_modificado.index(letra)]
            else:
                nome_decodificado += letra
        heroi_decodificado = [nome_decodificado, heroi_codificado[1]]
        #check do teen team
        if heroi_decodificado[0] in teen_team:
            if heroi_decodificado[0] == 'rex splode':
                print('Eu vou te detonar!')
            elif heroi_decodificado[0] == 'atom eve':
                print('Eu reescrevo a matéria... incluindo a SUA.')
            elif heroi_decodificado[0] == 'duplikate':
                print('Quantas de mim você acha que consegue lidar?')
            elif heroi_decodificado[0] == 'robot':
                print('Minha lógica diz que você vai perder.')
        #adiciona a equipe selecionada
        equipes[index_time].append(int(heroi_decodificado[1]))
        equipes[index_time].append(heroi_decodificado[0])
        
    elif acao == 'metamorfo':
        print('Atenção!!! Metamorfo encontrado, quem deverá ser removido do time?')
        heroi_metamorfo = input()
        #loop para busca e remoção do heroi específico
        for i in range(len(equipes)):
            for j in range(len(equipes[i])):
                if equipes[i][j] == heroi_metamorfo:
                    index1 = i
                    index2 = j
        else:
            equipes[index1].pop(index2)
            equipes[index1].pop(index2-1)
            #adicionar novamente      
            print('Quem você gostaria de colocar no lugar?')          
            heroi = input()
            index_time = int(input())

            #lógica para decodificar nome do heroi
            heroi_codificado = heroi.split(' - ')
            nome_decodificado = ''
            for letra in heroi_codificado[0]:
                if letra in alfabeto_modificado:
                    nome_decodificado += alfabeto_padrao[alfabeto_modificado.index(letra)]
                else:
                    nome_decodificado += letra
            heroi_decodificado = [nome_decodificado, heroi_codificado[1]]
            #check do teen team
            if heroi_decodificado[0] in teen_team:
                if heroi_decodificado[0] == 'rex splode':
                    print('Eu vou te detonar!')
                elif heroi_decodificado[0] == 'atom eve':
                    print('Eu reescrevo a matéria... incluindo a SUA.')
                elif heroi_decodificado[0] == 'duplikate':
                    print('Quantas de mim você acha que consegue lidar?')
                elif heroi_decodificado[0] == 'robot':
                    print('Minha lógica diz que você vai perder.')
            #adiciona a equipe selecionada
            equipes[index_time].append(int(heroi_decodificado[1]))
            equipes[index_time].append(heroi_decodificado[0])
    elif acao == 'FIM':
        times_terminaram = True
#soma de poder
somatorios_times = []
for time in range(len(equipes)):
    somatorio= 0
    for integrante in range(0, len(equipes[time]), 2):
        somatorio += equipes[time][integrante]
    somatorios_times.append(somatorio)
#ver se algum time é o teen team
tt_integrantes = 0
for time in range(len(equipes)):
    for integrante in range(len(equipes[time])):
        if equipes[time][integrante] in teen_team:
            tt_integrantes += 1
            index_tt = time
    if tt_integrantes == 4:
        print('O teen team esta completo, Cecil esta muito contente!')
        somatorios_times[index_tt] *= 1.1
        for membro in range(0, len(equipes[index_tt]), 2):
            equipes[index_tt][membro] *= 1.1
    tt_integrantes = 0


#escolha de time e ordenamento por bubblesort
melhor_time = equipes[somatorios_times.index(max(somatorios_times))]
for tamanho in range(len(melhor_time)//2): #loopa pela metade do tamanho da lista vezes
    for indice in range(len(melhor_time)-2, 0, -2):#fim da lista até o inicio
        if melhor_time[indice] > melhor_time[indice-2]:
            temppoder = melhor_time[indice] 
            tempnome = melhor_time[indice+1]
            #realizando troca
            melhor_time[indice] = melhor_time[indice-2]
            melhor_time[indice-2] = temppoder
            melhor_time[indice+1] = melhor_time[indice-1]
            melhor_time[indice-1] = tempnome
if len(melhor_time)//2 == 1:
    print(f'Aqui está o poderoso time da terra: {melhor_time[1]}')
    qtd_batalhas = 1
elif len(melhor_time)//2 == 2:
    print(f'Aqui está o poderoso time da terra: {melhor_time[1]}, {melhor_time[3]}')
    qtd_batalhas = 2
else:
    print(f'Aqui está o poderoso time da terra: {melhor_time[1]}, {melhor_time[3]}, {melhor_time[5]}')
    qtd_batalhas = 3
#batalha
vitorias_terra = 0
vitorias_viltrumitas = 0
rodada = 1
for i in range(0,qtd_batalhas*2, 2):
        print(f'{rodada} Duelo: {melhor_time[i+1]} X {equipe_inimiga[i+1]}')
        if melhor_time[i] > equipe_inimiga[i]:
            vitorias_terra += 1
        else:
            vitorias_viltrumitas += 1
        rodada += 1
if vitorias_terra > vitorias_viltrumitas:
    print('A terra venceu!')
else:
    print('Infelizmente o imperio viltrumita conquistou a terra!')
