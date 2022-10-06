


numero1=int(input('Ingrese un numero entero'))
numero2=int(input('Ingrese un numero entero'))

lista1= []
lista2= []


for i in range(1,numero1):
    if numero1%i== 0:
        lista1.append(i)


for i in range(1,numero2):
    if numero2%i== 0:
        lista2.append(i)


sum_list1= sum(lista1)
sum_list2= sum(lista2)
if sum_list1== numero2 or sum_list2== lista1:
        print("las parejas de numeros son amigos")
else:
    print('los numeros no son amigos')