

def buscador(lista,numero):
    for i in lista:
        for x in i:
            if x  ==numero:
                return True
    return False

def eliminador(lista,numero):
    for i in lista:
        for x in i:
            if x  ==numero:
                i.remove(x)
            return lista

def main():
    lista=[[1,2],[3,4]]
    while True:
        opcion=input("Ingrese una opcion valida\n1.  Buscar  un numero \n 2. Elimminar un numero encontrado\n3. salir ")
        if opcion== "1":
            numero= int(input("Ingrese un numero"))
            numero_en_lista=buscador(lista,numero)
            if numero_en_lista== True:
                print("El numero si esta en la lista")
            else:
                print("El numero no esta en la lista")
        elif opcion== "2":
            numero= int(input("Ingrese un numero"))
            numero_en_lista=buscador(lista,numero)
            numero_a_elim= eliminador(lista, numero)

            print(lista)

    
    
main()
