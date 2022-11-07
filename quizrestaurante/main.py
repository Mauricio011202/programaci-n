from alimentos import Alimento, Comida, Bebida
from persona import Persona

Alimento
def inputstr(entrada):
    string= input(f'Por favor ingrese {entrada}:')
    while not string.isalpha():
        string= input(f'Error! Por favor ingrese {entrada}:')
    return string

def inputint(entrada):
    numero= input(f'Por favor ingrese {entrada}:')
    while not numero.isnumeric() :
        numero= input(f'Error! Por favor ingrese {entrada}:')
    return int(numero)



def main():

    

    print ('Bienvenido a mi restaurante el poke.')
    facturacion= {'comida': [], 'persona': ""}
    while True:
        
        opcion= input("Ingrese una opcion \n 1. Pedir una comida \n 2. Pedir una bebida \n 3. Pedir factura")
        while opcion not in['1', '2', '3', '4']:
            opcion= input("Ingrese una opcion \n 1. Pedir una comida \n 2. Pedir una bebida \n 3. Pedir factura")
        if opcion== '1':
            nombre= inputstr('nombre')
            precio= inputint('precio')
            tipo= inputstr('tipo')
            sabor= inputstr('sabor')
            Comida(nombre,precio, tipo, sabor)
            facturacion['comida'].append(Comida(nombre,precio, tipo, sabor))
        elif opcion == '2':
            nombre= inputstr('nombre')
            precio= inputint('precio')
            grado_alcohol= inputstr('grado_alcohol')
            temperatura= inputstr('temperatura')
            Bebida(nombre,precio,grado_alcohol, temperatura)
            facturacion['comida'].append(Bebida(nombre,precio,grado_alcohol, temperatura))
        elif opcion == '3':
            nombre= inputstr('nombre')
            apellido= inputstr('apellido')
            ci= inputint('cedula')
            fecha_de_nacimiento= inputstr('fecha de nacimiento')
            Persona(nombre, apellido, ci, fecha_de_nacimiento)
            facturacion['persona']= Persona(nombre, apellido, ci, fecha_de_nacimiento)
            print(facturacion)


main()


