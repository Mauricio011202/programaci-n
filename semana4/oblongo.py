
numero=int(input("Ingrese un numero entero: "))
ia_oblongo= False
aux=1
while aux< numero:
    if aux*(aux+1)== numero:
        ia_oblongo= True
        break
    aux+= 1
if ia_oblongo==True:
    print('El numero es oblongo')
else:
    print('No es oblongo')