#definição de função
def batalhas(jogador_status, chefe_status, chefe, nivel, tentativa):
    #status por tentativa e experiência
    if tentativa > 1:
        if nivel == 'Iniciante':
            jogador_status[1] *= 1.05
            chefe_status[1] *= 0.9
        elif nivel == 'Veterano':
            jogador_status[1] *= 1.1
            chefe_status[1] *= 0.8
        elif nivel == 'Mestre do Souls':
            jogador_status[1] *= 1.2
            chefe_status[1] *= 0.67
    #variaveis pré batalha
    jogador_atual = jogador_status.copy()
    chefe_atual = chefe_status.copy()
    debuff = False
    #batalha
    acabou = False
    while not acabou:
        #ação do jogador
        chefe_atual[0] -= jogador_atual[1]
        #debuff sif
        if chefe == 'Sif, a Grande Loba Cinzenta' and (chefe_atual[0] <= (int(chefe_status[0] * 0.1))) and not debuff:
            print("Sif, a Grande Loba Cinzenta está gravemente ferida! Essa é sua chance, acabe com o sofrimento dela!")
            chefe_atual[1] -= 15
            #seta em zero se ficar menor, pra não curar o jogador
            if chefe_atual[1] < 0:
                chefe_atual[1] = 0
            debuff = True
            
        #ação chefe
        if not chefe_atual[0] <= 0:
            jogador_atual[0] -= chefe_atual[1]
            #dano extra Gwyn
            if chefe == 'Gwyn, Lorde das Cinzas' and (chefe_atual[0] <= int(chefe_status[0]*0.5)):
                jogador_atual[0] -= 10

        #se são postos a menos de zero, são colocados a exatamente 0
        if jogador_atual[0] < 0: jogador_atual[0] = 0
        if chefe_atual[0] < 0: chefe_atual[0] = 0

        #fim de batalha
        #se o jogador perde, recomeça a batalha e incrementa tentativa
        if jogador_atual[0] <= 0:
            return batalhas(jogador_status, chefe_status, chefe, nivel, tentativa+1)
        elif chefe_atual[0] <= 0:
            #tentativas necessárias
            print(f'Você precisou de {tentativa} tentativas para vencer o(a) {chefe}!')
            #mensagens por nível
            if nivel == 'Iniciante':
                if tentativa <= 5: print('Esse iniciante teve muita sorte, no próximo boss ele vai conhecer a verdadeira DOR!!!')
                elif tentativa <= 10: print('Até que não foi tão ruim assim, continue assim novato!')
                else: print('Bem vindo a Dark Souls.')
            elif nivel == 'Veterano':
                if tentativa <= 5: print('Você já andou por Lordran antes, não é? Impressionante.')
                elif tentativa <= 10: print('Nada mal, guerreiro. Mas os próximos desafios não terão piedade.')
                else: print('Mesmo os veteranos sangram em Dark Souls...')
            elif nivel == 'Mestre do Souls':
                if tentativa == 1: print('Inacreditável. Um verdadeiro Mestre do Souls. Está destinado a se tornar o Dark Lord!')
                elif tentativa <= 10: print('Seu conhecimento sobre o ciclo é profundo. Quase como se já tivesse vivido isso mil vezes...')
                else: print('Nem mesmo os Mestres escapam ilesos da chama...')
            #mensagens especiais por chefe
            if chefe == 'Gwyn, Lorde das Cinzas':
                print('A chama se apaga, e o silêncio reina em Lordran. Você derrotou o Senhor das Cinzas...')
                if tentativa == 1:
                    print('O ciclo foi quebrado... Você se tornou o verdadeiro Senhor das Cinzas. Um novo destino começa...')
                else:
                    print('Mas o ciclo... o ciclo continua.')
            elif chefe == 'Sif, a Grande Loba Cinzenta':
                print('A grande loba cai com honra. No fundo dos seus olhos, havia apenas lealdade.')
            #acaba a recursão
            return tentativa




#fim definição de funções
#iniciais chefes
sif_status = [3432, 35]
gwyn_status = [4185, 55]

#variaveis
#parametros do jogador
nivel_jogador = input()
atributos = input().split()
#variáveis, 1 = vida, 2= dps
jogador_status = [int(atributos[0])*20, int(atributos[1])*5]
#chefes parametros
chefe = input()


if chefe == 'Sif, a Grande Loba Cinzenta':
    print('Venha até mim guardiã do túmulo de Artorias... Vamos acabar logo com isso!')
    batalhas(jogador_status, sif_status, chefe, nivel_jogador, 1)
elif chefe == 'Gwyn, Lorde das Cinzas':
    print('Enfim estou de frente ao Senhor das Cinzas! Nossa batalha será lendária e ecoará em todos os cantos de Lordran!!!')
    batalhas(jogador_status, gwyn_status, chefe, nivel_jogador, 1)

