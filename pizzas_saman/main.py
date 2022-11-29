from alimentos import Alimentos, Pizza, Panuzzo
from cliente import Cliente

pizza_registradas_sin_blanca:list[Pizza]= []
pizza_registradas_con_blanca:list[Pizza]= []
panuzzos_registrados: list[Panuzzo]= []
clientes_registrados: list[Cliente]= []
pizzas_sin_salsa_comprados: list[Pizza]= []
pizzas_con_salsa_comprados: list[Pizza]= []
panuzos_comprados: list[Panuzzo]= []

def main():
    while True:
        option= input('Bienvenido a la pizeria saman seleccione una opcion: \n 1. Crear una comida.\n 2. Comprar comida. \n 3. Ver estadisticas del dia.\n 4. Salir. ')
        while option not in ['1','2','3','4']:
            option= input('Erro! Eliga una opcion valida: ')
        if option== '1':
            plato= input('Que comida desea registrar \n 1. Pizza. \n 2. Panuzzo')
            while plato not in ['1','2']:
                plato= input('Erro! Eliga una opcion valida: ')
            if plato == '1':
                tipo= 'pizza'
                precio= int(input('ingrese el precio : '))
                sabor= input('Ingrese si la pizza es rosa o bianca').lower()
                while sabor not in ['rosa', 'bianca']:
                    sabor= input('Error! Ingrese la palabra rosa o bianca').lower()
                pizza= Pizza(tipo,precio, sabor)
                if sabor == 'rosa':
                    pizza_registradas_sin_blanca.append(pizza)
                else:
                    pizza_registradas_con_blanca.append(pizza)
                
            elif plato== '2':
                tipo= 'panuzzo'
                precio= int(input('ingrese el precio : '))
                acompa= input('Ingrese si el panuzo tiene acompanante o no').lower()
                while acompa not in ['si', 'no']:
                    acompa= input('Error! Ingrese la palabra si o no').lower()
                panuzzo= Panuzzo(tipo,precio, acompa)
               
                panuzzos_registrados.append(panuzzo)
        
        elif option== '2':
            nombre= input('por favor ingrese su nombre: ')
            apellido= input('por favor ingrese su apellido: ')
            ci= int(input('por favor ingrese su cedula:'))
            telefono= input('por favor ingrese su telefono: ')
            alergico= input('inidique si es alergico (si o no): ')

            cliente= Cliente(nombre, apellido, ci, telefono, alergico)
            clientes_registrados.append(cliente)
            if alergico== 'si':
                for i in range(len(pizza_registradas_sin_blanca)):
                    print("Pizzas sin salsa blanca")
                    print(f'{i}. {pizza_registradas_sin_blanca[i].print_info()} ')
                for i in range(len(panuzzos_registrados)):
                    print("Panuzzos disponibles")
                    print(f'{i}. {panuzzos_registrados[i].print_info()} ')
            else:

                for i in range(len(pizza_registradas_con_blanca)):
                    print("Pizzas sin salsa blanca")
                    print(f'{i}. {pizza_registradas_con_blanca[i].print_info()} ')

                for i in range(len(pizza_registradas_sin_blanca)):
                    print("Pizzas sin salsa blanca")
                    print(f'{i}. {pizza_registradas_sin_blanca[i].print_info()} ')

                for i in range(len(panuzzos_registrados)):
                    print("Panuzzos disponibles")
                    print(f'{i}. {panuzzos_registrados[i].print_info()} ')

            
            while True:
                tipo_comida_comprar= input('Seleccione el tipo de comida que desee 1. pizza rosa, 2. pizza bianca. 3. panuzzo \n: ' )
                if tipo_comida_comprar == '1':
                    num_lista= int(input('ingrese el numero de plato que desea'))
                    pizzas_sin_salsa_comprados.append(pizza_registradas_sin_blanca[num_lista])
                elif tipo_comida_comprar == '2':
                    num_lista= int(input('ingrese el numero de plato que desea'))
                    pizzas_con_salsa_comprados.append(pizza_registradas_con_blanca[num_lista])
                elif tipo_comida_comprar == '3':
                    num_lista= int((input('ingrese el numero de plato que desea')))
                    panuzos_comprados.append(panuzzos_registrados[num_lista])
                seguir= input('Desea comprar algo mas 0. No 1. Si')
                if seguir == '0':
                    break
            print("Factura")
            print("info Cliente:")
            print(cliente.print_info())
            print("Productos")

            subtotal= 0 
            descuento= 0
            for i in pizzas_con_salsa_comprados:
                subtotal+= i.precio
                print(i.print_info())
            for i in pizzas_sin_salsa_comprados:
                subtotal+= i.precio
                print(i.print_info())
            for i in panuzos_comprados:
                subtotal+= i.precio
                print(i.print_info())
            print(f'cantidad de pizzas rosa: {len(pizzas_con_salsa_comprados)}')
            print(f'cantidad de pizzas rosa: {len(pizzas_sin_salsa_comprados)}')
            print(f'cantidad de pizzas rosa: {len(panuzos_comprados)}')
            print(f'subtotal: {subtotal}')


            lista_fibo= dar_suce_fibonacci(cliente.ci)
            for i in lista_fibo:
                if i== cliente.ci:
                    descuento= subtotal*0.10
            def dar_suce_fibonacci(numero_parada,lista_fibo= [],num1= 0,num2=1,):
                lista_fibo.append(num1)
                if num2 > numero_parada:
                    return lista_fibo
                return dar_suce_fibonacci(numero_parada,lista_fibo,num2,num1+num2)
            

            lista1= []
            abundate= False
            for i in range(1,subtotal):
                    if subtotal%i== 0:
                     lista1.append(i)

            sum_list1= sum(lista1)
            if sum_list1>subtotal:
                abundate= True
            else:
                abundate= False
            if abundate == True:
                descuento= subtotal*0.10
            monto= subtotal - descuento
            print(f'monto: {monto}$')

        elif option == '3':
            print('ESTADISTICAS DEL DIA')
            print(f'Cantidad de clientes: {len(clientes_registrados)}') 
            facturado_pcs= 0
            for i in pizzas_con_salsa_comprados:
                facturado_pcs+= i.precio
            print(f" total facturado pizzas bianca {facturado_pcs}") 
            facturado_pss= 0
            for i in pizzas_sin_salsa_comprados:
                facturado_pss+= i.precio
            print(f" total facturado pizzas bianca {facturado_pss}") 
            facturado_pnuzo= 0
            for i in panuzos_comprados:
                facturado_pnuzo+= i.precio
            print(f" total facturado pizzas bianca {facturado_pnuzo}") 
             
            
         
            


















main()
