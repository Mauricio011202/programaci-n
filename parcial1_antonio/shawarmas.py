

def mostrar_menu():
    menu= {'T': {'Descripcion': 'Tradicional', 'Precio': 8},
               'M': {'Descripcion': 'Mixto', 'Precio': 12},
               'S': {'Descripcion': 'Saman', 'Precio': 15}, }
    for key, value in menu.items():
        for key2, value2 in value.items():
            print(f'{key} {value2} ', end= ' ')
        print('\n')

def descuentos(cliente):
    if cliente.get('cantidad')%2 != 0:
        x= cliente.get('monto')
        descuento= x*0.15
        cliente['descuento']= descuento
    else:
        descuento=0
        cliente['descuento']= descuento
    return descuento




def main():
    
        
    clientes_con_descuento= 0
    shawarmas_t= 0
    shawarmas_m= 0
    shawarmas_s= 0
    clientes= []
    lista_correos= []
    print('Bienvenido a Shawarmas Saman ')
    while True:
        optin= input('Seleccione una opcion: \n1. Realizar un pedido.\n2. Ver estadisticas\n3. Salir\n=>')
        while optin not in ['1','2','3']:
            optin= input('Seleccione una opcion: \n1. Realizar un pedido.\n2. Ver estadisticas\n3. Salir\n=>')
        if optin == '1':
            cliente= {}
            cantidad_total_sha= 0
            nombre= input('Ingrese su nombre: ')
            while not nombre.isalpha():
                nombre= input('ERROR! Ingrese su nombre: ')
            cedula= input('Ingrese su cedula: ')
            while not cedula.isnumeric():
                cedula= input('ERROR! Ingrese su cedula: ')
            
            while True:
                corrreo= input('Ingrese su correo: ')
                if len(corrreo)> 50:
                    continue
                for i in corrreo:
                    if i == ' ':
                        continue
                aux= 0
                for i in corrreo:
                    if i == '@':
                        aux+= 1
                if aux!= 1:
                    continue
                else: 
                    break
            lista_correos.append(corrreo)
            cliente['Nombre']= nombre
            cliente['cedula']= cedula
            cliente['correo']= corrreo
            


            mostrar_menu()
            cliente['Shawarmas_s']= 0
            cliente['Shawarmas_m']= 0
            cliente['Shawarmas_t']= 0


            while True:
                tipo= input('Ingrese el tipo se shawarma que desea T, M, S:').capitalize()
                while tipo not in ['T','M', 'S']:
                    tipo= input('Ingrese el tipo se shawarma que desea T, M, S:').capitalize()
                if tipo == 'T':
                    
                    cantidad= int(input('Ingrese la cantidad de shawarmas tradicionales que desea: '))
                    shawarmas_t= cantidad + shawarmas_t
                    cantidad_total_sha+= cantidad

                    cliente['Shawarmas_t']= cantidad
                    
                elif tipo == 'M':
                    
                    cantidad= int(input('Ingrese la cantidad de shawarmas mixtos que desea: '))
                    shawarmas_m= cantidad + shawarmas_m
                    cliente['Shawarmas_m']= cantidad
                    cantidad_total_sha+= cantidad
                    
                elif tipo == 'S':
                    
                    cantidad= int(input('Ingrese la cantidad de shawarmas mixtos que desea: '))
                    shawarmas_s= cantidad + shawarmas_s
                    cliente['Shawarmas_s']= cantidad
                    cantidad_total_sha+= cantidad
                    if cantidad_total_sha%2 != 0:
                        clientes_con_descuento= clientes_con_descuento+ 1
                    
                seguir= input('Desea seguir comprando: \n1. SI \n2. NO')
                if seguir == '1':
                    continue
                else: 
                    break

            cliente['cantidad']= cantidad_total_sha
            print(cliente)
            monto= cliente.get('Shawarmas_t')*8 + cliente.get('Shawarmas_m')*12 + (cliente.get('Shawarmas_s'))*15
            cliente['monto']= monto
            descuento=descuentos(cliente)
            print('**********FACTURA*********')
            print('NOMBRE:', cliente.get('Nombre'))
            print('CEDULA:', cliente.get('cedula'))
            print('CORREO:', cliente.get('correo'))
            print('SHAWARMAS T:', cliente.get('Shawarmas_t'))
            print('SHAWARMAS M:', cliente.get('Shawarmas_m'))
            print('SHAWARMAS S:', cliente.get('Shawarmas_s'))
            print('MONTO:', cliente.get('monto'))
            print('DESCUENTO:', descuento)
            print('MONTO CON DESCUENTO: ', monto-descuento)
        
        elif optin == '2':
            print(f'Cantidad de shawaramas de tipo  T vendidos: {shawarmas_t}')
            print(f'Cantidad de shawaramas de tipo M vendidos: {shawarmas_m}')
            print(f'Cantidad de shawaramas de tipo S vendidos: {shawarmas_s}')
            print(f'Cantidad de clientes con descuento: {clientes_con_descuento}')

            longitud_correos= []
            for i in lista_correos:
                longitud_correos.append(len(i))
            x= max(longitud_correos)
            print(f'El ganador del correo es {x}')






main()