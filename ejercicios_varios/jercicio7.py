numero= int(input('ingrese un numero'))
aux= numero-1
acumulador= 0
while aux >= 1:
    if numero%aux == 0:
        acumulador+= aux
    aux-= 1
if acumulador > numero:
    print(f'El numero{numero}es abundnte')
else:
    print(f"El numero {numero} no es abundante")
