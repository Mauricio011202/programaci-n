
def descuento_nombre(nombre,monto):
        if  "a" in nombre:
            descuento= monto/2
            return descuento

        else:
            return monto


def descuento_cedula(cedula,monto):
        if  cedula%2== 0:
            descuento2= monto/2
            return descuento2

        else:
            return monto
        



def main():
    
    monto= 100
    nombre= input("Ingrese su nombre: ")
    cedula= int(input("Ingrese su cedula: "))
    descuento= descuento_nombre(nombre,monto)
    descuento2= descuento_cedula(cedula,descuento)
    print(descuento2)

main()