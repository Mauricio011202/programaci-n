numero= input("Ingrese un numero entero")
if numero.isnumeric():
    numero  =int(numero)
    for i in range(1,numero+1,2):
        aux= i
        while aux>= 1: 
          if aux == 1:
            print(aux)
          else:
            print(aux, end= " ")
          aux-=2


else:
    print("Ingrese un numero valido")