num= input('Ingrese un numero tope para la serie fibonacci: ')
num= int(num)

a= 0
b= 1
aux= None
lista_fibo= []

for i in range(num):
    lista_fibo.append(a)
    aux= a
    a = b
    b = aux + a

print(lista_fibo)