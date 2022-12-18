num= input("Ingrese un numero del que desee saber su factorial: ")
num = int(num)
lista_numero_a_multiplicar= []
for i in range(1,num+1):
    lista_numero_a_multiplicar.append(i)
factorial=1
for i in lista_numero_a_multiplicar:
    
    factorial= factorial*i
print(factorial)

    

   