#definição de funções
def batalha(atributos_lobo, atributos_geni, turno=1):
    print(f'--- Turno {turno} ---')
    #listas fixas
    lista_acoes_lobo = ['ataque', 'defesa', 'defesa perfeita', 'usar cabaça', 'desviar', 'contra ataque mikiri']
    lista_acoes_geni = ['ataque', 'defesa', 'recuperação de postura', 'ataque kanji']
    #caso genichiro seja posto a 0 ou a 100, pula o turno dele e pega input de ações especiais
    if atributos_geni[1] >= 100 or atributos_geni[0] <= 0:
        print('Genichiro está de joelhos e vulnerável! Acabe com isso, Lobo!')
        acao_lobo = input()
        
        #acoes para geni caido
        if acao_lobo == 'ataque':
            print('Sekiro executa um Golpe Mortal em Genichiro!')
            print('====================================')
            print('Vitória de Sekiro: Golpe Mortal!')
            return 0
        elif acao_lobo == 'hesitar':
            print('O lobo hesitou no seu golpe final, Genichiro recupera sua postura! Cuidado, Lobo!')
            if atributos_geni[1] >= 100:
                atributos_geni[1] -= 50
                if atributos_geni[0] <= 50:
                    atributos_geni[0] = 50
            else:
                atributos_geni[0] = 50
                atributos_geni[1] = 50
    else:
        #pega input de acoes, repete pedido até ser input valido
        acao_geni = input()
        while acao_geni not in lista_acoes_geni:
            print('Genichiro não tem esse movimento em seu arsenal.')
            acao_geni = input()
        acao_lobo = input()
        while acao_lobo not in lista_acoes_lobo:
            print('O lobo não adquiriu esse movimento ainda.')
            acao_lobo = input()

        #acoes no turno
        #para acao de ataque do genichiro
        if acao_geni == 'ataque':
            #respostas do lobo
            if acao_lobo == 'ataque':
                print('Clima de tensão! Os dois atacam numa luta implacável!')
                atributos_lobo[0] -= 25
                atributos_geni[0] -= 10
                atributos_geni[1] += 15
            elif acao_lobo == 'defesa':
                print('Sekiro firma sua espada e se defende, absorvendo o impacto em sua postura!')
                atributos_lobo[0] -= 10
                atributos_lobo[1] += 20
            elif acao_lobo == 'defesa perfeita':
                print('Lâminas se encontram! Um desvio perfeito de Sekiro desequilibra Genichiro!')
                atributos_geni[1] += 25
            elif acao_lobo == 'usar cabaça':
                if atributos_lobo[3] > 0:
                    atributos_lobo[3] -= 1
                    atributos_lobo[0] -= 25
                    print('Sekiro tenta curar, mas é punido pelo ataque impiedoso de Genichiro!')
                else:
                    atributos_lobo[0] -= 25
                    print('Sekiro busca sua cabaça, mas ela está vazia!\nEnquanto Sekiro se distrai, Genichiro avança com um ataque certeiro!')
            elif acao_lobo == 'desviar':
                print('O lobo desvia agilmente do ataque comum de Genichiro!')
            elif acao_lobo == 'contra ataque mikiri':
                print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro faz um movimento comum.')
                atributos_geni[1] += 10
        elif acao_geni == 'defesa':
            if acao_lobo == 'ataque':
                atributos_geni[1] += 5
                print('Genichiro prevê o movimento e apara o golpe de Sekiro com sua lâmina!')
            elif acao_lobo == 'defesa':
                print('Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.')
            elif acao_lobo == 'defesa perfeita':
                print('Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.')
            elif acao_lobo == 'usar cabaça':
                #caso ainda tenha cabaças de cura
                if atributos_lobo[3] > 0:
                    atributos_lobo[3] -= 1
                    atributos_lobo[0] += 25
                    print('Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.')
                else:
                    print('Sekiro busca sua cabaça, mas ela está vazia!\nGenichiro mantém a guarda, enquanto o lobo percebe seu erro.')
            elif acao_lobo == 'desviar':
                print('O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.')
            elif acao_lobo == 'contra ataque mikiri':
                print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.')
        #recuperação de postura
        elif acao_geni == 'recuperação de postura':
            #acoes lobo
            if acao_lobo == 'ataque':
                atributos_geni[0] -= 10
                atributos_geni[1] += 15
                print('Genichiro ia recuperar sua postura mas o lobo foi mais rápido, um grande ataque por parte do lobo!')
            elif acao_lobo == 'defesa':
                atributos_geni[1] = 0
                print('Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
            elif acao_lobo == 'defesa perfeita':
                atributos_geni[1] = 0
                print('Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
            elif acao_lobo == 'usar cabaça':
                if atributos_lobo[3] > 0:
                    atributos_lobo[3] -= 1
                    atributos_lobo[0] += 25
                    atributos_geni[1] = 0
                    print('Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.\nGenichiro consegue recuperar sua postura, cuidado lobo!')
                else:
                    atributos_geni[1] = 0
                    print('Sekiro busca sua cabaça, mas ela está vazia!')
                    print('Genichiro aproveita a hesitação do lobo para recuperar sua postura.')
                    print('Genichiro consegue recuperar sua postura, cuidado lobo!')
            elif acao_lobo == 'desviar':
                atributos_geni[1] = 0
                print('O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.')
                print('Genichiro consegue recuperar sua postura, cuidado lobo!')
            elif acao_lobo == 'contra ataque mikiri':
                atributos_geni[1] = 0
                print('O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.')
                print('Genichiro consegue recuperar sua postura, cuidado lobo!')
        #acao especial
        elif acao_geni == 'ataque kanji':
            if acao_lobo == 'contra ataque mikiri':
                atributos_geni[1] += 25
                print('O lobo utiliza a técnica de contra ataque mikiri e pisa na arma de Genichiro!')
            elif acao_lobo == 'desviar':
                print('O lobo desvia do ataque especial de Genichiro com muita agilidade!')
            #caso não seja uma das ações válidas contra o ataque kanji
            else:
                print('O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!')
                if acao_lobo == 'usar cabaça':
                    if atributos_lobo[3] > 0:
                        atributos_lobo[3] -= 1  
                    else:
                        print('Para piorar, Sekiro nem sequer tinha uma cabaça para usar!')
                atributos_lobo[0] -= 50
                atributos_lobo[1] += 20

    #fim de turno
    #se passado do limite de postura, reseta
    if atributos_lobo[0] <= 0:
        atributos_lobo[0] = 0
    if atributos_geni[0] <= 0:
        atributos_geni[0] = 0
    if atributos_lobo[1] > 100: 
        atributos_lobo[1] = 100
    if atributos_geni[1] > 100: 
        atributos_geni[1] = 100

    #condições de derrota do lobo
    if atributos_lobo[0] <= 0:
        print('Sekiro cai de joelhos, derrotado...')
        print('====================================')
        print('Vitória de Genichiro: Morte.')
        return 0
    elif atributos_lobo[1] >= 100:
        print('A postura do lobo foi quebrada! Ele não consegue se defender e é derrotado!\n====================================\nVitória de Genichiro: Morte.')
        return 0
    #loop recursivo
    else:
        batalha(atributos_lobo, atributos_geni, turno+1)
#fim da definição de funções

#atributos, 0 = vitalidade, 1= postura, 2= postura máxima, 3= cabaças(apenas lobo)
atributos_lobo = [100, 0, 100, 2]
atributos_geni = [100, 0, 100]
#inicio do programa
print('O duelo começa! Suas decisões determinarão o vencedor.')
batalha(atributos_lobo, atributos_geni, 1)
