qtd_pessoas = int(input())
classica = 0
caneta = 0
classineta = 0

for i in range(0, qtd_pessoas):
    voto = input()
    if voto == 'Clássica':
        classica += 1
    elif voto == 'Caneta':
        caneta += 1
    elif voto == 'Classineta':
        classineta += 1
pts_primeiro = max(classica, caneta, classineta)
pts_terceiro = min(classica, caneta, classineta)
if classica != pts_primeiro and classica != pts_terceiro:
    pts_segundo = classica
elif caneta != pts_primeiro and caneta != pts_terceiro:
    pts_segundo = caneta
else:
    pts_segundo = classineta
#primeiro
if classica == pts_primeiro:
    primeiro_lugar = 'Clássica' 
elif caneta == pts_primeiro:
    primeiro_lugar = 'Caneta'
elif classineta == pts_primeiro:
    primeiro_lugar = 'Classineta'

#segundo
if classica == pts_segundo:
    segundo_lugar = 'Clássica' 
elif caneta == pts_segundo:
    segundo_lugar = 'Caneta'
elif classineta == pts_segundo:
    segundo_lugar = 'Classineta'
#terceiro
if classica == pts_terceiro:
    terceiro_lugar = 'Clássica' 
elif caneta == pts_terceiro:
    terceiro_lugar = 'Caneta'
elif classineta == pts_terceiro:
    terceiro_lugar = 'Classineta'

print('Estamos calculando... tão rápido quanto dar Run no Dikastis...')
print(f'1º lugar: {primeiro_lugar} ({pts_primeiro} votos)')
print(f'2º lugar: {segundo_lugar} ({pts_segundo} votos)')
print(f'3º lugar: {terceiro_lugar} ({pts_terceiro} votos)')

if primeiro_lugar == 'Clássica':
    if (pts_primeiro - pts_segundo) >= 5:
        print('Podemos ver que a influência do grande Hugo Calderano foi disseminada pelos corredores do CIn!')
