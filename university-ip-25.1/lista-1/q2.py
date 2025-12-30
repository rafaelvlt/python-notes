nome_aluno = input()
notas1 = int(input())
notas2 = int(input())
notas3 = int(input())
notas4 = int(input()) * 10/6
notas5 = int(input()) * 10/6
notas6 = int(input()) * 10/6

media_geral = (notas1 + notas2 + notas3 + notas4 + notas5 + notas6)/6
print(f'A média de {nome_aluno} é {media_geral:0.1f}')

if notas2 >= notas1 and notas3 >= notas2 and notas4 >= notas3 and notas5 >= notas4 and notas6 >= notas5:
    print('Progresso constante! Parabéns pelo esforço!')
else:
    print('Alerta! Queda no rendimento.')

faltas = 0
if notas1 == 0:
    faltas += 1
if notas2 == 0:
    faltas += 1
if notas3 == 0:
    faltas += 1
if notas4 == 0:
    faltas += 1
if notas5 == 0:
    faltas += 1
if notas6 == 0:
    faltas += 1

if faltas >= 2:
    print('Alerta! Múltiplas listas não respondidas.')

if media_geral < 7:
    print('Alerta! Desempenho abaixo do esperado.')
elif media_geral < 8:
    print('Parabéns pelo bom desempenho!')
elif media_geral >= 8:
    print('Parabéns pelo excelente desempenho! Continue "au" sim.')
