

factura= {}
hamburguesa= [0]
papas= [0]
helados= [0]
descuento=0
while True:
    opcion= int(input(""""Bienvenido a Mcdonald's
        Marque una opcion:
        1. Comprar
        2. Salir
        :"""))
    while  (opcion!= 1 and opcion!= 2):
        print('Ingrese un dato valido')
    if opcion== 1:
        datos= input("Ingrese su nombre: ")
        factura["Nombre"]=datos
        datos= (input('Ingres su cedula: '))
        listadedatos= int(datos)
        #ALTERNATIVA
        #datos2= list(datos)
        #valor= int(datos2[-1])
        #if valor%2= 0: 
        if listadedatos%2== 0:
                descuento+= 1
        factura["Cedula"]=datos
        
        while True:
            compras= int(input("""Que deseas comprar?
                    1. Hamburguesas (3$)
                    2. Papas fritas (1.5$)
                    3. Helado (1$)
                    4. No quiero comprar nada mas, quiero mi factura
                    :"""))
            if compras== 1:
                cantidad=int(input('Cuantas quieres ordenar?  '))
                hamburguesa[0]=cantidad
                factura["Hamburguesas"]=hamburguesa
            if compras== 2:
                cantidad= int(input('Cuantas quieres ordenar?  '))
                papas[0]=cantidad
                factura["Papas fritas"]=papas
            if compras== 3:
                cantidad=int(input('Cuantos quieres ordenar?  '))
                helados[0]=cantidad
                factura["Helados"]=helados
            if compras== 4:
                monto=((hamburguesa[0]*3) +(papas[0]*1.5) + (helados[0]*1))
                if descuento== 1:
                    monto= (monto -(monto*0.15))
                #si quiero recorer el valiu de una key que hago
                factura["Monto en $"]= monto

                print(f'Esta es su factura: \n {factura}')
                break
    if opcion== 2:
        print("Gracias por venir vuelva pronto")
        break


        

