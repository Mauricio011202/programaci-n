numero= input("Ingrese un numero entero mayor que 0")
while not numero.isnumeric() or int(numero)<= 0:
    print("Ingrese undato valido")
    break
while int(numero)>+ 10:
    suma= 0
    for i in str(numero):
        suma+= int(i)
        numero= suma
print(f"El numero es {numero} ")

