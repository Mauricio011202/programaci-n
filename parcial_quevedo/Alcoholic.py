from Beverage import Beverage

class Alcoholic(Beverage):

  def __init__(self, name, price, alc_grd):
    super().__init__(name, price)
    self.alc_grd = alc_grd

  def describe(self):
    return f'{super().describe()}. {self.alc_grd}'
