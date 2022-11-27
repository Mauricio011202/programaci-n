

clientes= []
clientes_u= []
clientes_t= []
clientes_r= []

def bienevenida():
    print('Bienvenido a clinicas Caracas')

def marcar_opcion(studios):
    for k, v in studios.items():
        for key_int, v_int in v.items():
            print(f'{k}-{v_int}', end = "")
        print("")
    option= input('Ingrese el estudio que desea realizar: ').upper()
        
    return option


def datos_cliente(option):
    cliente= {'Cedula': input("Ingrese su cedula: "),
            'Edad': int(input("Ingrese su edad: ")),
            'Sexo': input("Ingrese su sexo 'M' o 'F': "),
            'Estudio': option}
    return cliente
def clasificacion_de_clientes( option,cu,ct,cr,cliente ):
    if option == 'U':
            cu.append(cliente)
    elif option== 'T':
            ct.append(cliente)
    elif option == 'R':
            cr.append(cliente)

def retornar_monto(cliente):
    for k, v in cliente.items():
        if v == 'U':
            monto= 8900
        elif v == 'T':
            monto= 12640
        elif v == 'R':
            monto= 15600
    cliente['Monto']= monto
    return monto

def calcular_descuentos(cliente):
    if cliente.get('Sexo')== 'F' and cliente.get('Edad') >= 55:
        descuento_cliente= cliente.get('Monto')*0.25
    elif cliente.get('Sexo')== 'M' and cliente.get('Edad') >= 65:
        descuento_cliente= cliente.get('Monto')*0.25
    else:
        descuento_cliente= 0
    cliente['Descuento']= descuento_cliente
    return descuento_cliente
            
def factura_cliente(cliente):
    print('**********FACTURA**********')
    print("Cedula:", cliente.get('Cedula'))
    print("sexo:", cliente.get('Sexo'))
    print("Monto sin descuento:", cliente.get('Monto'))
    print("Descueto:", cliente.get('Descuento'))
    print("Monto a cancelar:", (cliente.get('Monto')-cliente.get('Descuento')))

def monto_descuentos(clientes, descuento_total):
    
    for i in clientes:
        for k, v in i.items():
            if k == 'Descuento':
                descuento_total += v
    return descuento_total

def monto_neto_(clientes, monto_neto):
    
    for i in clientes:
        for k, v in i.items():
            if k == 'Monto': 
                monto_neto += v
    return monto_neto
    
def main():
    studios= {
        'U' :{'Descricion': 'Ultrasonido', 'Precio': 8900},
        'T' :{'Descricion': 'Tomogracia', 'Precio': 12640},
        'R' :{'Descricion': 'Resonancia', 'Precio': 15600},
    
    } 
    bienevenida()
    descuento_total= 0
    monto_neto=0
    
    while True:
        option= marcar_opcion(studios)
        cliente= datos_cliente(option)
        clasificacion_de_clientes( option, clientes_u,clientes_t,clientes_r, cliente)
        monto= retornar_monto(cliente)
        descuento_cliente= calcular_descuentos(cliente)
        clientes.append(cliente)
        factura_cliente(cliente)
        descuento_total= monto_descuentos(clientes, descuento_total)
        monto_final_dia= monto_neto_(clientes, monto_neto)
        if input('1.Deseas seguir agregado clientes\n 2. Ver las cuentas del dia') == '2':
            break
    print(clientes)
    print('Cantidad de clientes U:', len(clientes_u))
    print('Cantidad de clientes T:', len(clientes_t))
    print('Cantidad de clientes R', len(clientes_r))
    print('Monto total de descuentos:', descuento_total)
    print('Monto neto facturado', (monto_final_dia-descuento_total))
    print('Promedio de pago: ', (monto_final_dia/len(clientes)))
    

        

main()