def datos_clientes():
    info_cliente=[]
    nombre=input('Por favor ingrese su nombre:\n').capitalize()
    edad=input('Por favor ingrese su edad:\n')
    while  not edad.isnumeric():
        edad=input('Por favor ingrese su edad:\n')
    cedula=input('Por favor introduzca su cedula:\n')
    while not cedula.isnumeric():
        cedula=input('Por favor introduzca su cedula:\n')
    telefono=input('Por favor introduzca su numero de telefono:\n')
    while not telefono.isnumeric():
        telefono=input('Por favor introduzca su numero de telefono:\n')
    
    info_cliente.append(nombre)
    info_cliente.append(edad)
    info_cliente.append(cedula)
    info_cliente.append(telefono)
    return info_cliente


def comprar_herramienta():
    herramienta= input('Seleccione el tipo de herramienta que desea comprar:\n1-Herramienta de Plomeria\n2-Herramienta de Herrería\n3-Herramienta de Carpintería\n-->')
    while herramienta!='1' and herramienta!='2' and herramienta!='3':
         herramienta= input('Seleccione el tipo de herramienta que desea comprar:\n1-Herramienta de Plomeria\n2-Herramienta de Herrería\n3-Herramienta de Carpintería\n-->')
    return herramienta


def imprimir_factura(cliente,herramientas_plomeria,herramientas_carpinteria,herramientas_herreria,total,descuento_abundante):
    print('****FACTURA***')
    print(f'Cliente: {cliente[0]}')
    print(f'Edad:{cliente[1]}')
    print(f'Cedula: {cliente[2]}')
    print(f'Telefono: {cliente[3]}')
    if herramientas_plomeria!=[]:
        for herramienta in herramientas_plomeria:
            print(f'Herramienta Marca {herramienta[0]}')
            print(f'Color:{herramienta[1]}')
            print(f'Precio:{herramienta[2]}')
            print(f'Tipo: Plomeria')
            print(f'Pulgadas: {herramienta[4]}')
            print(f'Ajustable:{herramienta[5]}')
            print(f'Mantenimiento:{herramienta[6]}\n')
    elif herramientas_herreria!=[]:
          for herramienta in herramientas_herreria:
            print(f'Herramienta Marca {herramienta[0]}')
            print(f'Color:{herramienta[1]}')
            print(f'Precio:{herramienta[2]}')
            print(f'Tipo: {herramienta[3]}')
            print(f'Grados que soporta: {herramienta[4]}\n')
    elif herramientas_carpinteria!=[]:
         for herramienta in herramientas_carpinteria:
            print(f'Herramienta Marca {herramienta[0]}')
            print(f'Color:{herramienta[1]}')
            print(f'Precio:{herramienta[2]}')
            print(f'Tipo: {herramienta[3]}')
            print(f'Años de Garantia:{herramienta[4]}\n')
    monto_total=sum(total)
    descuento_primo=primo(monto_total)
    if descuento_primo==1:
        descuento=10/100
        monto=monto_total*descuento
        monto_total=monto_total-monto

    if descuento_abundante==1:
        descuento_a=10/100
        mont=monto_total*descuento_a
        monto_total=monto_total-mont
    print(f'Monto total:{monto_total}')




def divisores(numero_introducido):
    divisores= []
    for n in range(1,numero_introducido):
        if numero_introducido%n==0:
            divisores.append(n)
        else:
            pass
    return divisores
 
def comprobacion(d,edad):
    if sum(d)>edad:
        return 1
    else:
        return 0

def abundante(edad):
    d=divisores(edad)
    c=comprobacion(d,edad)
    return c

def primo(total):
    primo= True
    for n in range(2, total):
        if total % n == 0:
            primo= False
    if primo==True:
        return 1


