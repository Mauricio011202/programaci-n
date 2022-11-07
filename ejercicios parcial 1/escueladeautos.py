

def welcome():
    print("BIENVENIDO A LA AUOTOESCUELA LA RAPIDA")

def get_option():
    option= input("""Ingrese la opcion que desee realizar:
            1. Agregar un cliente
            2. Solicitar factura.
            3. Cantidad de clientes por carros
            4. Cantidad de clientes con descuento
            5. promedio de gacturacion por tipo de vehiculo.
            6. Salir
            """)
    return option

def get_data_cliente(carros_A, carros_B):
    info_cliente= {'Nombre': input("ingrese su nombre: "),
                   'Cedula': input("ingrese su cedula: "),
                   'Tipo de carro': input("ingrese tipo de carro 'A'o 'B': ").upper(),
                   'Horas': input("ingrese la cantidad de horas a conducir: ")}
    for k,v in info_cliente.items():
        if v == 'A':
            carros_A.append(info_cliente)
        elif v == 'B' :
            carros_B.append(info_cliente)

    return info_cliente

def monto_final_(info, clientes_descuento):
    for k,v in info.items():
        if v== 'A':
            precio= 2500

        elif v== 'B':
            precio= 3500
    for k,v in info.items():
        if k == 'Horas':
            horas= int(v)
    monto= (precio*horas)
    if horas>= 3:
        clientes_descuento.append(info)
        monto_final= monto - (monto*0.15)
        
    else:
        monto_final= monto
    return monto_final


def imprimir_factura(clientes1):
    cedula=input("Ingrese su cedula: ")
    for k,v in clientes1.items():
        if k == cedula:
            print("****FACTURA****")
            for datoss, valores in v.items():
                print(f"{datoss}:{valores}")
            
def promedio_pago(carros_A):
    for i in carros_A:
        for k,v in i.items():
            promedio=0
            if k== 'Monto':
                promedio+= v
    return promedio

def main():
    clientes=[]
    carros_A=[]
    carros_B=[]
    clientes1={}
    clientes_descuento=[]
    welcome()
    while True:
        option= get_option()
        if option== "1":
            info_cliente= get_data_cliente(carros_A, carros_B)
            monto_final= monto_final_(info_cliente, clientes_descuento)
            info_cliente['Monto']= monto_final 
            clientes.append(info_cliente)
            clientes1[info_cliente['Cedula']]=info_cliente
        elif option== "2":
            imprimir_factura(clientes1)
        elif option== "3":
            print(f"Los clases con carros A fueron {len(carros_A)}")
            print(f"Los clases con carros B fueron {len(carros_B)}")
        elif option== '4':
            print(f"La cantidad de clientes con descuento fueron de {len(clientes_descuento)}")      
        elif option== '5':
            promedio= promedio_pago(carros_A)
            print(promedio_pago(carros_A))
            promedio= promedio_pago(carros_B)
            print(promedio_pago(carros_B))
        elif option== '6':
            print('Gracias pr venir vuelva pronto.')
            break
main()