#inicio
print('🎾🏆 Bem-vindo ao Torneio Fatorial Ping Pong Championship! 🧮🏓\nHoje, o jovem Lavoi enfrentará seu maior desafio: CÁLCULOS!\n')
#numeros pedidos e checagens
print('Qual será o número que marcará o INÍCIO dessa tabuada fatorial?')
numero_inicio = int(input())
if numero_inicio < 0:
    while numero_inicio < 0:
        print(f'O número {numero_inicio} é inválido! O INÍCIO NÃO pode ser NEGATIVO.')
        numero_inicio = int(input())
print(f'O número {numero_inicio} é ótimo como número inicial!')
print('')

print('Qual será o número que marcará o FIM dessa tabuada fatorial?')
numero_fim = int(input())
if numero_fim < numero_inicio:
    while numero_fim < numero_inicio:
        print(f'O número {numero_fim} é inválido! O FIM NÃO pode ser MENOR que o número inicial {numero_inicio}.')
        numero_fim = int(input())
print(f'O número {numero_fim} é ótimo como número final!')
print('')

print('Qual será o número cujo FATORIAL será calculado?')
numero_sagrado = int(input())
if numero_sagrado < 0:
    while numero_sagrado < 0:
        print(f'O número {numero_sagrado} é inválido! Números válidos são maiores ou iguais a zero.')
        numero_sagrado = int(input())
print(f'O número {numero_sagrado} é ótimo para o cálculo do fatorial!')
print('')


for i in range(numero_inicio, numero_fim+1):
    fatorial = 0
    for j in range((i * numero_sagrado) + 1):
        if j == 0:
            fatorial = 1
        else:
            fatorial *= j 
    print(f'({i} * {numero_sagrado})! = {fatorial}')

print('')
print('🏁 Jornada Finalizada! Lavoi completou todos os estágios do desafio!')
print('🏓 Que sua energia vital continue brilhando nas próximas batalhas!')
