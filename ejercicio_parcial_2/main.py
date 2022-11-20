from bebida import Bebida,  Alcoholica, NoAlcoholica
from funciones import inputStr, inputInt
nombre_bebidas: list[str]= []
bebidas_registradas_alcoholicas= []
bebidas_registradas_no_alcoholicas= []
total_bebidas_alcolicas= []
total_bebidas_no_alcolicas= []
num_clientes= 0
clientes= []
total_compras= 0
salir= False
while salir== False:
    option= input('Bienvenido al Saman Bar \n 1. Registrar bebida. \n 2. para registrar una compra \n 3. para salir ')
    while option not in ['1', '2', '3']:
        option= input('Bienvenido al Saman Bar \n 1. Registrar bebida. \n 2. para registrar una compra \n 3. para salir ')

    if option== '1':
        print('Registrar bebida')
        tipo= input('Ingrese  1 para crear una bebidad alcoholica \n ingrese 2 para crear una bebida no alcoholica\n :')
        while tipo not in ['1', '2']:
            tipo= input('Ingrese  1 para crear una bebidad alcoholica ingrese 2 para crear una bebida no alcoholica')
        nombre_beb = inputStr('nombre de la bebida')
        name_beb = inputStr('nombre para la bebida')
    if tipo == '1':
      while name_beb in nombres_bebidas_alcoh_registradas:
        name_beb = inputStr('Error! Bebida alcoholica ya registrada. Ingrese el nombre para la bebida')
      nombres_bebidas_alcoh_registradas.append(name_beb)
    else:
      while name_beb in nombres_bebidas_no_alcoh_registradas:
        name_beb = inputStr('Error! Bebida no alcoholica ya registrada. Ingrese el nombre para la bebida')
      nombres_bebidas_no_alcoh_registradas.append(name_beb)
    price_beb = inputInt('precio de la bebida')
    if tipo == '1':
      degree_beb = inputInt('grado alcoholico de la bebida')
      bebidas_alcoh_registradas.append(Alcoholica(name_beb, price_beb, degree_beb))
    else:
      temperature_beb = inputInt('temperatura de la bebida')
      bebidas_no_alcoh_registradas.append(NoAlcoholica(name_beb, price_beb, temperature_beb))
    print("Bebida creada exitosamente!\n")
