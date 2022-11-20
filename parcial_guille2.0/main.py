
from Bebidas import Alcoholica, NoAlcoholica
from Cliente import Cliente
from funciones import inputInt, inputStr

nombres_bebidas_alcoh_registradas: list[str] = []
nombres_bebidas_no_alcoh_registradas: list[str] = []
bebidas_alcoh_registradas: list[Alcoholica] = []
bebidas_no_alcoh_registradas: list[NoAlcoholica] = []
bebidas_alcoh_compradas: list[Alcoholica] = []
bebidas_no_alcoh_compradas: list[NoAlcoholica] = []
global_bebidas_alcoh_compradas: list[Alcoholica] = []
global_bebidas_no_alcoh_compradas: list[NoAlcoholica] = []
total_compras = 0
num_compras_realizadas = 0
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

  elif option == '2':
    print("Comprar")
    if len(clientes) > 0:
      eres_nuevo = input("Eres nuevo?\n1. Si\n0. No\n=> ")
      while eres_nuevo not in ['0', '1']:
        eres_nuevo = input("Error!\nEres nuevo?\n1. Si\n0. No\n=> ")
      if eres_nuevo == "0":
        for i in range(len(clientes)):
          print( f"{i}. {clientes[i].print_info()}")
        this_client = inputInt("Seleccione su numero de cliente")
        while this_client not in range(len(clientes)):
          this_client = inputInt("Error!\nSeleccione su numero de cliente")
        client = clientes[this_client]
        print(f"Bienvenido {client.name}")
      else:
        name_client = inputStr('nombre del cliente')
        age_client = inputInt('edad del cliente')
        ci_client = inputInt('cédula del cliente')
        client = Cliente(name_client, age_client, ci_client)
        clientes.append(client)
    else:
      name_client = inputStr('nombre del cliente')
      age_client = inputInt('edad del cliente')
      ci_client = inputInt('cédula del cliente')
      client = Cliente(name_client, age_client, ci_client)
      clientes.append(client)

    print("Estos son nuestros productos:")
    if (client.age >= 18):
      for i in range(len(bebidas_alcoh_registradas)):
        print("Bebidas alcoholicas")
        print(f"{i}. {bebidas_alcoh_registradas[i].print_info()}")
    for i in range(len(bebidas_no_alcoh_registradas)):
        print("Bebidas no alcoholicas")
        print(f"{i}. {bebidas_no_alcoh_registradas[i].print_info()}")

    otra_bebida = True
    while otra_bebida:
      if (client.age >= 18):
        tipo_compra = input("Ingrese 1 para seleccionar una bebida alcholica\nIngrese 2 para seleccionar una bebida no alcoholica\n-> ")
        while tipo_compra not in ['1', '2']:
          tipo_compra = input("Error!\nIngrese 1 para seleccionar una bebida alcholica\nIngrese 2 para seleccionar una bebida no alcoholica\n-> ")
      else:
        tipo_compra = '2'
      choice = inputInt("el numero de la bebida que desea comprar")
      if tipo_compra == '1':
        while choice not in range(len(bebidas_alcoh_registradas)):
          choice = inputInt("Ingrese el numero de la bebida que desea comprar.")
        bebidas_alcoh_compradas.append(bebidas_alcoh_registradas[choice])
        global_bebidas_alcoh_compradas.append(bebidas_alcoh_registradas[choice])
      else:
        while choice not in range(len(bebidas_no_alcoh_registradas)):
          choice = inputInt("Ingrese el numero de la bebida que desea comprar.")
        bebidas_no_alcoh_compradas.append(bebidas_no_alcoh_registradas[choice])
        global_bebidas_no_alcoh_compradas.append(bebidas_no_alcoh_registradas[choice])

      volver_a_comprar = input("Desea algo más?\n1. Si\n0. No\n->")
      while volver_a_comprar not in ['1', '0']:
        volver_a_comprar = input("Error!\nDesea algo más?\n1. Si\n0. No\n->")
      if volver_a_comprar == '0':
        otra_bebida = False

    print("Factura")
    print("Cliente")
    print(client.print_info())
    print("Productos")

    subtotal = 0
    for bebida in bebidas_alcoh_compradas:
      subtotal += bebida.price
      print(bebida.print_info())
    for bebida in bebidas_no_alcoh_compradas:
      subtotal += bebida.price
      print(bebida.print_info())
    print(f"\nSubtotal ---------- {subtotal}")

    discount = 0
    print(f"Descuento ---------- {discount}") #TODO

    total = subtotal - discount
    total_compras += total

    print(f"Total ---------- {total}")
    print("Gracias por su compra \n\n\n")
    num_compras_realizadas += 1
    bebidas_alcoh_compradas = []
    bebidas_no_alcoh_compradas = []
  else:
    repeat = True

print("Estadisticas")
print(f"Se vendieron {len(global_bebidas_alcoh_compradas)} bebidas alchólicas")
print(f"Se vendieron {len(global_bebidas_no_alcoh_compradas)} bebidas no alchólicas")
print(f"Compraron {len(clientes)}")

top_alcoh = global_bebidas_alcoh_compradas[0]
top_no_alcoh = global_bebidas_no_alcoh_compradas[0]

for bebida in global_bebidas_alcoh_compradas:
  if top_alcoh != bebida:
    if global_bebidas_alcoh_compradas.count(bebida) > global_bebidas_alcoh_compradas.count(top_alcoh):
      top_alcoh = bebida

for bebida in global_bebidas_no_alcoh_compradas:
  if top_no_alcoh != bebida:
    if global_bebidas_no_alcoh_compradas.count(bebida) > global_bebidas_no_alcoh_compradas.count(top_no_alcoh):
      top_no_alcoh = bebida

print(f"La bebida alcholica más vendida es {top_alcoh.name}")
print(f"La bebida no alcholica más vendida es {top_no_alcoh.name}")
promedio = total_compras / num_compras_realizadas
print(f"El monto promedio por compra es ${promedio}")

