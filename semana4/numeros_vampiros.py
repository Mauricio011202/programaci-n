numero= int((input("Ingrese un numero de 3 digitos")))

confirmar= list(numero)
while len(confirmar) >= 4:
    numero= input('Ingrese un numero valido: ')
    confirmar= list(numero)

conseguido= True
while 6< len(confirmar):
    vampiro=str(confirmar[1])+str(confirmar[2])
    vampiro= int(vampiro)
    total= int(confirmar[0]*vampiro)
    