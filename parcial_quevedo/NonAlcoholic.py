from Beverage import Beverage

class NonAlcoholic(Beverage):

  def __init__(self, name, price, temp):
    super().__init__(name, price)
    self.temp = temp

  def describe(self):
    return f'{super().describe()}. {self.temp}'
