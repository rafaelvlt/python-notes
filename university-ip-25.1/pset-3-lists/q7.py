#locais validos
locais_validos = ['Torre Eiffel', 'Museu do Louvre', 'Catacumbas de Paris', 'Biblioteca Nacional', 'Galeria Lafayette', 'Parque dos Príncipes', 'Catedral de Notre-Dame', 'Jardim de Luxemburgo', 'Padaria Dupain Cheng']
horarios_mapeados = ['09:00 às 23:00', '08:00 às 18:00', '10:00 às 20:00', '07:00 às 22:00', '10:00 às 21:00', '06:00 às 23:00', '08:00 às 18:30', '07:00 às 19:00', '04:00 às 20:00']
horarios_formatados = []
for i in range(len(horarios_mapeados)):
    horario = horarios_mapeados[i]
    lista_horario_formatada = [float(horario[:2] + horario[3:5]),float(horario[9:11]+horario[12:14])]
    horarios_formatados.append(lista_horario_formatada)
seguranca_locais = ['Média', 'Alta', 'Baixa', 'Média', 'Alta', 'Baixa', 'Alta', 'Média', 'Baixa']
#faz a lista
lista_de_suspeitos = []
for suspeito in range(6):
    inputbruto = input()
    linha_suspeito = inputbruto.split(' - ')
    lista_de_suspeitos.append(linha_suspeito)

#variáveis de suspeitos
locais_invalidos = []
fora_horario = []
seguranca_baixa = []
presença_testemunhas = []
sem_suspeitos = True
mensagem_printada = 'Poxa vida, todos os àlibis parecem válidos… mas algo continua errado'
ignorar = False

for i in range(6):
    #checa se há algun local invalido entre os suspeitos, se houver ignora os próximos ifs checando outras coisas
    if lista_de_suspeitos[i][2] not in locais_validos:
        locais_invalidos.append(lista_de_suspeitos[i])
        ignorar = True
#caso haja apenas um local invalido printa a mensagem
if len(locais_invalidos) == 1:
    print(f'Esse lugar {locais_invalidos[0][2]} nem existe! {locais_invalidos[0][0]} com certeza foi akumatizado!')
elif len(locais_invalidos) > 1:
    #caso haja mais de um, separa os suspeitos em listas distintas para permitir o sort
    suspeitos_nomes = [sus[0] for sus in locais_invalidos]
    suspeitos_locais = [sus[2] for sus in locais_invalidos]
    #ordena cada lista
    suspeitos_nomes.sort()
    suspeitos_locais.sort()
    #printa
    nomes_msg = ", ".join(suspeitos_nomes)
    locais_msg = ", ".join(suspeitos_locais)
    print(f'{locais_msg} nem existem! {nomes_msg} estão mentindo!')


 #codigo para checar se o horario está invalido                          
if not ignorar:
    for i in range(6):
        index = locais_validos.index(lista_de_suspeitos[i][2])
        horario = lista_de_suspeitos[i][1]
        horario_suspeito = float(horario[:2] + horario[3:5])
        #horário dado no input é testado para os horários validos formatados para float
        if not (horario_suspeito >= horarios_formatados[index][0] and horario_suspeito <= horarios_formatados[index][1]):
            fora_horario.append(lista_de_suspeitos[i])
            ignorar = True
    if len(fora_horario) == 1:
        print(f'{fora_horario[0][2]} nem estava aberto às {fora_horario[0][1]}! {fora_horario[0][0]} recebeu memórias falsas!')
    elif len(fora_horario) > 1:
        #separa em listas diferentes para o sort
        suspeitos_nomes = [sus[0] for sus in fora_horario]
        suspeitos_locais = [sus[2] for sus in fora_horario]
        #dá o sort
        suspeitos_nomes.sort()
        suspeitos_locais.sort()
        #mensagem final
        nomes_msg = ", ".join(suspeitos_nomes)
        locais_msg = ", ".join(suspeitos_locais)
        print(f'{locais_msg} estavam fechados nesse horário! {nomes_msg} podem ter sido manipulados pelo Hawk Moth!')

#código para ver se a segurança era baixa
if not ignorar:
    for i in range(6):
        #loopa toda lista de suspeitos e vê se o local deles tem segurança baixa, caso sim, são adicionados a lista de segurança baixa
        index = locais_validos.index(lista_de_suspeitos[i][2])
        if seguranca_locais[index] == 'Baixa':
            seguranca_baixa.append(lista_de_suspeitos[i])
            ignorar = True
    #prints para caso haja apenas 1 em segurança baixa
    if len(seguranca_baixa) == 1:
        print(f'{seguranca_baixa[0][0]} estava em um local de segurança baixa... Ele pode ter mentido!')
    elif len(seguranca_baixa) > 1: #print caso haja vários
        suspeitos_nomes = [sus[0] for sus in seguranca_baixa]
        suspeitos_nomes.sort()
        nomes_msg = ", ".join(suspeitos_nomes)
        print(f'{nomes_msg} estavam em locais de segurança baixa... Eles podem estar forjando um álibi!')


#código para sem testemunhas
if not ignorar:
    sem_testemunhas = []
    for suspeito in lista_de_suspeitos:
        if suspeito[3] == 'nenhuma':
            sem_testemunhas.append(suspeito)
            ignorar = True

    #código para printar para cada caso sem testemunha
    if len(sem_testemunhas) == 1:
        print(f'{sem_testemunhas[0][0]} não teve testemunha para confirmar o álibi. É o mais suspeito até agora.')
    elif len(sem_testemunhas) == 6:
        print('Ninguém viu ninguém… estranho!!')
    elif len(sem_testemunhas) > 1:
        suspeitos_nomes = [sus[0] for sus in sem_testemunhas]
        suspeitos_nomes.sort()
        nomes_msg = ", ".join(suspeitos_nomes)
        print(f'{nomes_msg} não foram confirmados por ninguém. O Hawk Moth pode vir atrás deles de novo')
if not ignorar:
    print('Poxa vida, todos os àlibis parecem válidos… mas algo continua errado')
