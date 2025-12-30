qtd_grupos = int(input())

grupos = {}
#pega informação dos times de cada grupo, os times ficam em listas que estão associados a chaves de cada grupo
for i in range(1, qtd_grupos+1):
    times_do_grupo = []
    for time in range(1, 5):
        nome, pontuacao = input().split(' - ')
        infos = [int(pontuacao), nome]
        times_do_grupo.append(infos)
    #organiza da maior pontuacao pra menor
    times_do_grupo.sort(reverse=True)
    grupos[i] = times_do_grupo 

if qtd_grupos < 2 or (qtd_grupos % 2 != 0):
    print(f'Mas como que vamos fazer um torneio com {qtd_grupos} grupos Samir!?')
else:
    print('Roda os dados Samir!')
    #confrontos
    confrontos = []
    for embates in range(qtd_grupos//2):
        cruzamento = input().split(' x ')
        cruzamento[0] = int(cruzamento[0])
        cruzamento[1] = int(cruzamento[1])
        confrontos.append(cruzamento)
    #printa quem joga contra quem
    print('')
    for numero in range(len(confrontos)):
        #pega dos confrontos o grupo que deve ser o A e o B, e a partir da posição da lista de times, pega o primeiro e segundo lugar de cada grupo do cruzamento
        grupoA_primeiro = grupos[confrontos[numero][0]][0][1]
        grupoA_segundo = grupos[confrontos[numero][0]][1][1]
        grupoB_primeiro = grupos[confrontos[numero][1]][0][1]
        grupoB_segundo = grupos[confrontos[numero][1]][1][1]
        #printa os confrontos
        print(f'Confrontos chave {numero+1}:')
        print(f'{grupoA_primeiro} x {grupoB_segundo}')
        print(f'{grupoA_segundo} x {grupoB_primeiro}')
        print('')
    
    #rebaixados, printa baseado em quem é o ultimo por pontuaçao
    for numero in range(1, qtd_grupos+1):
        time_rebaixado = grupos[numero][3][1] 
        print(f'O time {time_rebaixado} ficou em último lugar em seu grupo e foi rebaixado!')

