numero= int(input('Ingrese un numero entero: '))
contador=0
primo= False
for i in range(2, numero):
    if numero%i== 0:
        primo=False
    else:
        primo=True

print(primo)

        