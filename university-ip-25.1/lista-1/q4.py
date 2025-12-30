dinheiro_dol = int(input())
cotacao_dolar = float(input())
despesa_racao = int(input())
despesa_aluguel = int(input())
despesa_onibus = int(input())

dinheiro_real = dinheiro_dol * cotacao_dolar
despesa_total = despesa_racao + despesa_aluguel + despesa_onibus
if dinheiro_real > despesa_total:
    print('Me chama pra sua casa um dia pra gente comer Pedigree! Com essa grana dá pra alugar uma ManCão!')
elif dinheiro_real == despesa_total:
    print('Vai dar pra alugar sua casa, mas sugiro que você vá trabalhar se quiser gastar com outra coisa!')
elif dinheiro_real < despesa_total:
    print('Eu acho melhor você ir morar comigo no Cin! O RU é só 4 reais e lá no DA tem saco de dormir!')
maior_gasto = ''
if despesa_racao > despesa_onibus and despesa_racao > despesa_aluguel:
    print('A inflaCão deu pros cachorros, viu! Sugiro que você vá no Coffee Break dos calouros e leve toda a comida!')
    maior_gasto = 'Ração'
elif despesa_aluguel > despesa_onibus and despesa_aluguel > despesa_racao:
    print('Não está fácil pra ninguém... Tenta dividir o aluguel com algum estudante aí!')
    maior_gasto = 'Aluguel'
else:
    print('Você consegue voar, por que quer orçamento de ônibus? Vai ser feliz!')
    maior_gasto = 'Ônibus'

#relatório
print(f'MESADA (dólares): {dinheiro_dol:0.2f} dólares')
print(f'MESADA (reais): {dinheiro_real:0.2f} reais')
print(f'MAIOR GASTO: {maior_gasto}')
