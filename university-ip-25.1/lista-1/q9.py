dia_semana = input()
turno = input()

if dia_semana == 'segunda-feira' or dia_semana == 'sexta-feira':
    hora = int(input())

local = input()
humor_Byte = input()

#dia da semana
if dia_semana == 'segunda-feira':
    if hora <= 7:
        print('Byte acordou em plena madrugada, quem tá acordado(a) pra levar ele essa hora?!')
elif dia_semana == 'sexta-feira':
    if hora >= 16:
        print('SEXTOU, quem vai levar Byte pra bater pata por aí??')

#local
if local == 'labirinto':
    print('Byte quer passear num labirinto, cuidado pra não se perder!')

#humor
if humor_Byte == 'pura energia':
    print('Byte está energizado com a ideia de passear, leve uma bolinha pra ele!')
elif humor_Byte == 'calminho':
    print('Byte está calminho, o passeio vai ser na paz, pode confiar!')
elif humor_Byte == 'rebelde':
    print('Byte está se comportando mal hoje, vamos ver quem terá coragem para acompanhá-lo em seu passeio')

#acompanhante
#1
if local == 'labirinto' and humor_Byte != 'rebelde':
    print('A prof. Fernanda Madeiral aceitou o desafio: labirinto caótico, uma Python no caminho… e Byte como companheiro. Afinal, o que pode dar errado?')

elif local == 'labirinto' and humor_Byte == 'rebelde':
    print('Mestre Iyoda e Byte adentram o labirinto. Uma missão ousada e um destino desconhecido.')

elif turno == 'manhã' and dia_semana != 'segunda-feira':
    print(f'Nesta manhã de {dia_semana}, é o Prof. Sergio Soares quem comanda o passeio com Byte')

elif turno == 'manhã' and dia_semana == 'segunda-feira' and (local == 'parque' or local == 'bosque'):
    print(f'{dia_semana}: uns indo pro trabalho, outros lidando com o Byte. Prof. Ricardo Massa escolheu a segunda opção. Força, guerreiro. {local}, aí vamos nós.')

elif turno == 'tarde' and (local == 'parque' or local == 'bosque'):
    print('Sol da tarde, coleira na mão: prof. Ricardo Massa entra em cena para o passeio com Byte.')

elif turno == 'noite' and (local == 'parque' or local == 'bosque'):
    print(f'Quando a noite cai e Byte chama, Mestre Iyoda atende. Que o {local} esteja preparado para essa dupla!')
