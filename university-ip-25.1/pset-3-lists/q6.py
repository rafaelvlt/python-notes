qtd_ondas = int(input())
vitorias_herois = 0
vitorias_viloes = 0

#diferenca
maior_diferenca = 0
diferenca_onda = 0
diferenca_vencedor = "nenhum"
participantes_diferenca = ""


for onda in range(qtd_ondas):
    personagens_bruto = input()
    lista_personagens = personagens_bruto.split(', ')
    lista_herois = []
    lista_viloes = []
    #separando entre herois e vilões
    for personagem in lista_personagens[1:-1]:
        if personagem[:1] == 'H':
             lista_herois.append(personagem[2:])
        elif personagem[:1] == 'V':
            lista_viloes.append(personagem[2:])
    
    diferenca = len(lista_herois) - len(lista_viloes)
    if diferenca > 0:
        vencedor = 'heróis'
        vitorias_herois += 1
    elif diferenca < 0:
        vencedor = 'vilões'
        vitorias_viloes += 1
    else:
        vencedor = 'empate'
    #codigo maior diferença
    if abs(diferenca) > maior_diferenca:
        maior_diferenca = abs(diferenca)
        diferenca_onda = onda+1
        diferenca_vencedor = vencedor
        participantes_diferenca = personagens_bruto

#fim do programa
if maior_diferenca == 0:
    print('🌀Nenhuma onda foi selecionada como a menos acirrada e a mais favorável para nenhum do dois lados!') #maldita formatação fiquei preso nisso
else:
    if diferenca_vencedor == 'heróis':
        print(f'🌀Onda {diferenca_onda} foi a menos acirrada e a mais favorável para os heróis!')
    elif diferenca_vencedor == 'vilões':
        print(f'🌀Onda {diferenca_onda} foi a menos acirrada e a mais favorável para os vilões!')
    
    print('Participantes analisados: ' + participantes_diferenca)

#pontuacao final
print('Agora vamos ao resultado geral das ondas...')
print(f'Heróis: {vitorias_herois} | Vilões: {vitorias_viloes}')
if vitorias_herois > vitorias_viloes:
    print('Ufa, os heróis dominaram! Central City está seguro outra vez')
elif vitorias_viloes > vitorias_herois:
    print('Ah, não. Os vilões vão dominar Central City e mandar todos os heróis embora!')
else:
    print('Ninguém é mais forte que ninguém. Heróis e vilões vão ter que entrar em consenso para viverem no mesmo espaço')
