
from NonAlcoholic import NonAlcoholic
from Alcoholic import Alcoholic
from Client import Client
from Tab import Tab

class Bar:

  def __init__(self):
    self.clients = []
    self.items = [
      NonAlcoholic('Coca-Cola', 2, '1'),
      Alcoholic('Cerveza', 1.5, '2'),
      NonAlcoholic('Redbull', 3, 4)
    ]
    self.tabs = []

  def register_client(self):
    name = input('Por favor ingresa tu nombre: ')
    dni = input('Por favor ingresa tu cédula: ')
    age = int(input('Por favor ingresa tu edad: '))
    client = Client(name, dni, age)
    self.clients.append(client)
    return client

  def register_beverage(self):
    name = input('Por favor ingrese el nombre:')
    price = float(input('Por favor ingrese el precio:'))
    is_alcoholic = input('Por favor diga si es alcoholica? (y/n): ').lower() == 'y'
    beverage = None
    if is_alcoholic:
      alc_grd = input('Ingrese los grados de alcohol: ')
      beverage = Alcoholic(name, price, alc_grd)
    else:
      temp = input('Ingrese la temperatura: ')
      beverage = NonAlcoholic(name, price, temp)
    self.items.append(beverage)

  def show_beverages(self, client):
    if (client.age >= 18):
      for idx, item in enumerate(self.items):
        print(f'{idx + 1}. {item.describe()}')
    else:
      for idx, item in enumerate(self.items):
        if (isinstance(item, NonAlcoholic)):
          print(f'{idx + 1}. {item.describe()}')

  def shop(self):
    dni = input('Ingrese su cédula: ')
    client = list(filter(lambda c: c.dni == dni, self.clients))
    if (len(client) == 0):
      client = self.register_client()
    else:
      client = client[0]
    tab = Tab(client)

    ans = 'y'
    while ans == 'y':
      self.show_beverages(client)
      idx = int(input('Por favor seleccionar una bebida: ')) - 1
      quantity: int(input('Por favor ingresa la cantidad: '))
      tab.add_item(self.items[idx], quantity)
      ans = input('Desea continuar? (y/n) ').lower()
    tab.print_bill()
    self.tabs.append(tab)

  def beverage_per_type(self):
    non_alcoholic = 0
    alcoholic = 0
    for tab in self.tabs:
      for item in tab.items:
        if (isinstance(item["product"], Alcoholic)):
          alcoholic += item["quantity"]
        else:
          non_alcoholic += item["quantity"]
    return non_alcoholic, alcoholic

  def amount_of_clients(self):
    return len(self.clients)

  def avg_per_tab(self):
    total = 0
    for tab in self.tabs:
      total += tab.total()["total"]
    return total / len(self.tabs)

  def most_sold_per_type(self):
    alcoholic = None
    non_alcoholic = None

    for tab in self.tabs:
      for item in tab.items:
        if (isinstance(item, Alcoholic)):
          if alcoholic == None:
            alcoholic = item
          else:
            if (alcoholic["quantity"] > item["quantity"]):
              alcoholic = item
        else:
          if (non_alcoholic == None):
            non_alcoholic = item
          else:
            if (non_alcoholic["quantity"] > item["quantity"]):
              non_alcoholic = item

    return non_alcoholic, alcoholic

  def menu(self):
    ans = 'y'

    while ans == 'y':
      option = input('''
        1. Registrar bebida
        2. Realizar compra
        3. Ver estadísticas
      ''')
      if option == '1':
        self.register_beverage()
      elif option == '2':
        self.shop()
      else:
        self.amount_of_clients()
        self.avg_per_tab()
        self.most_sold_per_type()
        self.beverage_per_type()

      ans = input('Desea continuar? (y/n) ').lower()

