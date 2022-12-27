numero= int(input('Ingrese un numero positivo: '))
numeros_anterirores= []
for i in range(1,numero+1):
    x= numero - i
    numeros_anterirores.append(x)

for i in numeros_anterirores:
    if i == numeros_anterirores[-1]:
        print(i, end= '.')
    else:
        print(i, end= ', ')

