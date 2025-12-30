#definição de função
def partida(time1_info, time2_info, artilheiros):
    """simula uma partida, recebe informações de ambos os times e os artilheiros, e retorna o vencedor, com motivo(vitoria ou empate, por sg) e também a artilharia"""
    gols_time1, gols_time2 = 0, 0
    
    entrada_gol = input()
    while entrada_gol != "FIM":
        jogador, time = entrada_gol.split(" - ")
        print(f"Gol do {time}, {jogador} é o nome da emoção")
        
        #vê se o jogador tá na artilharia, se não tiver, recebe valor padrão, se tiver, recebe os gols atuais para atualizar
        chave_artilheiro =  (jogador, time)
        gols_atuais = artilheiros.get(chave_artilheiro, 0)
        artilheiros[chave_artilheiro] = gols_atuais + 1

        if time == time1_info['nome']:
            gols_time1 += 1
        else:
            gols_time2 += 1
        entrada_gol = input()
            
    print("Fim de jogo.")
    
    #determina o vencedor
    vencedor_partida, motivo = '', "venceu"
    if gols_time1 > gols_time2:
        vencedor_partida = time1_info
    elif gols_time2 > gols_time1:
        vencedor_partida = time2_info
    else: #em caso de empate
        motivo = "empate"
        #vencedor por rankeamento
        if time1_info['rank'] < time2_info['rank']:
            vencedor_partida = time1_info 
        else:
            vencedor_partida = time2_info
    #printa o vencedor
    if vencedor_partida['nome'] == time1_info['nome']:
        print(f"Placar: {time1_info['nome']} {gols_time1} X {gols_time2} {time2_info['nome']}")
    else:
        print(f"Placar: {time2_info['nome']} {gols_time2} X {gols_time1} {time1_info['nome']}")

    return vencedor_partida, motivo, artilheiros

#fim de definição de função
mapa = {
    'PE': 'Nordeste', 'BA': 'Nordeste', 'AL': 'Nordeste', 'SE': 'Nordeste', 'PB': 'Nordeste', 'RN': 'Nordeste', 'CE': 'Nordeste', 'PI': 'Nordeste', 'MA': 'Nordeste',
    'SP': 'Sudeste', 'RJ': 'Sudeste', 'MG': 'Sudeste', 'ES': 'Sudeste',
    'RS': 'Sul', 'SC': 'Sul', 'PR': 'Sul'
}
cotas_regiao = {'Nordeste': 0, 'Sudeste': 0, 'Sul': 0}
times = {}



nome_clube = ''
while len(times) < 6 and nome_clube != 'FIM':
    nome_clube = input()
    #checa se não acabou
    if nome_clube != "FIM":
        #pega a sigla e descobre de qual região é
        estado = input()
        regiao = mapa[estado]

        if cotas_regiao[regiao] >= 2:
            print(f"Cota para a região {regiao} atingida. Por favor, insira um clube de outro estado, de outra região.")
        else:
            cotas_regiao[regiao] += 1
            times[nome_clube] = {'nome': nome_clube, 'estado': estado, 'regiao': regiao, 'pontos': 0, 'saldo_gols': 0, 'gols_feitos': 0}

if len(times) < 6:
    print(f'Ai não dá, com {len(times)} somente não dá para fazer um campeonato, essa ideia de Copa União foi um fiasco mesmo, #VOLTACBF')
else:
    #fase de liga
    for i in range(15):
        linha_placar = input().split(" X ")
        partes_time1 = linha_placar[0].split(' ')
        gols_time1 = int(partes_time1[-1])
        #junta o nome exceto o placar
        nome_time1 = " ".join(partes_time1[:-1])

        partes_time2 = linha_placar[1].split(' ')
        gols_time2 = int(partes_time2[0])
        #junta o nome exceto o placar
        nome_time2 = " ".join(partes_time2[1:])

        #saldo de gols
        times[nome_time1]['gols_feitos'] += gols_time1
        times[nome_time1]['saldo_gols'] += (gols_time1 - gols_time2)
        times[nome_time2]['gols_feitos'] += gols_time2
        times[nome_time2]['saldo_gols'] += (gols_time2 - gols_time1)

        #decide resultado da partida e pontuação
        if gols_time1 > gols_time2:
            times[nome_time1]['pontos'] += 3
        elif gols_time2 > gols_time1:
            times[nome_time2]['pontos'] += 3
        else:
            times[nome_time1]['pontos'] += 1
            times[nome_time2]['pontos'] += 1
        
    #selection sort
    tabela_ordenada = {}
    times_ja_colocados = {}
    #loop pra preencher o ranking
    for i in range(1, len(times) + 1):
        melhor_time_nome = ''

        #encontra o melhor entre os ainda não selecionados
        for nome_time in times:
            if nome_time not in times_ja_colocados:
                if melhor_time_nome == '':
                    melhor_time_nome = nome_time
                else:
                    candidato_info = times[nome_time]
                    melhor_info_atual = times[melhor_time_nome]

                    #seleção por pontos
                    if candidato_info['pontos'] > melhor_info_atual['pontos']:
                        melhor_time_nome = nome_time
                    #seleção por saldo de gols
                    elif candidato_info['pontos'] == melhor_info_atual['pontos']:
                        if candidato_info['saldo_gols'] > melhor_info_atual['saldo_gols']:
                            melhor_time_nome = nome_time
       
        #adiciona o melhor time encontrado na tabela e marca como já colocado
        tabela_ordenada[i] = {'nome': melhor_time_nome}
        tabela_ordenada[i].update(times[melhor_time_nome])
        times_ja_colocados[melhor_time_nome] = True
    
    #impressao da tabela
    for i in range(1, 7):
        time_info = tabela_ordenada[i]
        print(f"{time_info['nome']} - {time_info['pontos']} pontos")
    
    #classificados
    classificado1, classificado2, classificado3, classificado4 = tabela_ordenada[1], tabela_ordenada[2], tabela_ordenada[3], tabela_ordenada[4]
    classificado1['rank'], classificado2['rank'], classificado3['rank'], classificado4['rank'] = 1, 2, 3, 4
    #confrontos
    print("Os confrontos foram definidos:")
    print(f"{classificado1['nome']} X {classificado4['nome']}")
    print(f"{classificado2['nome']} X {classificado3['nome']}")

    artilheiros = {}
    #finais
    print("Vai começar o confronto, quem será que vence?")
    msg_venceu = "venceu e foi para a final, será que vai ser campeão?"
    msg_empatou = "passa para a final após vencer nos pênaltis, será que vai ser campeão?"
    #semi 1
    #descobre quem venceu e quem perdeu
    vencedor_semi1, motivo1, artilheiros = partida(classificado1, classificado4, artilheiros)
    if vencedor_semi1['nome'] == classificado1['nome']:
        perdedor_semi1 = classificado4 
    else:
        perdedor_semi1 = classificado1
    if motivo1 == 'venceu':
        msg = msg_venceu
    else:
        msg = msg_empatou
    print(f"O {vencedor_semi1['nome']} {msg}")
    #semi2
    print("Vai começar o confronto, quem será que vence?")
    #descobre quem venceu e perdeu
    vencedor_semi2, motivo2, artilheiros = partida(classificado2, classificado3, artilheiros)
    if vencedor_semi2['nome'] == classificado2['nome']:
        perdedor_semi2 = classificado3
    else:
        perdedor_semi2 = classificado2

    if motivo2 == 'venceu':
        msg = msg_venceu
    else:
        msg = msg_empatou
    print(f"O {vencedor_semi2['nome']} {msg}")
    
    #final
    print("Vai começar a grande decisão, quem será o campeão brasileiro de 1987?")
    campeao, motivofinal, artilheiros = partida(vencedor_semi1, vencedor_semi2, artilheiros)
    #decide campeão e vice
    campeao_final = campeao
    if campeao['nome'] == vencedor_semi1['nome']:
        vice_campeao = vencedor_semi2
    else:
        vice_campeao = vencedor_semi1
    #casos especiais sport e santa passam o titulo
    if campeao['nome'] == 'Sport' or campeao['nome'] == 'Santa Cruz':
        if campeao['nome'] == 'Sport':
            print("Quem deixou o Sport participar, a Copa União só permite clubes grandes de participarem, tirem ele daqui que do jeito que eles são é capaz de irem no tribunal pedir o reconhecimento do 'Brasileiro de Questão de IP'")
        else:
            print("O terror do Nordeste agradece o reconhecimento, porém recusa o titulo, diferente do seu rival ele prefere ganhar o título em campo, e não em imaginação")
        
        campeao_final = vice_campeao
    else:
        campeao_final = campeao
    #caso continue sendo um dos dois, vai pelo ranking
    if campeao_final['nome'] == 'Sport' or campeao_final['nome'] == 'Santa Cruz':
        if campeao_final['nome'] == 'Sport':
                print("Quem deixou o Sport participar, a Copa União só permite clubes grandes de participarem, tirem ele daqui que do jeito que eles são é capaz de irem no tribunal pedir o reconhecimento do 'Brasileiro de Questão de IP'")
        else:
                print("O terror do Nordeste agradece o reconhecimento, porém recusa o titulo, diferente do seu rival ele prefere ganhar o título em campo, e não em imaginação")
            
        #campeao se torna o com maior pontos
        if perdedor_semi1['pontos'] > perdedor_semi2['pontos']:
            campeao_final = perdedor_semi1
        elif perdedor_semi2['pontos'] > perdedor_semi1['pontos']:
            campeao_final = perdedor_semi2
        else: #desempate por sg
            if perdedor_semi1['saldo_gols'] > perdedor_semi2['saldo_gols']:
                campeao_final = perdedor_semi1
            else:
                campeao_final = perdedor_semi2

    #print campeão
    if campeao_final['nome'] == 'Flamengo':
        print("Em 1987, o Flamengo é o campeão inquestionável! Conquistou na bola e com o reconhecimento merecido. Qualquer outra conversa é história para boi dormir.")
    else:
        print(f"E o campeão do real Campeonato Brasileiro de 1987 foi o {campeao_final['nome']}, ouvi dizer que a CBF tava querendo fazer um outro campeonato chamado módulo amarelo, ainda bem que todo mundo entendeu que aquilo é somente uma serie B")

    #artilharia
    if artilheiros == {}:
        print("Esse ano o nivel foi fraco, não tivemos um artilheiro")
    else:
        #encontra o maior numero de gols
        max_gols = 0
        for chave_artilheiro in artilheiros:
            gols_do_jogador = artilheiros[chave_artilheiro]
            if gols_do_jogador > max_gols:
                max_gols = gols_do_jogador
        
        #encontra o artilheiro
        artilheiro_final = ""
        artilheiro_time = ""
        for chave_artilheiro in artilheiros:
            gols_do_jogador = artilheiros[chave_artilheiro]
            
            #desempate por ordem alfabética
            if gols_do_jogador == max_gols:
                nome_candidato = chave_artilheiro[0] 
                if artilheiro_final == "" or nome_candidato < artilheiro_final:
                    artilheiro_final = nome_candidato
                    artilheiro_final_time = chave_artilheiro[1]
        
        #prints por time do artilheiro
        if artilheiro_final_time == campeao_final['nome']:
            print(f"{artilheiro_final} garantiu o título do campeonato e a artilharia, que ano feliz para ele")
        else:
            print(f"Apesar de não ter sido campeão, pelo menos {artilheiro_final} foi o artilheiro, a culpa não foi dele")
