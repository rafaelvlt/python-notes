qtd_tecnicos = int(input())
contador = 0
tecnicos = {}
while contador < qtd_tecnicos:
    nome = input()
    nacionalidade = input()
    if nacionalidade != 'argentino':
        #informações do técnico
        titulos_continentais = int(input())
        titulos_nacionais = int(input())
        aproveitamento = float(input())
        interesse = input()
        pontuação_total = (titulos_continentais + titulos_nacionais) * aproveitamento
        tecnicos[contador] = {'nome': nome, 'nacionalidade': nacionalidade, 'titulos_continentais': titulos_continentais, 'titulos_nacionais': titulos_nacionais, 'aproveitamento': aproveitamento, 'interesse': interesse, 'pontuação_total': (titulos_continentais*100 + titulos_nacionais*50) * aproveitamento}
        
        #buffs e debuffs por nacionalidade
        if tecnicos[contador]['nacionalidade'] == 'brasileiro':
            tecnicos[contador]['pontuação_total'] *= 1.10
        elif tecnicos[contador]['nacionalidade'] == 'alemão':
            tecnicos[contador]['pontuação_total'] *= 0.90
            print('Iremos mesmo perdoar o 7x1?')
        #debuff por falta de titulo continental
        if tecnicos[contador]['titulos_continentais'] == 0:
            tecnicos[contador]['pontuação_total'] *= 0.50

        if tecnicos[contador]['nome'] == 'Ancelotti':
            print('Será que Carleto irá continuar no cargo?')
        elif tecnicos[contador]['nome'] == 'Jorge Jesus':
            print('O mister finalmente retornará ao Brasil?')
        contador += 1
    else:
        print('Um hermano comandando a seleção? Sai fora!')
        qtd_tecnicos -= 1
#ranking por bubblesort
for i in range(len(tecnicos)):

    for j in range(0, len(tecnicos) - i - 1):
        if tecnicos[j+1]['pontuação_total'] > tecnicos[j]['pontuação_total']:
            temp = tecnicos[j]
            tecnicos[j] = tecnicos[j+1]
            tecnicos[j+1] = temp

#printa o raking
print('Lista de treinadores - CBF')
print(f"1º {tecnicos[0].get('nome')} - {tecnicos[0].get('nacionalidade')} - {tecnicos[0]['pontuação_total']:.2f} pontos")
print(f"2º {tecnicos[1].get('nome')} - {tecnicos[1].get('nacionalidade')} - {tecnicos[1]['pontuação_total']:.2f} pontos")
print(f"3º {tecnicos[2].get('nome')} - {tecnicos[2].get('nacionalidade')} - {tecnicos[2]['pontuação_total']:.2f} pontos")


#vê qual dos tecnicos é o escolhido em ordem decrescente
escolhido = {}
for i in range(3):
    #caso seja o ancelotti, é escolhido na hora
    if tecnicos[i].get('nome') == 'Ancelotti' and tecnicos[i].get('interesse') == 'sim':
        escolhido = tecnicos[i]
    #se não for o ancelotti e já n tiver escolhido, vai iterando sobre os tecnicos para escolher o mais qualificado que deseja treinar
    elif tecnicos[i].get('interesse') != 'sim' and escolhido == {}:
        print(f"O {tecnicos[i].get('nome')} não aceitou a proposta da CBF e outros nomes serão analisados. Cuida, CBF!")
    elif tecnicos[i].get('interesse') == 'sim' and escolhido == {}:
        escolhido = tecnicos[i]

if escolhido == {}:
    print('Nenhum técnico aceitou a maior seleção do mundo!? Que humilhação, Sr. Samir Xaud!!!')
else:
    #nao for br
    if escolhido['nacionalidade'] != 'brasileiro':
        print(f"{escolhido['nome']} será o quarto estrangeiro a treinar o Brasil. Que honra para o {escolhido['nacionalidade']}!")
    
    #prints caso tecnicos especiais com eslse para se não for
    if escolhido['nome'] == 'Ancelotti':
        print('Depois de uma longa novela, Carlo Ancelotti continuará como o treinador da Seleção Brasileira! Estamos bem servidos!')

    elif escolhido['nome'] == 'Jorge Jesus':
        print('JESUS VOLTOU!!! Será que ele conseguirá repetir na seleção o sucesso que obteve no Flamengo?')
    
    elif escolhido['nome'] == 'Felipão':
        print('FELIPÃO DE NOVO!? Vem mais um 7x1 por aí?')

    else:
        print(f"O técnico {escolhido['nacionalidade']} {escolhido['nome']} irá treinar o Brasil. Não era o nome que esperávamos, mas torcemos para que faça um bom trabalho!")
