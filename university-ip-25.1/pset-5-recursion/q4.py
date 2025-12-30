#definição de funções
def aprimoramento_armas(arma, nivel):
    entrada = input()
    valido = False
    if entrada == 'fim':
        arma[1] = int(arma[1])
        return arma, nivel
    else:
        entrada = int(entrada)
        if arma[2] == 'basica':
            valido = tribonnaci(entrada, 1, 1, 0)
            if valido:
                if nivel < 20:
                    nivel += 1
                    arma[1] *= 1.1
                    print(f'Pronto, consegui mais um nível agora a/o {arma[0]} está no nível {nivel}!')
        elif arma[2] == 'especial':
            valido = fatorial(entrada, 1, 1)
            if valido:
                if nivel < 10:
                    nivel+= 1
                    arma[1] *= 1.2
                    print(f'Pronto, consegui mais um nível agora a/o {arma[0]} está no nível {nivel}!')
    return aprimoramento_armas(arma, nivel)
def tribonnaci(numero_fim, num_atual, num_anterior, num_ante_previo):
    """checa se um numero está presente na sequencia de tribonnaci, se sim, retorna True, se não, False"""
    if num_atual == numero_fim or numero_fim == 0 or numero_fim == 1:
        return True
    elif num_atual > numero_fim:
        return False
    else:
        proximo_num = num_atual + num_anterior + num_ante_previo
        return tribonnaci(numero_fim, proximo_num, num_atual, num_anterior)
def fatorial(numero_fim, valor_atual, n):
    """checa se o numero faz parte da sequencia fatorial, se sim, retorna true, se nao, false"""
    if valor_atual == numero_fim:
        return True
    elif valor_atual > numero_fim:
        return False
    else:
        proximo_valor = n * valor_atual
        return fatorial(numero_fim, proximo_valor, n+1)

def grande_runas(inputs):
    """recebe uma lista de 10 numeros e retorna se são parte de uma sequencia catalan
    """
    if len(inputs) < 3:
        return False, 0, 0, 0
    primeiro = inputs[0]
    segundo = inputs[1]
    terceiro = inputs[2]
    resto = inputs[1:]
    #variavel
    indice_primeiro = ''
    indice_tentativa = 0
    #acha o indice do primeiro numero, se for de catalan
    acabou = False


    if primeiro == 1:
        if segundo == 1 and terceiro == 2:
            return True, 1, 1, 2
        elif segundo == 2 and terceiro == 5:
            return True, 1, 2, 5
    while not acabou:
        catalan_atual = catalan(indice_tentativa)
        if catalan_atual == primeiro:
            acabou = True
            indice_primeiro = indice_tentativa
        elif catalan_atual > primeiro:
            acabou = True
        else:
            indice_tentativa += 1

    if indice_primeiro != '':
        if primeiro == catalan(indice_primeiro) and segundo == catalan(indice_primeiro+1) and terceiro == catalan(indice_primeiro+2):
            return True, primeiro, segundo, terceiro
    
    #recursao
    return grande_runas(resto)
#fim da definição de funções

def catalan(numero):
    if numero == 0:
        return 1
    else:
        resultado = 0
        for i in range(numero):
            resultado += catalan(i) * catalan(numero - i - 1)
        return resultado
def combate(num_turno, vida_maxima, vida_atual, inimigo, inventario, runa_malenia):
    arma_atual = inventario[0]
    resto = inventario[1:]
    #turno
    print(f'{num_turno}° TURNO')
    print(f'Melhor conferir meus status antes de lutar -> vida: ({vida_atual}/{vida_maxima})')
    print(f'E o {inimigo[0]} ainda está com {inimigo[1]} pontos de vida')
    #ataque
    print(f'Atacando com {arma_atual[0]}.')
    print(f'Consegui causar {arma_atual[1]} de dano no/a {inimigo[0]}!!!')
    print(f'Acabei consumindo a/o {arma_atual[0]}, hora de pegar outra arma do arsenal.')
    inimigo[1] -= arma_atual[1]
    #grande runa de malenia
    if runa_malenia and inimigo[1]>0 and vida_atual < vida_maxima:
        vida_antes = vida_atual
        vida_atual += vida_maxima * 0.05
        vida_atual = int(vida_atual)
        if vida_atual > vida_maxima:
            vida_atual = vida_maxima
        valor_cura = vida_atual - vida_antes
        print(f'Ainda bem que eu ativei a Grande Runa da Malenia, consegui recuperar {valor_cura}')
    #contra-ataque
    if inimigo[1] > 0:
        print(f'Droga {inimigo[0]} ainda não morreu, acabei recebendo {inimigo[2]} de dano.')
        vida_atual -= inimigo[2]
    print('')

    #loop
    if inimigo[1]>0 and vida_atual > 0 and len(resto) > 0:
        return combate(num_turno+1, vida_maxima, vida_atual, inimigo, resto, runa_malenia)
    #fim de batalha
    else:
        if inimigo[1] <= 0:
            print('Great Enemy Felled')
            if len(resto) == 0:
                print(f'Acabei usando tudo que eu trouxe, mas finalmente consegui derrotar a/o {inimigo[0]}.')
            else:
                print(f'Finalmente depois de tanto me preparar consegui derrotar a/o {inimigo[0]}.')
                armas_sobrando = []
                for arma in resto:
                    armas_sobrando.append(arma[0])
                armas_sobrando = ", ".join(armas_sobrando)
                print(f'Acho que me preparei bem eu ainda tenho {len(resto)} arma/as sobrando são ela/as: {armas_sobrando}.')
        elif vida_atual <= 0:
            print('You Died')
            print(f'Droga acabei morrendo para a/o {inimigo[0]} e ele ainda tem {inimigo[1]} pontos de vida, vou ter que trazer armas mais fortes da próxima vez.')
        elif len(resto) == 0:
            print(f'Parece que eu não me preparei o suficiente, acabei usando tudo que tinha e a/o {inimigo[0]} ainda tem {inimigo[1]} pontos de vida, vou ter que me preparar mais da próxima vez.')
        
        return 0
#fim declaração de funções

#inputs
info_maculado = input().split(' - ')
info_maculado[1] = int(info_maculado[1])

qtd_total_acoes = int(input())

#variáveis
inputs_runa = []
inventario = []
runa = ''
runa_tentada = False
runa_godrick = False
runa_malenia = False

for acao in range(qtd_total_acoes):
    info = input()
    #aprimorar arma
    if ' - ' in info:
        nivel = 0
        arma = info.split(' - ')
        arma[1] = int(arma[1])
        print(f'Vou levar a/o {arma[0]} ela/e vai ser de grande ajuda.')
        print('Hora de Aprimorar!!!')
        arma, nivel = aprimoramento_armas(arma, 0)
        inventario.append(arma)
        if nivel > 0:
            print(f'Agora sim! Acho que a/o {arma[0]} está forte o suficiente, consegui colocar ele/a para o nível {nivel}\n')
        else:
            print(f'Droga não consegui aumentar o nível da/o {arma[0]}\n')
    #ativar grande runa
    elif not runa_tentada:
        runa_tentada = True
        #prints
        frase_efeito = ''
        if info == 'Grande Runa de Godrick':
            frase_efeito = 'acho que um pouco de tudo não é nada mal.'
        elif info == 'Grande Runa de Radahn':
            frase_efeito = 'mais vida vai ajudar muito.'
        elif info == 'Grande Runa de Morgott':
            frase_efeito = 'quanto mais vida melhor.'
        elif info == 'Grande Runa de Malenia':
            frase_efeito = 'ela foi tão difícil de conseguir, tenho que testar ela pelo menos uma vez.'
        print(f'A batalha vai ser difícil melhor tentar ativar uma runa!\nMe decidi vou tentar ativar a {info}, {frase_efeito}')
        #checa se conseguiu ou nao
        for i in range(10):
            inputs_runa.append(int(input()))
        pertence, primeiro, segundo, terceiro = grande_runas(inputs_runa)
        if pertence:
            print('Isso consegui ativar a Grande Runa.')
            print(f'Acabei precisando apenas dos números: {primeiro} - {segundo} - {terceiro}.')
            runa = info
            #aplica efeitos da runa
            if runa == 'Grande Runa de Radahn':
                info_maculado[1] += info_maculado[1] * 0.15
                info_maculado[1] = int(info_maculado[1])
            elif runa == 'Grande Runa de Morgott':
                info_maculado[1] += info_maculado[1] * 0.25
                info_maculado[1] = int(info_maculado[1])
            elif runa == 'Grande Runa de Godrick':
                info_maculado[1] += info_maculado[1] * 0.10
                info_maculado[1] = int(info_maculado[1])
                runa_godrick = True
            elif runa == 'Grande Runa de Malenia':
                runa_malenia = True
        else:
            print('Caramba não consegui ativar a Grande Runa, infelizmente vou ter que me contentar com as armas que vou levar.')
        print('') # quebra de linha
#efeitos godrick
if runa_godrick:
    for i in range(len(inventario)):
        inventario[i][1] *= 1.1
        inventario[i][1] = int(inventario[i][1])


#recebe informações do inimigo
info_inimigo = input().split(' - ')
info_inimigo[1] = int(info_inimigo[1])
info_inimigo[2] = int(info_inimigo[2])

#combate
vida_maxima = info_maculado[1]
vida_atual = vida_maxima
turno = 1
combate(turno, vida_maxima, vida_atual, info_inimigo, inventario, runa_malenia)
