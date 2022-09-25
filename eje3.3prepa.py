numero= input(" Por favor ingrese un numero entre 2 y 12")
while not numero.isnumeric() or int(numero) not in range(2,13):
    numero= input("Por favor ingrese un numero entre 2 y 12.")

numero= int(numero)

