#Los ciclos son funciones que nos permiten hacer una secuencia 
#Listas son estrucuturas de datos que funcina como una secuencia de elementos muutablesyordenados, son mutables porque pueden alterar cualquier valor
#Indexing es la posicion delos elementos, es pueden contar de atras hacia  delante 
#para acceder a cualquier elemento deuna lista usamos []
#para elegir una seie de elementos es [1: 5] y el ultimo numero toma hasta  n-1

#insert()para agregar un elemento a una lista 
from itertools import count
from math import factorial


lista= [1, 2, 3]
lista.insert(4, 4)
print(lista)
# CICLOS
#While se ejecuta mientras una determinada concion se ejecuta

factorial= 1
n= 5
count= 1
while count<= n:
    factorial*= count
    count+= 1
print(factorial)
#Interar ns permiete recorrer uno a uno cada elemnto
#Ciclofor 
ciudades= ['Caracas', 'Valencia', 'Margarita', 'Maracay']

for index in range(len(ciudades)):
    ciudades[index].title
    print(ciudades[2].lower)
    
