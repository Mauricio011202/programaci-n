figura= int(input('Eliga una figura: \n 1. Triangulo \n 2. Circulo \n 3. Cuadrado->\n'))
if figura == 1:
    base= float(input("Ingrese la base"))
    altura= float(input("Ingrese la altura")) 
    print(f'El area de triangulo es {(base*altura)/2} ')
elif figura == 2:
    radio= float(input("Ingrese el radio"))
    
    print(f'El area de circulo es {(radio**2)*3.1416} ')
elif figura== 3:
    base= float(input("Ingrese la base"))
    
    print(f'El area de triangulo es {(base**2)} ')
else:
    print('Su ingrso no es valido')
    

