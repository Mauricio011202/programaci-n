
while True:
    opcion= input("""
                1. Verificar si un numero es narcicista.
                2. Salir
                :""")
    if opcion== "1":
        numero= input("Ingrese un numero entero positivo: ")

        while not numero.isnumeric():
            numero= input("ERROR!! Ingrese un numero entero: ")
        numero_cifras= len(numero)
        suma=0
        for i in numero:

            x=int(i)**numero_cifras
            suma= suma+x
            
        if suma== int(numero):
            print(f"El numero {numero} es narcicista")
        else:
            print(f"El numero {numero} no es narcicista")

        

    
            
    elif opcion== "2":
        break
            
    
    

