
from Bebidas import Alcoholica, NoAlcoholica
from Cliente import Cliente
from funciones import inputInt, inputStr

#TODO: Añadir a lista de la compra del cliente y lista para las compras globales
bebidas_alcoh_registradas: list[Alcoholica] = []
bebidas_no_alcoh_registradas: list[NoAlcoholica] = []
num_clientes = 0
bebidas_alcoh_compradas: list[Alcoholica] = []
bebidas_no_alcoh_compradas: list[NoAlcoholica] = []
total_compras = 0
clientes: list[Cliente] = []

repeat = False
while repeat == False:
  option = input("Bienvenido al Samán Bar:\ningrese 1 para registrar bebida\ningrese 2 para registrar una compra\ningrese 3 para finalizar\n-> ")
  while option not in ['1', '2', '3']:
    option = input("Error!\ningrese 1 para registrar bebida\ningrese 2 para registrar una compra\ningrese 3 para finalizar\n-> ")

  if option == '1':
    print("Registrar Bebida")
    tipo = input("Ingrese 1 para crear una bebida alcholica\nIngrese 2 para crear una bebida no alcoholica\n-> ")
    while tipo not in ['1', '2']:
      tipo = input("Error!\nIngrese 1 para crear una bebida alcholica\nIngrese 2 para crear una bebida no alcoholica\n-> ")

    name_beb = inputStr('nombre para la bebida')
    price_beb = inputInt('precio de la bebida')
    if tipo == '1':
      degree_beb = inputInt('grado alcoholico de la bebida')
      bebidas_alcoh_registradas.append(Alcoholica(name_beb, price_beb, degree_beb))
    else:
      temperature_beb = inputInt('temperatura de la bebida')
      bebidas_no_alcoh_registradas.append(NoAlcoholica(name_beb, price_beb, temperature_beb))
    print("Bebida creada exitosamente!\n")

  elif option == '2':
    print("Comprar")
    name_client = inputStr('nombre del cliente')
    age_client = inputInt('edad del cliente')
    ci_client = inputStr('cédula del cliente') #TODO: Cambiar a Int
    client = Cliente(name_client, age_client, ci_client)
    clientes.append(client) #? No lo piden

    print("Estos son nuestros productos:") #TODO: No esta imprimiendo los productos #BUG
    if (age_client >= 18):
      for i in range(len(bebidas_alcoh_registradas)):
        f"{i}. {bebidas_alcoh_registradas[i].print_info()}"
    for i in range(len(bebidas_no_alcoh_registradas)):
        f"{i}. {bebidas_no_alcoh_registradas[i].print_info()}"
    otra_bebida = True
    while otra_bebida:
      tipo_compra = input("Ingrese 1 para seleccionar una bebida alcholica\nIngrese 2 para seleccionar una bebida no alcoholica\n-> ")
      while tipo_compra not in ['1', '2']:
        tipo_compra = input("Error!\nIngrese 1 para seleccionar una bebida alcholica\nIngrese 2 para seleccionar una bebida no alcoholica\n-> ")
      choice = inputInt("el numero de la bebida que desea comprar")
      if tipo_compra == '1':
        while choice not in range(len(bebidas_alcoh_registradas)):
          choice = inputInt("Ingrese el numero de la bebida que desea comprar.")
        bebidas_alcoh_compradas.append(bebidas_alcoh_registradas[choice]) #TODO: Añadir a lista total y a contadores
      else:
        while choice not in range(len(bebidas_no_alcoh_registradas)):
          choice = inputInt("Ingrese el numero de la bebida que desea comprar.")
        bebidas_no_alcoh_compradas.append(bebidas_no_alcoh_registradas[choice]) #TODO: Añadir a lista total y a contadores
      volver_a_comprar = input("Desea algo más?\n1. Si\n0. No\n->")
      while volver_a_comprar not in ['1', '0']:
        volver_a_comprar = input("Error!\nDesea algo más?\n1. Si\n0. No\n->")
      if volver_a_comprar == '0':
        otra_bebida = False
    print("Factura")
    print("Cliente")
    print(client.print_info())
    print("Productos")
    for bebida in bebidas_alcoh_compradas:
      print(bebida.print_info())
    for bebida in bebidas_no_alcoh_compradas:
      print(bebida.print_info())
    print("Gracias por su compra \n\n\n")
  else:
    repeat = True

print("Estadisticas")

