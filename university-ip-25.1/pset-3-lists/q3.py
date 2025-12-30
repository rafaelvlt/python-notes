#inputs iniciais de qtd de armas e criação da lista
qtd_armas = int(input())
arsenal = []
armas_usadas = []
for arma in range(qtd_armas):
    arsenal.append(input())

golpes_thanos = 0
combate_terminou = False
while not combate_terminou:
    solicitacao = input()
    #caso a solicitacao esteja no arsenal
    if solicitacao in arsenal:
        if solicitacao not in armas_usadas: #caso não esteja nas armas usadas
            print(f'{solicitacao} usado(a) com sucesso!')
            armas_usadas.append(solicitacao) #adiciona a lista nas armas usadas
        else:
            print(f'{solicitacao} já foi usado(a)!')
            golpes_thanos += 1
    else: #se a solicitacao não estiver no arsenal
        #scaso esteja solicitando fim, termina o loop
        if solicitacao == 'fim':
            combate_terminou = True
        else: #caso contrario, arma não foi inserida
            print(f'{solicitacao} não está disponível!')
            golpes_thanos += 1

#após combate, pega o tamanho da lista de armas usadas e printa o tamanho, ou seja quantidade usada
print(f'Batalha encerrada! Os Vingadores utilizaram {len(armas_usadas)} arma(s).')

#condições de fim de batalha
if golpes_thanos == 0:
    print('Vitória! Os Vingadores salvaram o UNIVERSO!\n')
    print('Tony Stark:\nSalvar o mundo de novo? Vou precisar de um aumento.\n')
    print('Thor:\nEspero que tenha cerveja depois disso!\n')
    print('Homem-Aranha:\nPosso dizer que ajudei, né? Tipo… oficialmente?\nDá pra postar isso no Insta dos Vingadores?')
elif golpes_thanos == 1:
    print('Os Vingadores sofreram um golpe do Thanos!\nVitória por pouco! Os Vingadores ganharam...\n')
    print('Tony Stark:\nQuase que eu fico sem troco para o cafezinho.\n')
    print('Thor:\nEsse quase foi o meu momento de “não consegui”. Mas consegui, então vale cerveja!\n')
    print('Peter Quill (Star-Lord):\nCara, quase perdi o ritmo do meu walkman!')
elif golpes_thanos >= 2:
    print(f'Os Vingadores sofreram {golpes_thanos} golpes do Thanos!')
    print('Derrota... Os Vingadores não conseguiram todas as armas necessárias.\n')
    print('Tony Stark:\nEssa não foi das melhores ideias...\n')
    print('Thor:\nCulpa do humano. Eu sabia que devíamos ter chamado o Hulk.')
