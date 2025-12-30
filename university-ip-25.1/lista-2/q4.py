f_max = int(input())
forca_inicial = int(input())
nivel = input()
forca_jogador = int(input())
tempo = 0
F_rebatida = 0
forca_total_acumulada = 0
media_robo = 0
encerrar_partida = False
#inicialização programa
print('Robô Hugo 4.0 foi inicializado…')
if nivel == 'facil':
    print('Iniciando no modo iniciante... Ótimo para aquecer os motores!')
    incremento = 1
elif nivel == 'medio':
    print('Você escolheu o modo intermediário. Hora de mostrar técnica e estratégia!')
    incremento = 3
elif nivel == 'dificil':
    print('Modo lendário ativado! Hugo 4.0 está a todo vapor — prepare-se para o combate definitivo!')
    incremento = 5

#partida
while encerrar_partida != True:
    tempo += 1
    F_rebatida = forca_inicial + (tempo * incremento)
    if F_rebatida > 150:
        encerrar_partida = True
    else:
        forca_total_acumulada += F_rebatida
        print(f'Rebatida {tempo}: força = {F_rebatida}, força acumulada = {forca_total_acumulada}')
        if forca_total_acumulada > f_max:
            encerrar_partida = True
else:
    if forca_total_acumulada > f_max:
        print('Energia do robô esgotada! Encerrando o confronto…')
    elif F_rebatida > 150:
        print('Bola fora! A força da rebatida excedeu os limites da mesa.')
media_robo = forca_total_acumulada // tempo
#fim do programa
print(f'Partida finalizada! Estas são as estatísticas do embate:\nO robô realizou {tempo} rebatidas em {tempo} segundos, com força total de {forca_total_acumulada}.')
print(f'Força média do robô: {media_robo}\nForça média do jogador: {forca_jogador}')
if media_robo > forca_jogador:
    print('Vitória do Hugo 4.0! O robô mostrou quem manda na quadra!')
elif media_robo < forca_jogador:
    print('Vitória do jogador! O talento humano ainda é imbatível!')
elif media_robo == forca_jogador:
    print('Empate técnico! Um duelo digno de mestres do tênis de mesa.')
