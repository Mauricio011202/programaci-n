precios ={
    "Pollo": "10",
    "Pescado": "15"
}

comprador = {'Name': 'Juan',
            'id': '5',
            'productos': {'1':['Pollo', '10']}}

while True:
    opcion= input(""" Seleccione una opcion:
            1. Comprar.
            2. Calcular Factura.
            3. Salir.


    """)
    if opcion== "1":
        id=input('Ingrese su cedula')
        encontrado=False
        for k,v in comprador.items():
            if id== k:
                encontrado= True
                print('hola')
            print('Hola')
        if encontrado== True:
            count=1
            for k,v in precios.items():
                print(f"{count}. {k}")
                count+=1
            compra=input("Pulse el nuero de lo que quiere comprar?")
            count=1
            for k,v in precios.items():
                if str(count)==compra:
                    producto=k
                count+=1
            cantidad=input('Ingrese la cantidad')
            maximo=len(comprador[id]["productos"]+1)
            comprador[id]["productos"][maximo]=[producto,cantidad]
            
        print(comprador)

