entradas= {'G':{'descripcion': "general", "precio": 20}, 'V':{'descripcion': "vip", "precio": 35}}


def mostrar_etradas(entradas):
    for key, vali in entradas.items():
        for key2, vali2 in vali.items():
            print(f'{key2}:{vali2} ', end= '')
        print('')
def get_cedula():
    cedula= input('ingrese su cedula: ')
    while not cedula.isnumeric():
        cedula= input('ERROR!! ingrese su cedula: ')
    return int(cedula)
def get_correo(lista: list):
    
    while True:
        correo= input('Ingrese su correo: ')
        if len(correo)> 50:
                    continue
        for i in correo:
            if i == ' ':
                continue
        aux= 0
        for i in correo:
                if i == '@':
                        aux+= 1
        if aux!= 1:
                    continue
        else: 
                    break
    lista.append(correo)
    return correo



def crear_cliente(clientes: list, cantidad_g, cantidad_v,correos):
    cliente= {'Nombre': input('Ingrese su nombre: '),
                'cedula': get_cedula(),
                'correo': get_correo(correos),
                'entradas_g': cantidad_g,
                'entradas_v': cantidad_v,
                'personas': int(input('ingrese el numero de personas: '))}
    return cliente

def dar_descuento(cliente):
    descuento= False
    if cliente.get('personas')%2 != 0:
        descuento =True
    return descuento
def factura(cliente, descuento, clientes_descuento: list):
    print('**********FACTURA*********')
    print('Nombre', cliente.get('Nombre'))
    print('Cedula', cliente.get('cedula'))
    print('Correo', cliente.get('correo'))
    print('General', cliente.get('entradas_g'))
    print('vip', cliente.get('entradas_v'))
    sub_monto= (cliente.get('entradas_g')*20) + (cliente.get('entradas_v'))*35
    
    if descuento== True:
        clientes_descuento.append(cliente)
        descuento1= sub_monto*0.15
        monto= sub_monto - descuento1
    elif descuento == False:
        descuento1 = 0
        monto = sub_monto
    print(f'Descuento: {descuento1}$')    
    print(f'Monto: {monto}$')
        
    
def main():
    clientes= []
    clientes_descuento= []
    lista_correos= []
    entradas_g = []
    entradas_v= []
    while True:
        option = input('Bienvenido a la party seleccione una opcion \n1. Comprar una entrada \n2. Ver estadisticas del dia \n=> ')
        while option not in ['1', '2']:
            option = input('Bienvenido a la party seleccione una opcion \n1. Comprar una entrada \n2. Ver estadisticas del dia \n=> ')
        if option == '1':
            mostrar_etradas(entradas)
            cantidad_entradas_g= 0
            cantidad_entradas_v= 0
            while True:
                tipo= input('Seleccione el tipo de entrada que desea: \n1. General \n2. Vip \n3. SALIR \n=> ')
                if tipo == '1':
                    cantidad_entradas_g= int(input('Cantidad: '))
                    entradas_g.append(cantidad_entradas_g)
                elif tipo == '2':
                    cantidad_entradas_v= int(input('Cantidad: '))
                    entradas_v.append(cantidad_entradas_v)
                elif tipo == "3":
                    break
                
            cliente = crear_cliente(clientes, cantidad_entradas_g, cantidad_entradas_v,lista_correos)
            descuento = dar_descuento(cliente)
            factura(cliente, descuento, clientes_descuento)
            
        elif option == '2':
            print('*********ESTADISTICAS DEL DIA***********')
            print(f'Entradas tipo g vendidas: {sum(entradas_g)}')
            print(f'Entradas tipo v vendidas: {sum(entradas_v)}')
            print(f'Cantidad de clientes con descuento: {len(clientes)}')
        






main()