#definição de função
def descriptografar(nome_criptografado):
    """recebe um nome criptografado, realiza a descriptografia e retorna"""
    ascii_chars = (
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?',
    '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_',
    '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~')

    #divide o nome criptografado em duas partes
    tamanho = len(nome_criptografado)
    parte1 = list(nome_criptografado[0:tamanho//2]) 
    parte2 = list(nome_criptografado[tamanho//2:])

    #shift -1 parte 2
    for i in range(len(parte2)):
        index = ascii_chars.index(parte2[i]) + 1
        if index >= len(ascii_chars):
            index = index - len(ascii_chars)
        parte2[i] = ascii_chars[index]
    #concatenando e desinvertendo
    lista_concat = parte1 + parte2
    lista_concat = lista_concat[::-1]

    #descriptografai final
    for i in range(len(lista_concat)):
        index = ascii_chars.index(lista_concat[i]) - 3
        if index < 0:
            index = index + len(ascii_chars)
        lista_concat[i] = ascii_chars[index]
    nome_descriptografado = "".join(lista_concat)
    return nome_descriptografado
#fim da declaração de funções

qtd_nomes = int(input())
#pega os nomes
dicionario_cripto = {}
for i in range(qtd_nomes):
    dicionario_cripto[i] = input()

#descriptografa
dicionario_descripto = {}
for i in range(qtd_nomes):
   dicionario_descripto[i] = descriptografar(dicionario_cripto[i])

#fase 1
for i in range(qtd_nomes):
    print(f'Criptografada: {dicionario_cripto.get(i)}')
    print(f'Descriptografada: {dicionario_descripto.get(i)}')
    print('-' * 50)
#fase 2
#separa os jogadores e técnicos em dicionarios diferentes
jogadores = {}
tecnico = {}
for i in range(qtd_nomes):
    nome = dicionario_descripto.get(i)
    if nome == 'Ronaldo':
        print('Ronaldo Fenômeno detectado! Autor dos gols na final!')
        jogadores[i] = nome
    elif nome == 'Ronaldinho':
        print('Ronaldinho Gaúcho chegou! Chamem o inglês que ele vai chutar do meio-campo...')
        jogadores[i] = nome
    elif nome == 'Cafu':
        print('Capitão Cafu presente! O único a jogar 3 finais de Copa seguidas!')
        jogadores[i] = nome
    elif nome == 'Marcos':
        print('Marcos está na área! O paredão do Brasil em 2002!')
        jogadores[i] = nome
    elif nome == 'Luiz Felipe Scolari':
        print('Técnico reconhecido: Luiz Felipe Scolari — o comandante do penta!')
        tecnico[0] = 'Luiz Felipe Scolari'
    else:
        print(f'{nome} está confirmado na escalação!')
        jogadores[i] = nome
#fase 3
print('')
#print para jogadores
if len(jogadores) < 11:
    print('!!!!!!!!!! Escalação incompleta! !!!!!!!!!!')
    print(f'Só foram encontrados {len(jogadores)} jogadores. Faltam jogadores para completar o time.')
elif len(jogadores) >= 11:
    print('++++++++++ Escalação Confirmada ++++++++++')
    print(f'Escalação Oficial da Seleção Brasileira — Copa do Mundo 2002')
    print('==================================================')
    for jogador in jogadores:
        print(f'->{jogadores.get(jogador)}')
    print('==================================================')

#print pro tecnico
if len(tecnico) == 0:
    print('!!!!!!!!!! Técnico não encontrado! !!!!!!!!!!')
    print('Como vamos jogar sem treinar? Como vamos ganhar o penta?')
else:
    print('========== Técnico ==========')
    print('Luiz Felipe Scolari (Felipão)')

#se tiver completo
if len(jogadores) >= 11 and len(tecnico) > 0:
    print('===== Tudo pronto! Rumo ao Penta! =====')
    print('Escalação completa com técnico confirmado.\nQue comece o espetáculo, Brasil rumo ao penta!')
