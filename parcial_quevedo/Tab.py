class Tab:

  def __init__(self, client):
    self.client = client
    self.items = []

  def add_item(self, beverage, quantity):
    self.items.append({
      "product": beverage,
      "quantity": quantity
    })

  def is_prime(self, num):
    if (num == 1 or num == 2):
      return True
    aux = 2
    prime = True
    while aux < num:
      if (num % aux == 0):
        prime = False
        break
      aux += 1
    return prime

  def fibo(self, num):
    if (num == 0 or num == 1):
      return num
    return self.fibo(num - 1) + self.fibo(num - 2)

  def is_fibo(self, num):
    fibo_num = self.fibo(num)
    return num == fibo_num

  def total(self):
    subtotal = sum(list(map(lambda p: p["product"].price * p["quantity"], self.items)))
    discount = 0
    # Descuentos
    if (self.is_fibo(self.client.age)):
      discount = subtotal * 0.05
    if (self.is_prime(subtotal)):
      discount = discount + (subtotal - discount) * 0.1

    return {
      "discount": discount,
      "total": subtotal - discount
    }


  def print_bill(self):
    print(self.client.describe())
    for idx, item in enumerate(self.items):
      print(f'{idx + 1}. {item["product"].describe()} - {item["quantity"]}')
    total_dict = self.total()
    print(f'''
      descuento: {total_dict["discount"]}
      total: {total_dict["total"]}
    ''')


