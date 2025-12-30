#definição de funções
def novo_lutador(primeiro, segundo):
    """checa se o nome do primeiro e segundo lutador são compatíveis para ter um terceiro, se sim retorna o nome do lutador que receberá ajuda"""
    resultado = ''

    if (primeiro == 'Goku' and segundo == 'Jiren') or (primeiro == 'Jiren' and segundo == 'Goku') :
        resultado = 'Goku'
    elif (primeiro == 'Frieza' and segundo == 'Jiren') or (segundo == 'Frieza' and primeiro == 'Jiren'):
        resultado = 'Frieza'
    elif (primeiro == 'Gohan' and segundo == 'Namekuseijins') or (segundo == 'Gohan' and primeiro == 'Namekuseijins'):
        resultado = 'Gohan'
    elif (primeiro == 'Androide 17' and segundo == 'Ribrianne') or (segundo == 'Androide 17' and primeiro == 'Ribrianne'):
        resultado = 'Androide 17'
    else:
        resultado = 'nenhum'
    return resultado

def calcular_pontuacao(golpe1, golpe2=''):
    """calcula a pontuacao de um lutador/equipe, o 2 parametro fica vazio default se houver apenas 1 lutador invés de ser uma equipe"""
    resultado = 0
    resultado = (len(golpe1) % 8) + (len(golpe2) % 8)
    return resultado


#fim de definição de funções

#variáveis
qtd_batalhas = int(input())
two_versus_one = False
pontuacao_primeiro = 0
pontuacao_segundo = 0
vencedor = ''
ajudado = ''

print(f'O torneio do poder irá começar com {qtd_batalhas} batalhas no dia de hoje! Vamos ver quais universos vão conseguir se manter vivos até o final do dia!')
for batalha in range(qtd_batalhas):
    #recebe os inputs e transforma em lista, sendo indice 0 nome do lutador, e indice 1 o golpe
    lutador1 = input()
    lutador2 = input()
    lutador1 = lutador1.split(' - ')
    lutador2 = lutador2.split(' - ')
    ajudado = novo_lutador(lutador1[0], lutador2[0])
    #caso seja uma luta especial, pega string pro lutador 3 e divide em lista também
    if  ajudado != 'nenhum':
        #habilita a flag de 2v1, e pega as infos do 3 lutador
        two_versus_one = True
        lutador3 = input()
        lutador3 = lutador3.split(' - ')
        print(f'A intensidade dos dois lutadores motivou {lutador3[0]} a entrar na batalha também!')
        #checa qual lutador será ajudado
        if ajudado == lutador1[0]:
            pontuacao_primeiro = calcular_pontuacao(lutador1[1], lutador3[1])
            pontuacao_segundo = calcular_pontuacao(lutador2[1])
        else:
            pontuacao_primeiro = calcular_pontuacao(lutador1[1])
            pontuacao_segundo = calcular_pontuacao(lutador2[1], lutador3[1])
    else: #se nenhum for ajudado
        pontuacao_primeiro = calcular_pontuacao(lutador1[1])
        pontuacao_segundo = calcular_pontuacao(lutador2[1])

    #declara qual foi vencedor e qual foi perdedor
    if pontuacao_primeiro > pontuacao_segundo:
        if two_versus_one and ajudado == lutador1[0]: #se for uma luta 2v1
            vencedor = lutador1[0] + ' e ' + lutador3[0]
        else:
            vencedor = lutador1[0]
    
    else:
        if two_versus_one and ajudado == lutador2[0]:
            vencedor = lutador2[0] + ' e ' + lutador3[0]
        else:
            vencedor = lutador2[0]
            
    #printa o vencedor dependendo se é tag team ou não
    if two_versus_one:
        print(f'Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {lutador1[1]}, {lutador2[1]} e {lutador3[1]}! A batalha acaba com {vencedor} no topo!')
    else:
        print(f'Incrível! {vencedor} mostrou sua força e defenderá seu universo até o final!')
    two_versus_one = False #reseta a flag
