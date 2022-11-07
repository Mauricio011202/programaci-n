



# HAY QUE PONER TODAS LAS CATIDADES DE PAN EN 0 PARA QUE NO LOO TOME COMO NONE, FUE LO QUE USTED ME COMENTO QUE HICIERA

cantidad_shawarma_t= []
cantidad_shawarma_m= []
cantidad_shawarma_s= []
def elegir_shawarmas(productos, pedido, cantidad_shawarma_t, cantidad_shawarma_m,cantidad_shawarma_s):
    for k, v in productos.items():
        for key, vali in v.items():
            print(f"{k}: {vali}", end= '')
        print('')
    while True:
        shawarma= input("Ingrese el tipo de shawarma: ")
        cantidad_s= 0
        cantidad_t= 0
        cantidad_m= 0
        if shawarma == "T":
            z=0
            z= int(input('Ingrese la cantidad de shawarmas: '))
            cantidad_t+= z 
            cantidad_shawarma_t.append(cantidad_t)
            
            pedido[shawarma]= cantidad_t
        elif shawarma == "M":
            z=0
            z= int(input('Ingrese la cantidad de shawarmas: '))
            cantidad_m+= z 
            cantidad_shawarma_m.append(cantidad_m)
            
            pedido[shawarma]= cantidad_m
        elif shawarma == "S":
            z=0
            z= int(input('Ingrese la cantidad de shawarmas: '))
            cantidad_s+= z 
            cantidad_shawarma_s.append(cantidad_s)
            
            pedido[shawarma]= cantidad_s
        if input("quieres pedir otro tipo de shawarma? Y o N: ")== "Y":
                continue
        return pedido

def datos_cliente(pedido):
    cedula= input("Ingrese su cedula: ")
    while not cedula.isnumeric():
            cedula= input("ERROR. Ingrese su cedula: ")
    correo= input("Ingrese su correo:")
    while len(correo) > 50:
        correo= input("Ingrese su correo:")
    while True:
        contador= 0
        for i in correo:

            if i== "@":
                contador+=1

            if i == " ":
                correo= input("Ingrese su correo:")
                break 


        if contador!= 1:
            correo= input("Ingrese su correo:")
        break
    cliente= {'Nombre': input("Ingrese su nombre completo: "),
              'Cedula': cedula, 
              'Correo': correo,
              'Shawarmas T': pedido.get('T'),
              'Shawarmas M': pedido.get('M'),
              'Shawarmas S': pedido.get('S')}
    return cliente

def crear_monto(cliente):
    monto=0 
    monto+= cliente.get('Shawarmas T')*8
    monto+= cliente.get('Shawarmas M')*12
    monto+= cliente.get('Shawarmas S')*15
    cliente['Monto']= monto
    return monto

def crear_factura(cliente):
    print("Nombre: ", cliente.get('Nombre'))
    print("Cedula: ", cliente.get('Cedula'))
    print("Correo", cliente.get('Correo'))
    print("Cantidad de Shawarmas T", cliente.get('Shawarmas T'))
    print("Cantidad de Shawarmas M", cliente.get('Shawarmas M'))
    print("Cantidad de Shawarmas S", cliente.get('Shawarmas S'))
    print("Monto Total en $: ", cliente.get('Monto'))



        

           




def main():
    print('Bienvenido a Shawarma Saman ')
    
    productos= {'T': {'Descripcion': 'Tradicional', 'Precio': 8},
               'M': {'Descripcion': 'Mixto', 'Precio': 35},
               'S': {'Descripcion': 'Saman', 'Precio': 35}, }
    pedido_cliente={}
    
    
    while True:
        pedido= elegir_shawarmas(productos, pedido_cliente, cantidad_shawarma_t, cantidad_shawarma_m,cantidad_shawarma_s)
        cliente= datos_cliente(pedido)
        
        monto= crear_monto(cliente)
        opcion= input('Desea seguir con la compra S o N')
        if opcion== 'N':
            continue
        print("Nombre: ", cliente.get('Nombre'))
        print("Cedula: ", cliente.get('Cedula'))
        print("Correo", cliente.get('Correo'))
        print("Cantidad de Shawarmas T", cliente.get('Shawarmas T'))
        print("Cantidad de Shawarmas M", cliente.get('Shawarmas M'))
        print("Cantidad de Shawarmas S", cliente.get('Shawarmas S'))
        print("Monto Total en $: ", cliente.get('Monto'))
        
        if input("desea continuar  Y O N: ") == 'N':
            continue
        #fINAL DEL DIA
        print('Cantidad para tipo T',len(cantidad_shawarma_t))
        print('Cantidad para tipo M',len(cantidad_shawarma_m))
        print('Cantidad para tipo S',len(cantidad_shawarma_s))

        


        
        
main()