pan= 3.49
descuento= pan*0.6

panesv= input("Ingrese el numero de panes viejos")

while not panesv.isnumeric:
    print("Por favor ingrese undato valido")
panesv= int(panesv)
print(f"El precio de habitual del pan es {pan}$\n ")

print(f"El descuento por cada pan viejo es de {descuento}$\n")

print(f"El monto a cancelar por {panesv} panes es de: {(panesv*pan)-(panesv*descuento)}$ ")

