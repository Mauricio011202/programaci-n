from Funciones import *
from Herramienta import *

def main ():
    salir=False
    cliente=datos_clientes()
    while salir==False:
        seguir=input('Desea seguir comprando:\n1-Si\n2-No')
        if seguir=='2':
            salir=True
        herramientas_plomeria=[]
        herramientas_herreria=[]
        herramientas_carpinteria=[]
        total=[]
        print('BIENVENIDO A SAMAN TOOLS')
        descuento_abundante=abundante(int(cliente[1]))
        herramienta=comprar_herramienta()
        if herramienta=='1':
            marca=input('Ingrese la marca de la herramienta:')
            color=input('Ingrese el color de la herramienta:')
            precio=50
            total.append(precio)
            tipo='Plomeria'
            pulgadas=input('Ingrese la cantidad de pulgadas:')
            ajustable=input('Seleccione:\n1-Es ajustable\n2-No es ajustable')
            while ajustable!='1' and ajustable!='2':
                ajustable=input('Seleccione:\n1-Es ajustable\n2-No es ajustable')
            if ajustable=='1':
                ajustable='Si'
            else:
                ajustable='No'
            mantenimiento=input('Seleccione:\n1-Necesita mantenimiento\n2-No necesita mantenimiento')
            while mantenimiento!='1' and mantenimiento!='2':
                mantenimiento=input('Seleccione:\n1-Necesita mantenimiento\n2-No necesita mantenimiento')
            if mantenimiento=='1':
                mantenimiento='Si'
            else:
                mantenimiento='No'


            plomeria=Plomeria(marca,color,precio,tipo,pulgadas,ajustable,mantenimiento)
            herramienta_plomeria=plomeria.mostrar_herramienta()
            herramientas_plomeria.append(herramienta_plomeria)
           
        elif herramienta=='2':
            marca=input('Ingrese la marca de la herramienta:')
            color=input('Ingrese el color de la herramienta:')
            precio=40
            total.append(precio)
            tipo='Herreria'
            grados=input('Ingrese la cantidad de grados celsisus que soporta:')
            herreria=Herreria(marca,color,precio,tipo,grados)
            herramienta_herreria=herreria.mostrar_herramienta()
            herramientas_herreria.append(herramienta_herreria)
           

        elif herramienta=='3':
            marca=input('Ingrese la marca de la herramienta:')
            color=input('Ingrese el color de la herramienta:')
            precio=30
            total.append(precio)
            tipo='Carpinteria'
            garantia=input('Ingrese los años de garantia que posee el producto:')
            while not garantia.isnumeric():
                garantia=input('Ingrese los años de garantia que posee el producto:')

            carpinteria=Carpinteria(marca,color,precio,tipo,garantia)
            herramienta_carpinteria=carpinteria.mostrar_herramienta()
            herramientas_carpinteria.append(herramienta_carpinteria)
            
    

        imprimir_factura(cliente,herramientas_plomeria,herramientas_carpinteria,herramientas_herreria,total,descuento_abundante)

            




       
            
        
main()