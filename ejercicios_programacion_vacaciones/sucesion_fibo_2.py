x= 0
y =1
num=1000
lista_fibo= []
aux= None
for i in range(1,num):
    lista_fibo.append(x)
    aux= x
    x= y
    y= aux + x
    if len(lista_fibo) == 10:
        break
print(lista_fibo)

    
