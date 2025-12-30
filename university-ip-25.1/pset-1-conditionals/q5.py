visto_byte = False
cachorro_ganhador = False

nome_cao1 = input()
pontos1_prova1 = int(input())
pontos1_prova2 = int(input())
pontos1_prova3 = int(input())
soma1 = pontos1_prova1 + pontos1_prova2 + pontos1_prova3

if nome_cao1 == 'Byte':
    print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')
    visto_byte = True
elif soma1 == 30 and not visto_byte:
    print(f'Com uma pontuação perfeita, {nome_cao1} conquista o título de mascote do CIn!')
    cachorro_ganhador = True
if not visto_byte and not cachorro_ganhador:
    nome_cao2 = input()
    pontos2_prova1 = int(input())
    pontos2_prova2 = int(input())
    pontos2_prova3 = int(input())
    soma2 = pontos2_prova1 + pontos2_prova2 + pontos2_prova3
    if nome_cao2 == 'Byte':
        print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')
        visto_byte = True
    elif soma2 == 30 and not visto_byte:
        print(f'Com uma pontuação perfeita, {nome_cao2} conquista o título de mascote do CIn!')
        cachorro_ganhador = True

if not visto_byte and not cachorro_ganhador:
    nome_cao3 = input()
    pontos3_prova1 = int(input())
    pontos3_prova2 = int(input())
    pontos3_prova3 = int(input())
    soma3 = pontos3_prova1 + pontos3_prova2 + pontos3_prova3
    if nome_cao3 == 'Byte':
        print('Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!')
        visto_byte = True
    elif soma3 == 30 and not visto_byte:
        print(f'Com uma pontuação perfeita, {nome_cao3} conquista o título de mascote do CIn!')
        cachorro_ganhador = True

if not visto_byte and not cachorro_ganhador:
    if soma1 < 15:
        print(f'Infelizmente {nome_cao1} está fora da disputa')
    if soma2 < 15:
        print(f'Infelizmente {nome_cao2} está fora da disputa')
    if soma3 < 15:
        print(f'Infelizmente {nome_cao3} está fora da disputa')
    vencedor = max(soma1, soma2, soma3)
    if soma1 == vencedor:
        print(f'Após uma disputa acirrada, o novo mascote do CIn é {nome_cao1}!')
    elif soma2 == vencedor:
        print(f'Após uma disputa acirrada, o novo mascote do CIn é {nome_cao2}!')
    else:
        print(f'Após uma disputa acirrada, o novo mascote do CIn é {nome_cao3}!')
