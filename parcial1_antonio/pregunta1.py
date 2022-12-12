def acumulado(lst):
    temp = []
    suma = 0
    for item in lst:
        suma += item
        temp.append(suma)
    return temp
    
lista= [1,2,3]
lista_final= acumulado(lista)
print(lista_final)