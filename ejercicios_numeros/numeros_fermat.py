numero= input('Ingrese un numero: ')
while not numero.isnumeric():
    numero= input('Ingrese un numero natural mayor que 0: ')

    while not int(numero)>=0:
        numero= input('Ingrese un numero natural mayor que 0: ')
        
        if numero.isnumeric():
         numero2= 2**(2**int(numero))+1
        for n in range(2, numero2):
                if (numero2%n==0):
                    print(f"el numero {numero} no es un numero primo de format. ")
                    break
        print(f"El numero {numero} si es primode fermat porque {numero2} es primo ")

