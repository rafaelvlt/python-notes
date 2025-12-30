jogadores = {}
nome_jogador = ''
index_jogadores = 0
#pega informações dos jogadores e coloca em um dicionario com outros dicionarios aninhados
while nome_jogador != 'FIM':
    nome_jogador = input()
    if nome_jogador != 'FIM':
        disposicao_percentual = int(input())
        posicao = input()
        if disposicao_percentual >= 85:
            acoes_ofensivas = int(input())
            jogadores[index_jogadores] = {'nome': nome_jogador, 'posicao': posicao, 'disposicao': disposicao_percentual, 'acoes': acoes_ofensivas}
        elif disposicao_percentual >= 50:
            desempenho_ultimo_jogo = int(input())
            jogadores[index_jogadores] = {'nome': nome_jogador, 'posicao': posicao, 'disposicao': disposicao_percentual, 'ultimo jogo': desempenho_ultimo_jogo}
        else:
            desempenho_ultimo_treino = int(input())
            jogadores[index_jogadores] = {'nome': nome_jogador, 'posicao': posicao, 'disposicao': disposicao_percentual, 'ultimo treino': desempenho_ultimo_treino}
        
        index_jogadores += 1

#relatorio individual
atacantes_prontos = 0
meio_def_prontos = 0
for index in range(len(jogadores)):
    if jogadores[index]['disposicao'] >= 85:
        if jogadores[index]['posicao'] == 'atacante':
            if jogadores[index]['acoes'] > 10:
                print(f"{jogadores[index].get('nome')} está com um bom desempenho ofensivo.")
                atacantes_prontos += 1
            else:
                print(f"{jogadores[index].get('nome')} pode melhorar, Ancelotti pode usá-lo no segundo tempo.")
        else:
            if jogadores[index]['acoes'] >= 20:
                print(f"{jogadores[index].get('nome')} está com um bom desempenho de passes.")
                meio_def_prontos += 1
            else:
                print(f"{jogadores[index].get('nome')} pode melhorar, Ancelotti pode não colocá-lo no primeiro tempo.")
    elif jogadores[index]['disposicao'] >= 50:
        if jogadores[index]['ultimo jogo'] > 80:
            print(f"O jogador {jogadores[index].get('nome')} pode ser escalado para a próxima partida.")
            if jogadores[index]['posicao'] == 'atacante':
                atacantes_prontos += 1
            else:
                meio_def_prontos += 1
        else:
            print(f"Ancelotti precisa analisar o desempenho do {jogadores[index].get('nome')} na partida.")
    else:
        if jogadores[index]['ultimo treino'] > 70:
            print(f"Ancelotti deve colocar {jogadores[index].get('nome')} para treinar mais.")
        else:
            print(f"{jogadores[index].get('nome')} não deveria estar na próxima convocação.")

#resumo da comissão técnica
print('')
print('Relatório dos jogadores:')
print(f'Total de jogadores analisados: {len(jogadores)}')
print(f'Atacantes prontos para começar: {atacantes_prontos}')
print(f'Meio-campistas e Defensores prontos para começar: {meio_def_prontos}')
