class Beverage:

  def __init__(self, name, price):
    self.name = name
    self.price = price

  def describe(self):
    return f'{self.name} - {self.price}'
