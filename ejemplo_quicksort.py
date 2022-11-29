lista= [3,5,4,7,2,1,0,8,9,100]

def quick_sort(lista):
    if len(lista)<2:
        return lista
    menor,pivote,mayor=partition(lista)
    return quick_sort(menor)+[pivote]+quick_sort(mayor)
def partition(lista):
    menores=[]
    mayores=[]
    pivote=lista[0]
    for i in range(len(lista)):
        if lista[i]<pivote:
            menores.append(lista[i])
        elif lista[i]>pivote:
            mayores.append(lista[i])
    return menores, pivote, mayores

print(quick_sort(lista))