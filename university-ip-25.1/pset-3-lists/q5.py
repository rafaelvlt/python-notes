print('Vamos lá, Vanellope! Vou te ajudar a montar um carro CINistro!')

#para usar in em ufs
tipos_volante = ['Pretzel', 'Donuts']
tipos_corpo = ['Bolo de rolo', 'Barra de chocolate', 'Banda de ovo de Páscoa']
tipos_roda = ['Mentos', 'Jujuba']
#para etapa de construlão do carro
roda = []
corpo = []
volante = []
carro = []

doce_recebido = []
doces_descartados = []
recurso = input()
while recurso != 'Recursos Esgotados':
    #caso o rei roubar, descarta tudo, se não, splita o input() e faz lógica com ele
    if recurso == 'O REI DOCE ESTÁ ROUBANDO TODOS OS INGREDIENTES!':
        print('Ah não!! Ele vai destruir seu carro, Vanellope! CUIDADO')
        if len(roda)>0:
            doces_descartados.append(roda.pop(0))
        if len(corpo)>0:
            doces_descartados.append(corpo.pop(0))
        if len(volante)>0:
            doces_descartados.append(volante.pop(0))
        recurso = input()
    else:
        doce_recebido.append(recurso.split(' - '))
        if doce_recebido[0][1] == 'estragado': #caso seja estragado, é descartado automaticamente
            doces_descartados.append(doce_recebido.pop(0))
        else:
            #caso doce recebido seja um corpo e não haja já um corpo definido, é comparado a qualidade, se for maior é trocado 
            #o item pelo de amior qualidade e descartado o anterior, senão, o item é descartado
            if doce_recebido[0][0] in tipos_corpo:
                if len(corpo)>0:
                    if doce_recebido[0][1] == 'alta qualidade' and corpo[0][1] == 'qualidade mediana':
                        doces_descartados.append(corpo.pop(0))
                        corpo.insert(0, doce_recebido[0])
                    else:
                        doces_descartados.append(doce_recebido[0])
                else:
                    corpo.append(doce_recebido[0])
            #mesma lógica para volante
            if doce_recebido[0][0] in tipos_volante:
                if len(volante)>0:
                    if doce_recebido[0][1] == 'alta qualidade' and volante[0][1] == 'qualidade mediana':
                        doces_descartados.append(volante.pop(0))
                        volante.insert(0, doce_recebido[0])
                    else:
                        doces_descartados.append(doce_recebido[0])
                else:
                    volante.append(doce_recebido[0])
            #roda
            if doce_recebido[0][0] in tipos_roda:
                if len(roda)>0:
                    if doce_recebido[0][1] == 'alta qualidade' and roda[0][1] == 'qualidade mediana':
                        doces_descartados.append(roda.pop(0))
                        roda.insert(0, doce_recebido[0])
                    else:
                        doces_descartados.append(doce_recebido[0])
                else:
                    roda.append(doce_recebido[0])
        carro = corpo + volante + roda
        recurso = input()
        doce_recebido = []
#fim do programa
carro = corpo + volante + roda
if len(carro) == 3:
    componentes_medianos = 0
    for i in range(3):
        if carro[i][1] == 'qualidade mediana':
            componentes_medianos += 1
    
    if componentes_medianos == 3:
        print('Pelo menos anda! Você consegue!')
    else:
        print('Conseguimos! Impossível você não ganhar essa corrida, Vanellope!')
        print(f'Para fazer o carro você utilizou {corpo[0][0]} para ser a estrutura do carro, {volante[0][0]} para o volante, {roda[0][0]} para compor as rodas!')
else:
    print('Sinto muito, Vanellope. Não consegui te ajudar dessa vez.')
qtd_descartados = len(doces_descartados)
if qtd_descartados > 0:
    print('Alguns doces foram descartados. São eles:')
    for index in range(qtd_descartados):
        if index != qtd_descartados - 1:
            print(f'{doces_descartados[index][0]}', end=', ')
        else:
            print(f'{doces_descartados[index][0]}')









































