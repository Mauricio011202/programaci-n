from cliente import Cliente
from herramientas import Herramientas, Herreria, Carpinteria, Plomeria



clientes= []
monto_herramienta_carpi= []
montos_totales_clientes= []
monto_herramienta_herre= []
monto_herramienta_plome= []
def main():

    print('Bienvenido al hotel saman ')
    while True:
        opcion= input('Ingrese una opcion \n 1. Comprar una herramienta \n 2. Ver estadisticas \n 3. Salir \n =>')
        while opcion not in ['1','2','3']:
            opcion= input('Ingrese \n 1. Reservar una habitacion \n 2. Ver estadisticas \n 3. Salir \n =>')
        if opcion== '1':
            nombre= input('Por favor igrese su nombre: ')
            edad= input('Por favor igrese su edad: ')
            while not edad.isnumeric():
                edad= input('Por favor igrese su edad: ')
            edad= int(edad)
            ci= input('Por favor igrese su cedula: ')
            telf= input('Por favor igrese su telefono: ')
            
            cliente= Cliente(nombre, edad,ci, telf)
            clientes.append(cliente)
            while True:
                descuentos=0
                tipo_herramienta= input('Escoger el tipo de hab que desee \n 1. Plomeria \n 2. Herreria \n 3. Carpinteria \n =>')
                while tipo_herramienta not in [ '1', '2', '3']:
                    tipo_herramienta= input('Escoger el tipo de hab que desee \n 1. Plomeria \n 2. Herreria \n 3. Carpinteria \n =>')
                herramientas_por_cliente: list [Herreria,Plomeria,Carpinteria] = []
                monto_finales= []
                marca= input('Ingrese la marca de la herramienta que desea: ')
                color= input('Ingrese el color de la herramienta que desea: ')
                

                if tipo_herramienta == '1':
                    precio= 50
                    tipo= 'plomeria'
                    pulgadas= input('Ingrese de cuantas pulgadas desea la herramienta: ')
                    ajustable= input('Desea una herramienta ajustables ingrese (Si o No): ')
                    while ajustable.capitalize() not in ['Si','No']:
                        ajustable= input('Desea una herramienta ajustables ingrese (Si o No): ')
                    mantenimiento= input('Desea una herramienta que requiera mantenimiento ingrese (Si o No): ')
                    while mantenimiento.capitalize() not in ['Si','No']:
                        ajustable= input('Desea una herramienta que requiera mantenimiento ingrese (Si o No): ')
                    cantidad= input('Ingrese la cantidad de herramientas que desea: ')
                    while not cantidad.isnumeric():
                        cantidad= input('ERROR.Ingrese la cantidad de herramientas que desea: ')
                        
                    monto= precio*int(cantidad)
                    monto_finales.append(monto)
                    herramienta= Plomeria(marca, color, precio, tipo, pulgadas,ajustable, mantenimiento, cantidad)
                    herramientas_por_cliente.append(herramienta)
                    monto_herramienta_plome.append(monto)
                elif tipo_herramienta == '2':
                    precio= 40
                    tipo= 'herreria'
                    grados= input('Ingrese la temperatura maxima que soporta laherramienta que desea: ')
                    while not grados.isnumeric():
                        grados= input('Ingrese la temperatura maxima que soporta laherramienta que desea: ')
                    cantidad= input('Ingrese la cantidad de herramientas que desea: ')
                    while not cantidad.isnumeric():
                        cantidad= input('ERROR.Ingrese la cantidad de herramientas que desea: ')
                        
                    monto= precio*int(cantidad)
                    monto_finales.append(monto)
                    herramienta= Herreria(marca, color, precio, tipo, grados, cantidad)
                    herramientas_por_cliente.append(herramienta)
                    monto_herramienta_herre.append(monto)
                elif tipo_herramienta== '3':
                    precio= 30
                    tipo= 'Carpinteria'
                    garantia= input('Ingrese el tiempo de garantia que deseaen meses: ')
                    while not garantia.isnumeric():
                        garantia= input('Ingrese la temperatura maxima que soperta laherramienta que desea: ')
                    cantidad= input('Ingrese la cantidad de herramientas que desea: ')
                    while not cantidad.isnumeric():
                        cantidad= input('ERROR.Ingrese la cantidad de herramientas que desea: ')
                        
                    monto= precio*int(cantidad)
                    monto_finales.append(monto)
                    herramienta= Carpinteria(marca, color, precio, tipo, garantia, cantidad)
                    herramientas_por_cliente.append(herramienta)
                    monto_herramienta_carpi.append(monto)
                    seguir= input('Desea comprar mas herramientas para la misma cuenta marque S si no marque cualquier letra').capitalize()
                if seguir!= 'S':
                        break
            print('----FACTURA-------')
            for herramienta in herramientas_por_cliente:
                herramienta.mostrar()
            cliente.mostrar()
            print(f'TOTAL: {sum(monto_finales)}')
            
        elif opcion == '2':
            print('ESTADISTICAS')
            print(f'Cantidad de clientes que compraron productos: {len(clientes)}')
            print(f'Total facturado por herramientas de plomeria: {sum(monto_herramienta_plome)}$ ')
            print(f'Total facturado por herramientas de herreria: {sum(monto_herramienta_herre)}$ ')
            print(f'Total facturado por herrmientas de carpinteria: {sum(monto_herramienta_carpi)}$ ')


            
                




                    

main()