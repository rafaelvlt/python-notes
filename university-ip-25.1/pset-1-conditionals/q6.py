nome_1 = input()
indicador_1 = input()
pontos_1 = len(nome_1)

nome_2 = input()
indicador_2 = input()
pontos_2 = len(nome_2)

nome_3 = input()
indicador_3 = input()
pontos_3 = len(nome_3)

gato_avistado_1 = False
gato_avistado_2 = False
gato_avistado_3 = False

if 'gato' in nome_1:
    pontos_1 = 0
    gato_avistado_1 = True
if 'gato' in nome_2:
    pontos_2 = 0
    gato_avistado_2 = True
if 'gato' in nome_3:
    pontos_3 = 0
    gato_avistado_3 = True

inimigo = ''
if indicador_1 == 'felino espião':
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')
    inimigo = nome_1
    pontos_1 = 0

if 'cin' in nome_1 and nome_1 != inimigo and not gato_avistado_1:
    print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')
    pontos_1 += 10

if indicador_2 == 'felino espião':
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')
    inimigo = nome_2
    pontos_2 = 0

if 'cin' in nome_2 and nome_2 != inimigo and not gato_avistado_2:
    print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')
    pontos_2 += 10

if indicador_3 == 'felino espião':
    print('Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.')
    inimigo = nome_3
    pontos_3 = 0
if 'cin' in nome_3 and nome_3 != inimigo and not gato_avistado_3:
    print('Os melhores nomes são aqueles que fazem referência a minha casinha :)')
    pontos_3 += 10

#ranking

if pontos_1 > pontos_2 and pontos_1 > pontos_3:
    nome_primeiro_lugar = nome_1
    if pontos_2 > pontos_3:
        nome_segundo_lugar = nome_2
        nome_terceiro_lugar = nome_3
    else:
        nome_segundo_lugar = nome_3
        nome_terceiro_lugar = nome_2

elif pontos_2 > pontos_1 and pontos_2 > pontos_3:
    nome_primeiro_lugar= nome_2
    if pontos_1 > pontos_3:
        nome_segundo_lugar = nome_1
        nome_terceiro_lugar = nome_3
    else:
        nome_segundo_lugar = nome_3
        nome_terceiro_lugar = nome_1
elif pontos_3 > pontos_1 and pontos_3 > pontos_2:
    nome_primeiro_lugar= nome_3
    if pontos_1 > pontos_2:
        nome_segundo_lugar = nome_1
        nome_terceiro_lugar = nome_2
    else:
        nome_segundo_lugar = nome_2
        nome_terceiro_lugar = nome_1

print('RANKING DOS NOMES:')
print(f'Primeiro lugar: {nome_primeiro_lugar}')
print(f'Segundo lugar: {nome_segundo_lugar}')
print(f'Terceiro lugar: {nome_terceiro_lugar}')
