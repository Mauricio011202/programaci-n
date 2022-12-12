num= input('Ingrese un numero positivo: ')

suma_de_numeros=0

for i in num:
    i= int(i)
    suma_de_numeros+= i

print('La suma de numeros que lo componen es: {}'.format(suma_de_numeros))