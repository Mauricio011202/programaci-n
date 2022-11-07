contador=0
numeros_divisores=[]
primo=[]
while True:
        numero= input("Ingrese un numero entero positivo: ")

        while not numero.isnumeric():
            numero= input("ERROR!! Ingrese un numero entero: ")
            
        suma=0    
        for i in range(1, int(numero)):
            if int(numero)%i== 0:
                numeros_divisores.append(i)
                 
        suma=sum(numeros_divisores)
        
        for i in range(1,suma):
            if suma%i== 0:
                contador+=i
        if contador==suma:
            print("el numero es ambicioso")
        elif contador!= suma:
           print("el numero no es ambicioso") 
        break