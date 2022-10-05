from re import I


numero= input("Ingrese un numero entero: ")
if numero.isnumeric():
    numero  =int(numero)
    for numero_for in range(1,numero+1):
        print("*"*numero_for)
else:
    print("Inavlida opcion")