#declaração de funções
def calcular_dano(tipo_golpe, multiplicador):
    """calcula e retorna o dano(int) do ataque dependendo do tipo e motivação"""
    resultado = 0
    if tipo_golpe == 'Normal':
        resultado = 20 * multiplicador
    else:
        resultado = 40 * multiplicador
    return int(resultado)
def simular_batalha(mot_veg, oponente, vida_oponente ):
    """retorna oponente derrotado(bool), vida restante vegeta(int)"""
    print(f'--- Iniciando o combate contra {oponente} ---\n')
    oponente_caiu = False
    vida_restante = 0
    motivacao_guerreiroz = float(input())
    vida_vegeta = 100
    turno = 1
    qtd_potentes = 0
    acabou = False
    while not acabou:
        print(f'--- Turno {turno} ---')
        #acoes do vegeta
        acao_lutador = input()
        #checa se foram dois golpes potentes seguidos dependendo da acao, se sim termina o combate
        if acao_lutador == 'Potente':
            qtd_potentes += 1
            if qtd_potentes == 2:
                print('Vegeta usou dois Golpes Potentes seguidos e desmaiou com o esforço!')
                acabou = True
                vida_vegeta = 0
                vida_restante = vida_vegeta
                oponente_caiu = False
        else:
            qtd_potentes = 0
        if not acabou:
            dano = calcular_dano(acao_lutador, mot_veg)
            vida_oponente -= dano
            print(f'Vegeta usou Golpe {acao_lutador} e causou {dano} de dano!')
        
        #acoes do oponente se não tiver sido derrotado
        if not vida_oponente <= 0 and not acabou:
            acao_lutador = input()
            dano = calcular_dano(acao_lutador, motivacao_guerreiroz)
            vida_vegeta -= dano
            print(f'{oponente} usou Golpe {acao_lutador} e causou {dano} de dano!')

        #decide ganhador e a vida restante
        if vida_vegeta <= 0:
            oponente_caiu = False
            vida_vegeta = 0
            vida_restante = 0
            acabou = True
        elif vida_oponente <= 0:
            oponente_caiu = True
            vida_oponente = 0
            vida_restante = vida_vegeta  
            acabou = True
        #printa status e incrementa o turno
        print(f'|Vegeta: {vida_vegeta} HP vs {oponente}: {vida_oponente} HP|\n')
        turno += 1
            
    return oponente_caiu, vida_restante 

def venceu_ou_perdeu(oponente_derrotado, nome_oponente, vida_restante):
    """printa a mensagem dependendo se vegeta venceu ou perdeu, retorna 0 caso perdeu, retorna 1 caso venceu"""
    if oponente_derrotado:
        print('Vitória de Vegeta!')
        print(f'Vegeta venceu a batalha contra {nome_oponente} com {vida_restante} HP restantes!\n')
        return 1
    else:
        print(f'Vegeta foi derrotado! A Terra está a salvo graças a {nome_oponente}!')
        return 0
#fim de declaração das funções

#variaveis 
motivacao_vegeta = float(input())
vida_inicial_oponente = 100
oponente_derrotado = True
ordem_luta = 1
vitorias = 0

#loop da simulação
print('A saga de Vegeta começa!\n')
while ordem_luta < 4 and oponente_derrotado == True:
    if oponente_derrotado:
        if ordem_luta == 1: 
            #simula a batalha vs piccolo, retorna se foi derrotado e a vida restante de vegeta
            oponente_derrotado, vida_restante_vegeta = simular_batalha(motivacao_vegeta, 'Piccolo', vida_inicial_oponente)
            #vê quem venceu e printa a mensagem de acordo, também incrementando o numero de vitórias caso tenha vencido
            vitorias += venceu_ou_perdeu(oponente_derrotado, 'Piccolo', vida_restante_vegeta)    
        elif ordem_luta == 2:
            oponente_derrotado, vida_restante_vegeta = simular_batalha(motivacao_vegeta, 'Gohan', vida_inicial_oponente)
            vitorias += venceu_ou_perdeu(oponente_derrotado, 'Gohan', vida_restante_vegeta)
        elif ordem_luta == 3:
            vida_inicial_oponente = 200
            oponente_derrotado, vida_restante_vegeta = simular_batalha(motivacao_vegeta, 'Goku', vida_inicial_oponente)
            vitorias += venceu_ou_perdeu(oponente_derrotado, 'Goku', vida_restante_vegeta)
    
    if oponente_derrotado:
        #após vitória, muda dinamicamente a motivacao de vegeta
        motivacao_vegeta = motivacao_vegeta * (1 +(vida_restante_vegeta / vida_inicial_oponente))
    ordem_luta += 1
#print caso tenha derrotado todos guerreiros Z
if vitorias == 3:
    print('Vegeta derrotou todos os Guerreiros Z! A Terra foi conquistada!')
