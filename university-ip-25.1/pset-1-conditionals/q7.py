lugar = input()
x_inicial = 500
y_inicial = 100

if lugar == 'Concha Acústica da UFPE':
    ponto_x = 400
    ponto_y = 500
elif lugar == 'Laguinho da UFPE':
    ponto_x = 300
    ponto_y = 1000
elif lugar == 'Hospital das Clínicas':
    ponto_x = 1000
    ponto_y = 1000
elif lugar == 'Ginásio e Pista de Atletismo da UFPE':
    ponto_x = 800
    ponto_y = 100

distancia = ((ponto_x - x_inicial)**2 + (ponto_y - y_inicial)**2)**(1/2)
distancia_total = distancia * 2
distancia_formatada = round(distancia_total)
tempo_gasto = round((distancia_total/120) + 15)

print(f'Byte visitou {lugar}, caminhou {distancia_formatada} metros e gastou {tempo_gasto} minutos passeando!')

if lugar == 'Concha Acústica da UFPE':
    print('Aqui é muito grande mesmo! Muitos eventos ocorrem por aqui!')
elif lugar == 'Laguinho da UFPE':
    print('Nossa, mas esse lago é longe hein?!')
elif lugar == 'Hospital das Clínicas':
    print('Um dos hospitais mais importantes do estado também fica na área do Campus da UFPE!')
elif lugar == 'Ginásio e Pista de Atletismo da UFPE':
    print('Que legal! O Ginásio é bem perto do CIn!')
