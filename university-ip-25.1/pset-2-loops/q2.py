material = ''
uniformes = 0
isotonicos = 0
raquetes = 0
toalhas = 0
numero_materiais = 0
sabotagens = 0 #sabotage certamente um dos artistas

while material != "FIM":
    material = input()
    #caso não for uma sabotagem, entra nos ifs que adicionam material
    if material != "Sabotagem":
        if material == 'Uniforme':
            uniformes += 1
            numero_materiais += 1
            print(f'Tava faltando camisa! Agora temos {uniformes} uniforme(s)')
        elif material == "Isotônico":
            isotonicos += 1
            numero_materiais += 1
            print(f'Bora garantir a hidratação! Agora temos {isotonicos} isotônico(s)')
        elif material == "Raquete":
            raquetes += 1
            numero_materiais += 1
            print(f'Mais uma raquete saindo! Agora temos {raquetes} raquete(s)')
        elif material == "Toalha":
            toalhas += 1
            numero_materiais += 1
            print(f'Mais uma toalha saindo! Agora temos {toalhas} toalha(s)')
    else:  #se for uma sabotagem, pega o input do material sabotado, e vê se é possível que ele seja de fato sabotado
        material = input()
        if material == 'Uniforme' and uniformes > 0:
            uniformes -= 1
            numero_materiais -= 1
            sabotagens += 1
            print(f'O sueco está roubando as camisas de Hugo!')
        elif material == "Isotônico" and isotonicos > 0:
            isotonicos -= 1
            numero_materiais -= 1
            sabotagens += 1
            print(f'O sueco está sabotando a hidratação de Hugo!')
        elif material == "Raquete" and raquetes > 0:
            raquetes -= 1
            numero_materiais -= 1
            sabotagens += 1
            print(f'O sueco está roubando as raquetes de Hugo!')
        elif material == "Toalha" and toalhas > 0:
            toalhas -= 1
            numero_materiais -= 1
            sabotagens += 1
            print(f'O sueco está roubando as toalhas de Hugo!')


#relatório final
print(f'Bora ver o relatório final dos materiais!\nUniforme: {uniformes} unidade(s).\nIsotônico: {isotonicos} unidade(s).\nRaquete: {raquetes} unidade(s).\nToalha: {toalhas} unidade(s).')

#sabotagem completa
if numero_materiais == 0 and sabotagens > 0:
    print('Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!')

#esqueceu
if numero_materiais == 0 and sabotagens == 0:
    print('Vish... Parece que vão faltar materiais para garantir a vitória do nosso atleta.')


if numero_materiais > 0:
    if uniformes > 0 and isotonicos > 0 and raquetes > 0 and toalhas > 0:
        print('Tudo pronto! Não vai faltar nada para mais um título de Hugo Calderano!')
    else:
        print('Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!')
