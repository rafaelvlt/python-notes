monitor1 = int(input())
monitor2 = int(input())
monitor3 = int(input())
monitor4 = int(input())
monitor5 = int(input())

resultado = (monitor1 + monitor2 + monitor3 + monitor4 + monitor5) % 5
if resultado == 0:
    print('Arthur vai ter a honra de passear com Byte hoje!')
elif resultado == 1:
    print('Bruna vai ter a honra de passear com Byte hoje!')
elif resultado == 2:
    print('César vai ter a honra de passear com Byte hoje!')
elif resultado == 3:
    print('Daniel vai ter a honra de passear com Byte hoje!')
elif resultado == 4:
    print('Eduarda vai ter a honra de passear com Byte hoje!')
