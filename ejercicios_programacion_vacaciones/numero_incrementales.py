numero= input(' Ingrese un numero de 3 cifras: ')
while not numero.isnumeric() or len(numero)==2:
    numero= input('ERROR! Ingrese un numero de 3 cifras: ')
lista_num= []
for i in numero:
    x= int(i)
    lista_num.append(x)
if lista_num[0] < lista_num[1] and lista_num[1]  < lista_num[2] :
    print(f'el numero {numero} es ascendente.')
else:
    print(f'el numero {numero} es descendente.')