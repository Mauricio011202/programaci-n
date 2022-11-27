lista= [1, 2, 3, 4, 5, 6]
lista2= []
count=0
for i in lista:
    if count%2==1:
        count+=1
        i= i**2
        lista2.append(i)
    else:
        lista2.append(i)
        count+=1
print(lista2)