count= 0
palabra=input("Ingrese una palabra: ")
while not palabra.isalpha():
    palabra=input("Ingrese un dato valido por favor!")
while count <= 10:
    print(palabra.capitalize())
    count+= 1
    