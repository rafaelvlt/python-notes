#definição de função
def calcular_pontos(jogador):
    """recebe o dicionario com acoes do jogador e retorna a pontuação dele"""
    #dicionario com pontuação
    poisocoes_defesa = ('goleiro', 'zagueiro', 'lateral')
    pontos = 0

    #por gol
    pontos += jogador['gols_feitos'] * 8
    #assistencia
    pontos += jogador['assistencias'] * 5
    #cartões
    pontos += jogador['cartoes_amarelos'] * (-1)
    pontos += jogador['cartoes_vermelhos'] * (-3)

    #caso seja defensor
    if jogador['posicao'] in poisocoes_defesa:
        if jogador['gols_sofridos'] == 0:
            pontos += 5
    
    return pontos
#fim de definição de função
prioridades = {'goleiro': 5, 'lateral': 4, 'zagueiro': 3, 'meia': 2, 'atacante': 1}
#inputs
qtd_tecnicos = int(input())
                   
tecnicos = {}
tecnicos_ordem = []
num_jogadores = 0
for i in range(qtd_tecnicos):
    nome_tecnico = input()
    tecnicos[nome_tecnico] = {}
    tecnicos_ordem.append(nome_tecnico)
    dados_tecnico = {
    'titulares': {'goleiro': [], 'zagueiro': [], 'lateral': [], 'meia': [], 'atacante': []},
    'reservas': {'goleiro': [], 'zagueiro': [], 'lateral': [], 'meia': [], 'atacante': []},
    'substituicao_feita': ''
    }
    for banco in range(2):
        entrada = input()
        if entrada == 'titulares': num_jogadores = 11
        else: num_jogadores = 5
        
        #pega informações sobre os jogadores
        for jogador in range(num_jogadores):
            info_jogador = input().split(',')
            jogador = {'nome': info_jogador[0], 'posicao': info_jogador[1], 'gols_feitos': int(info_jogador[2]), 'assistencias': int(info_jogador[3]), 'cartoes_amarelos': int(info_jogador[4]), 'cartoes_vermelhos': int(info_jogador[5]), 'gols_sofridos': int(info_jogador[6])}
            dados_tecnico[entrada][jogador['posicao']].append(jogador)
    #coloca infos no dicionario
    tecnicos[nome_tecnico] = dados_tecnico

#calculo de pontos
for nome_tecnico, dados in tecnicos.items():
    pontuacao_inicial = 0

    for posicao in dados['titulares']:
        for jogador in dados['titulares'][posicao]:
            jogador['pontos'] = calcular_pontos(jogador)
            pontuacao_inicial += jogador['pontos']
    for posicao in dados['reservas']:
        for jogador in dados['reservas'][posicao]:
            jogador['pontos'] = calcular_pontos(jogador)

    #logica para substituição
    melhor_troca = {'ganho': 0}
    for posicao_reserva, lista_reserva in dados['reservas'].items():
        #pega os dados do reserva atual
        reserva = lista_reserva[0]
        
        for titular in dados['titulares'][posicao_reserva]:
            #diferença entre pontos do reserva e do titular
            ganho_atual = reserva['pontos'] - titular['pontos']

            #caso seja um ganho melhor do que até agora, realiza a troca
            if ganho_atual > melhor_troca['ganho']:
                melhor_troca = {'ganho': ganho_atual, 'titular': titular, 'reserva': reserva}
            #checa a prioridade se o ganho for igual
            elif ganho_atual == melhor_troca['ganho'] and ganho_atual > 0:
                prioridade_atual = prioridades[posicao_reserva]
                prioridade_melhor = prioridades[melhor_troca['reserva']['posicao']]

                #troca se a prioridade for maior que o do melhor até agora
                if prioridade_atual > prioridade_melhor:
                    melhor_troca = {'ganho': ganho_atual, 'titular': titular, 'reserva': reserva}
                #substituição lexicográfica
                elif prioridade_atual == prioridade_melhor:
                    if titular['nome'] > melhor_troca['titular']['nome']:
                        melhor_troca = {'ganho': ganho_atual, 'titular': titular, 'reserva': reserva}
    if 'titular' in melhor_troca.keys():
        dados['substituicao_feita'] = melhor_troca
        dados['pontuacao_final'] = pontuacao_inicial + melhor_troca['ganho']
    else:
        dados['pontuacao_final'] = pontuacao_inicial

#relatório final
print(f"Os técnicos que participarão da avaliação da rodada serão {', '.join(tecnicos_ordem)}.")

#prints se fez substituição ou não
for nome in tecnicos_ordem:
    dados_do_tecnico = tecnicos[nome]
    #se fez substituição, pega os dados dela
    if dados_do_tecnico['substituicao_feita'] != '':
        titular_nome = dados_do_tecnico['substituicao_feita']['titular']['nome']
        reserva_nome = dados_do_tecnico['substituicao_feita']['reserva']['nome']
        print(f"{nome} é um gênio da bola mesmo, a substituição de {titular_nome} por {reserva_nome} fez ele ganhar pontos!")
    else: # se não, printa a mensagem
        print(f"Pode cortar {nome} dos candidatos a técnico da amarelinha, nem fazer uma substituição ele consegue...")


vencedor = ''
maior_pontuacao = 0
#itera sobre o dicionario e devolve o nome e pontuação do vencedor
for nome_tecnico, dados in tecnicos.items():
    if maior_pontuacao == 0 or dados['pontuacao_final'] > maior_pontuacao:
        maior_pontuacao = dados['pontuacao_final']
        vencedor_nome = nome_tecnico
#prints finais
print(f"{vencedor_nome} é incrível ganhou essa rodada com {maior_pontuacao} pontos!")
if tecnicos[vencedor_nome]['substituicao_feita'] == '':
    print(f"Temos que pedir desculpas a {vencedor_nome}, mesmo sem fazer uma substituição ele foi o melhor da rodada, talvez ele deva assumir a amarelinha depois do Ancelotti!")
