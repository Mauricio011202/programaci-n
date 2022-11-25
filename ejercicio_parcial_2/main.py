from bebida import Bebida,  Alcoholica, NoAlcoholica
from funciones import inputStr, inputInt
from cliente import Cliente
nombre_bebidas_alco_registradas: list[str]= []
nombre_bebidas_no_alco_registradas: list[str]= []
bebidas_alcoholicas_registradas: list[Alcoholica]= []
bebidas_no_alcoholicas_registradas: list[NoAlcoholica]= []
clientes_registrados: list[Cliente]= []
bebidas_alcoh_compradas: list[Alcoholica] = []
bebidas_no_alcoh_compradas: list[NoAlcoholica] = []


while True:
    opcion= input(" Bienvenido a Saman Bar marque un numero para realizar una accion: \n 1. Registrar una bebida \n 2. Realizar un compra \n 3. Ver estadisticasde venta \n 4. Salir \n =>")
    while opcion not in ['1','2','3','4']:
        opcion= input(" ERROR! Marque un numero valido: \n 1. Registrar una bebida \n 2. Realizar un compra \n 3. Ver estadisticasde venta \n 4. Salir\n =>")
    if opcion == '1':
        tipo= input('Ingrese el tipo de bebida quedesee registrar: \n 1. Alcoholica \n 2. No alcoholica\n =>')
        
        while tipo not in ['1','2']:
            tipo= input('Error! Ingrese el tipo de bebida que desee registrar: \n 1. Alcoholica \n 2. No alcoholica\n =>')
        nombre_beb= inputStr("el nombre de la bebida")
        
        if tipo == '1':
            while nombre_beb in nombre_bebidas_alco_registradas:
                nombre_beb=input('Error! bebida ya registrada, ingrese otra bebida que desee registrar')
            nombre_bebidas_alco_registradas.append(nombre_beb) 
            precio_beb= inputInt("el precio de la bebida")
            grado_alco= inputStr("el grado de alcohol de la bebida")
            bebidas_alcoholicas_registradas.append(Alcoholica(nombre_beb, precio_beb, grado_alco))
            print('Bebida registrada con exito!')
        
        elif tipo == '2':
            while nombre_beb in nombre_bebidas_no_alco_registradas:
                nombre_beb=input('Error! bebida ya registrada, ingrese otra bebida que desee registrar')
            nombre_bebidas_no_alco_registradas.append(nombre_beb) 
            precio_beb= inputInt("el precio de la bebida")
            temperatura= inputStr("la temperatura de consumo de la bebida")
            bebidas_no_alcoholicas_registradas.append(NoAlcoholica(nombre_beb, precio_beb, temperatura))
            print('Bebida registrada con exito!')
    elif opcion == '2':
        if len(clientes_registrados) > 0:
            cliente_nuevo= input('Eliga una opcion: \n 1. Cliente nuevo \n 2. Cliente registrado \n =>')
            while cliente_nuevo not in ['1', '2']:
                cliente_nuevo= input('ERROR! Eliga una opcion: \n 1. Cliente nuevo \n 2. Cliente registrado \n =>')

            if cliente_nuevo== '1':
                nombre_cli= inputStr('nombre')
                edad_cli= inputInt('edad')
                ci= inputStr('cedula de identidad')
                cliente = Cliente(nombre_cli,edad_cli,ci)
                clientes_registrados.append(Cliente(nombre_cli,edad_cli,ci))
            else:
                for i in range(len(clientes_registrados)):
                    print(f'{i}.{clientes_registrados[i].prin_info()}')
                num_cliente= input('Ingrese el numero que tenga sus datos: ')
                while num_cliente not in range(len(clientes_registrados)):
                    num_cliente= input('ERROR! Ingrese el numero que tenga sus datos: ')
                cliente: Cliente= clientes_registrados[num_cliente]
                print(f'Bienvenido de nuevo {cliente.nombre}')
        else:
            nombre_cli= inputStr('nombre')
            edad_cli= inputInt('edad')
            ci= inputStr('cedula de identidad')
            cliente = Cliente(nombre_cli,edad_cli,ci)
            clientes_registrados.append(Cliente(nombre_cli,edad_cli,ci))

        if cliente.edad >= 18:
            print("-----Bebidas alcoholicas--------")
            for i in range(len(bebidas_alcoholicas_registradas)):
                print(f'{i}.{bebidas_alcoholicas_registradas[i].print_info}')
        print("-----Bebidas no alcoholicas--------")
        for i in range(len(bebidas_no_alcoholicas_registradas)):
            print(f'{i}.{bebidas_no_alcoholicas_registradas[i].print_info}')

        while True:
            if cliente.edad>= 18:
                tipo_compra= input('Eliga la accion que desee realizar \n 1. Comprar una bebida alcholica \n 2. comprar una bebida no alcoholica \n 3. no comprar nada mas ')
                if tipo_compra == '1':
                    num_beb_deseada= input('Ingrese el numero de la bebida que desea')
                    while num_beb_deseada not in bebidas_alcoholicas_registradas:
                        num_beb_deseada= input('Ingrese el numero de la bebida que desea')
                    bebidas_alcoh_compradas.append(bebidas_alcoholicas_registradas[num_beb_deseada])

                elif tipo_compra == '2':
                    num_beb_deseada= input('Ingrese el numero de la bebida que desea')
                    while num_beb_deseada not in bebidas_no_alcoholicas_registradas:
                        num_beb_deseada= input('Ingrese el numero de la bebida que desea')
                    bebidas_no_alcoh_compradas.append(bebidas_no_alcoholicas_registradas[num_beb_deseada])
                    





            

            
                    
            

        
            


        