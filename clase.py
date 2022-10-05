
while True:
    calculador= input(""""Que operacion deseas realizar: 
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Divicion
            5. Salir de la calculadora""")
        
    while  (calculador!= '1' and calculador!='2' and calculador!='3' and calculador!='4' and calculador!='5'):
        calculador =input("Ingrese un numero valido: ")

    if calculador== "1":

        x=(input(" Ingrese un numero:  "))
        while not x.isnumeric():
            x =input("Ingrese un numero valido")

        y=(input(" Ingrese otro numero"))
        while not y.isnumeric():
            y =input("Ingrese un numero valido")

        z=int(x)+int(y)
        print(f"Tu numero es {z}")
    elif calculador== "2":
        x=int(input(" Ingrese un numero"))
        y=int(input(" Ingrese otro numero"))
        z=x-y
        print(f"Tu numero es {z}")
    elif calculador== "3":
        x=int(input(" Ingrese un numero"))
        y=int(input(" Ingrese otro numero"))
        z=x*y
        print(f"Tu numero es {z}")
    elif calculador== "4":
        x=int(input(" Ingrese un numero"))
        y=int(input(" Ingrese otro numero"))
        z=x/y
        print(f"Tu numero es {z}")
    else:
        print('El programa se cerrara.')
        break

    


    

