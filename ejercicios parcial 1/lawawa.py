def main():
    bd=[]
    info=[{"Codigo":"v", "Destino":"Valencia", "Costo":500, "Capacidad":30},
    {"Codigo":"p", "Destino":"Puerto La Cruz", "Costo":700,"Capacidad":30},
    {"Codigo":"b","Destino":"Barquisimeto", "Costo":800,"Capacidad":30}]
    menu(info,bd)

def menu(info,bd):
    menu_bool=True

    print("*******BIENVENIDO *******")
    while menu_bool:
        option=int(input('''Seleccione que quiere hacer hoy:\n1.- Registrar clientes
                                                            \n2.- Ver estadísticas del día
                                                            \n3.-Salir\n==>''')) 
        if option==1:
            registrar(info,bd)
        if option==2:
            estadísticas(bd)
        if option==3:
            print("Gracias por preferirnos!")
            print("Saliendo...")
            menu_bool=False
            

def registrar(info,bd):
    registrar_bool=True
    other_bool=True
    while registrar_bool:
        destiny=input("Seleccione el destino a ir:\nV.-Valencia\nP.-Puerto La Cruz\nB.-Barquisimeto\n==>").lower()
        for dict in info:
            if dict["Codigo"]==destiny:
                if dict["Capacidad"]==0:
                    print("No hay más tickets para el destino seleccionado")
                else:
                    registrar_bool=False
    viaje=None
    while other_bool:
        ticket=int(input("Cuándo tickets desea comprar? "))
        for dict in info:
            if dict["Codigo"]==destiny:
                if ticket<=dict["Capacidad"]:
                    viaje=dict 
                    other_bool=False
                    dict["Capacidad"]-=ticket
                else:
                    print("Papi no puedes comprar más de 30 tickets") 
    dni=input("Ingrese su dni: ")
    factura(ticket,viaje,dni,bd)

def factura(ticket,viaje,dni,bd):
    subtotal=ticket*viaje["Costo"]
    iva=0.16*subtotal
    total=subtotal+iva
    descuento=0
    if ticket>4:
        descuento=total*0.20
    new_client={"Cédula":dni,"Destino":viaje['Destino'],"Codigo":viaje['Codigo'], "Boletos comprados":ticket, "Subtotal":subtotal,"Descuento":descuento,"IVA":iva,"Total":total}
    print("*******FACTURA*********")
    print(f"Cédula: {dni}")
    print(f"Destino: {viaje['Destino']} Codigo: {viaje['Codigo']}")
    print(f"Boletos comprados: {ticket}")
    print(f"Subtotal: {subtotal}")
    print(f"Descuento: {descuento}")
    print(f"IVA:{iva-descuento}")
    print(f"Total a pagar: {total-descuento}")
    bd.append(new_client)

def estadísticas(bd):
    monto_v=0
    monto_p=0
    monto_b=0
    client_v=0
    client_p=0
    client_b=0
    descuentos_v=0
    descuentos_p=0
    descuentos_b=0
    highest_pay_client=bd[0]
    for client in bd:
        if client["Codigo"]=="v":
            client_v+=1
            monto_v+=client['Total']
            if client['Descuento']!=0:
                descuentos_v+=monto_v
        if client["Codigo"]=="p":
            client_p+=1
            monto_p+=client['Total']
            if client['Descuento']!=0:
                descuentos_p+=monto_p
        if client["Codigo"]=="b":
            client_b+=1
            monto_b+=client['Total']
            if client['Descuento']!=0:
                descuentos_b+=monto_b
        if client['Total']>highest_pay_client['Total']:
            highest_pay_client=client
    
    print("*******ESTADÍSTICAS*********")
    print("------------------")
    print(f'''Cantidad clientes por destino:
                Valencia: {client_v}
                Puerto La Cruz: {client_p}
                Barquisimeto: {client_b}''')
    print("------------------")
    print(f'''Monto total facturado por destino:
                Valencia: {monto_v}
                Puerto La Cruz: {monto_p}
                Barquisimeto: {monto_b}''')
    print("------------------")
    print(f'''Monto de descuentos total facturado por destino:
                Valencia: {descuentos_v}
                Puerto La Cruz: {descuentos_p}
                Barquisimeto: {descuentos_b}''')
    print("------------------")
    print(f'''Monto total facturados por Expresos Samán
                Total facturado: {monto_b+monto_p+monto_v}''')
    print("------------------")
    print(f'''El cliente que más pagó: 
                Cédula:{highest_pay_client["Cédula"]}
                Pagó: {highest_pay_client["Total"]}''')
    
main()
    