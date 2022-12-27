frase= input('Ingrese una frase: ')
letra= input('Ingrese una letra: ')
contador= 0
for le in frase:
    if le == letra:
        contador+= 1

if contador== 0:
    print('Esa letra no esta la frase')
else:
    print(f'La letra {letra} se encuentra {contador} veces en la frase')
