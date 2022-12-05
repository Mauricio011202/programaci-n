from cliente import Cliente
from habitaciones import Habitacion, Suite, Doble, Sencilla

clientes= []
suites= []
dobles= []
sencilla= []
montos_suites= []
montos_dobles= []
montos_sencillas= []

def main():

    print('Bienvenido al hotel saman ')
    while True:
        opcion= input('Ingrese una opcion \n 1. Reservar una habitacion \n 2. Ver estadisticas \n 3. Salir \n =>')
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
            num_personas=   input('Por favor igrese el numero de acompanantes: ')
            cliente= Cliente(nombre, edad,ci, telf, num_personas)
            clientes.append(cliente)
            while True:
                descuentos=0
                tipo_hab= input('Escoger el tipo de hab que desee \n 1. Suite \n 2. Doble \n 3. Sencilla \n =>')
                while tipo_hab not in [ '1', '2', '3']:
                    tipo_hab= input('ERROR! Escoger el tipo de hab que desee \n 1. Suite \n 2. Doble \n 3. Sencilla \n =>')
                habitacion_por_cliente: list [Habitacion] = []
                monto_finales= []
                if tipo_hab== '1':
                    noches= int(input('ingrese la cantidad de noches'))
                    monto= 100*noches
                    lista1= []

                    for i in range(1,edad):
                            if edad%i== 0:
                             lista1.append(i)
                    
                    sum_list1= sum(lista1)
                    if sum_list1>edad:
                        abundante= True
                    else:
                        abundante= False
                    if abundante == True:
                        descuentos= monto*0.10
                    monto= monto - descuentos 
                    montos_suites.append(monto)
                    monto_finales.append(monto)
                    camas= 3
                    baños= 2
                    jacuzzi_op= input('Desea una habitacion con jacuzzi? 1\n 1. Si \n 2. No \n =>')
                    if jacuzzi_op == '1':
                        jacuzzi= True
                    else:
                        False
                    nueva_habitacion= Suite(camas, baños,monto, jacuzzi)
                    suites.append(nueva_habitacion)
                    habitacion_por_cliente.append(nueva_habitacion)

                elif tipo_hab== '2':
                    noches= int(input('ingrese la cantidad de noches:  '))
                    monto= 60*noches
                    lista1= []

                    for i in range(1,edad):
                            if edad%i== 0:
                             lista1.append(i)
                    
                    sum_list1= sum(lista1)
                    if sum_list1>edad:
                        abundante= True
                    else:
                        abundante= False
                    if abundante == True:
                        descuentos= monto*0.10
                    monto= monto - descuentos
                    montos_dobles.append(monto)
                    monto_finales.append(monto)
                    camas= 2
                    baños= 2
                    cama_op= input('Desea una habitacion con cama matrimonial o sencilla? 1\n 1. Matrimonal \n 2.Sencilla \n =>')
                    if cama_op == '1':
                        tipo= 'matrimonial'
                    else:
                        tipo= 'sencilla'
                    nueva_habitacion= Doble(camas, baños, monto, tipo )
                    dobles.append(nueva_habitacion)
                    habitacion_por_cliente.append(nueva_habitacion)

                elif tipo_hab== '3':
                    noches= int(input('ingrese la cantidad de noches:  '))
                    monto= 40*noches
                    lista1= []

                    for i in range(1,edad):
                            if edad%i== 0:
                             lista1.append(i)
                    
                    sum_list1= sum(lista1)
                    if sum_list1>edad:
                        abundante= True
                    else:
                        abundante= False
                    if abundante == True:
                        descuentos= monto*0.10
                    monto= monto - descuentos 
                    montos_sencillas.append(monto)
                    monto_finales.append(monto)
                    camas= 1
                    baños= 1
                    tv_op= input('Desea una habitacion con tv? 1\n 1. Si \n 2.No \n =>')
                    if tv_op == '1':
                        tv= 'SI'
                    else:
                        tv= 'NO'
                    nueva_habitacion= Sencilla(camas, baños, monto, tv )
                    sencilla.append(nueva_habitacion)
                    habitacion_por_cliente.append(nueva_habitacion)
                seguir= input('Desea reservar mas habitaciones para la misma cuenta marque S').capitalize()
                if seguir!= 'S':
                    break
                    
            print('----FACTURA-------')
            for habitaciones in habitacion_por_cliente:
                habitaciones.mostrar_hab()
            cliente.mostrar()
            print(f'TOTAL: {sum(monto_finales)}')
            
        elif opcion == '2':
            print('ESTADISTICAS')
            print(f'Cantidad de clientes alojados: {len(clientes)}')
            print(f'Promedio de alojamiento habitacion suite: {len(suites)} ')
            print(f'Promedio de alojamiento habitacion dobles: {len(dobles)} ')
            print(f'Promedio de alojamiento habitacion sencilla: {len(sencilla)} ')
            print(f'Total facturado por habitacion suite: {montos_suites}$ ')
            print(f'Total facturado por habitacion sencilla: {montos_sencillas}$ ')
            print(f'Total facturado por habitacion dobles: {montos_dobles}$ ')








main()
