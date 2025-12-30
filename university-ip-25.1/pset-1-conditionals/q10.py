sequestro_texto = 'Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!'
cidade_ruim = 0
sequestrado = False
partida_jogada = 0
vitorias = 0
derrotas = 0

print('Byte, o cachorro mais promissor do futebol nordestino, acaba de calçar suas quatro chuteiras e está pronto para entrar em campo!')

#partida1
cidade1 = input()
rival1 = input()
resultado1 = input()

cidade2 = cidade1
rival2 = rival1

if resultado1 == sequestro_texto:
    #num1 operador1 num2
    sequestrado = True
    expressao_num = input()
    num1, operador, num2 = expressao_num
    vitorias += 1

if cidade1 == 'Catende' or cidade1 == 'Tabira':
    print('É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.')
    cidade_ruim += 1

#codigo sport
if 's' in rival1:
    if 'p' in rival1:
        if 'o' in rival1:
            if 'r' in rival1:
                if 't' in rival1:
                    print('Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!')

if resultado1 == 'VENCEU':
    print('TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!')
    vitorias += 1
elif resultado1 == 'perdeu':
    print('Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...')
    derrotas += 1
partida_jogada += 1
#partida 2
if not sequestrado:
    cidade2 = input()
    rival2 = input()
    resultado2 = input()
    if resultado2 == sequestro_texto:
        #num1 operador1 num2
        sequestrado = True
        expressao_num = input()
        num1, operador, num2 = expressao_num
        vitorias += 1

    if cidade2 == 'Catende' or cidade2 == 'Tabira':
        print('É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.')
        cidade_ruim += 1

    if cidade_ruim == 2:
        print('Não dá mais! Jogar nessas duas cidades é sinal de que o Santa Cruz precisa mais de magia do que de reforços...')

    if 's' in rival2:
        if 'p' in rival2:
            if 'o' in rival2:
                if 'r' in rival2:
                    if 't' in rival2:
                        print('Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!')
                        


    if resultado2 == 'VENCEU':
        print('TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!')
        vitorias += 1
    elif resultado2 == 'perdeu':
        print('Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...')
        derrotas += 1
    partida_jogada += 1

#caso seja sequestrado
if sequestrado:
    print('Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!')
    num1 = int(num1)
    num2 = int(num2)
    if operador == '+':
        resposta = num1 + num2
    elif operador == '-':
        resposta = num1 - num2
    elif operador == '*':
        resposta = num1 * num2
    elif operador == '/':
        resposta = num1 / num2
    print(f'A expressão resolvida é: {resposta:.2f}')
    print('Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!')

#relatorio
print('\nRELATÓRIO DA PRÉ-TEMPORADA DO BYTE:')
print(f'- Partidas jogadas: {partida_jogada}')
print(f'- Vitórias: {vitorias}')
print(f'- Derrotas: {derrotas}')
if sequestrado:
    print('- Tentaram roubar o bixinho: sim :(')
elif not sequestrado:
    print('- Tentaram roubar o bixinho: Não!!!! :D')
if cidade1 == cidade2:
    print(f'- Cidades visitadas: {cidade1}')
else:
    cidades_visitadas = cidade1 + ' e ' + cidade2
    print(f'- Cidades visitadas: {cidades_visitadas}')

if rival1 == rival2:
    print(f'- Adversários enfrentados: {rival1}\n')
else:
    rivais_enfrentados = rival1 + ' e ' + rival2
    print(f'- Adversários enfrentados: {rivais_enfrentados}\n')

print('E assim termina a pré-temporada do Byte pelos gramados. Anotar tudo isso na mão dá uma trabalheira! Nas próximas férias o Byte deve esperar saber laços, listas, funções e muito mais pra registrar tudo com mais facilidade :)')
