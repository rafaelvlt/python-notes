humor = input()
vezes_senta = int(input())
vezes_pata = int(input())
vezes_fica = int(input())
vezes_pega = int(input())
novo_comando = input()

if novo_comando == 'Senta':
    vezes_senta += 1
elif novo_comando == 'Dá a patinha':
    vezes_pata += 1
elif novo_comando == 'Fica':
    vezes_fica += 1
elif novo_comando == 'Pega':
    vezes_pega += 1

if novo_comando == 'Senta':
    if vezes_senta >= 3:
        if humor != 'Brincalhão':
            print('Byte é o melhor')
        else:
            print('Ele parece estar muito animado para isso!')
    else:
        print('Parece que ele não aprendeu esse truque ainda')
elif novo_comando == 'Dá a patinha':
    if vezes_pata >= 3:
        print('Ele é um bom garoto!')
    else:
         print('Parece que ele não aprendeu esse truque ainda')
elif novo_comando == 'Fica':
    if vezes_fica >= 3:
        if humor != 'Brincalhão':
            print('Ele está aprendendo')
        else:
            print('Ele não consegue ficar parado')
    else:
        print('Parece que ele não aprendeu esse truque ainda')
elif novo_comando == 'Pega':
    if vezes_pega >= 3:
        if humor != 'Preguiçoso':
            print('Ele é muito ágil!')
        else:
            print('Quem não tem seu momento de preguiça?')
    else:
        print('Parece que ele não aprendeu esse truque ainda')

if vezes_senta >= 3 or vezes_pata >= 3 or vezes_fica >= 3 or vezes_pega >= 3:
    print(f'O nosso novo mascote estava {humor} e aprendeu o(s) seguinte(s) truque(s):')
    if vezes_senta >= 3:
        print('Senta')
    if vezes_pata >= 3:
        print('Dá a patinha')
    if vezes_fica >= 3:
        print('Fica')
    if vezes_pega >= 3:
        print('Pega')
