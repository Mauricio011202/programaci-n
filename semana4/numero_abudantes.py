
numero1=int(input('Ingrese un numero entero'))


lista1= []



for i in range(1,numero1):
        if numero1%i== 0:
         lista1.append(i)

sum_list1= sum(lista1)
if sum_list1>numero1:
    print('El numero es abundante')
else:
    print('No es abundante')