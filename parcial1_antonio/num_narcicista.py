numero= input('Ingreseun numero entero: ')

potencia= len(numero)

suma=0
for digito in numero:
    suma+= int(digito)**potencia

if suma== int(numero):
    print('El numero es narcicista')

else :
    print('El numero no es narcicista')