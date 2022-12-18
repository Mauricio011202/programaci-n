numero= int(input("Ingrese el numero al que desee buscarle el cuadrado mas cercano: "))
lista_de_cuadrados= []
for i in range(1,numero):
    x=i*i
    if x <= numero:
        lista_de_cuadrados.append(x)
print(lista_de_cuadrados[-1])


