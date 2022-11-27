numero= input("ingrese un numero entero positivo")
aux= 1
if numero.isnumeric():
    numero= int(numero)
    while aux <= numero:
      if aux+2 >= numero:
        print(aux)
    

else:
    print(aux, end=",")
    aux+=2
