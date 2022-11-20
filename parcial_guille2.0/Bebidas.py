class Bebida:
  def __init__(self, name: str, price: int):
    self.name = name
    self.price = price

class Alcoholica(Bebida):
  def __init__(self, name: str, price: int, degree: int):
    super().__init__(name, price)
    self.degree = degree

  def print_info(self):
    return f"{self.name} {self.degree}% ---------- ${self.price}\n"

class NoAlcoholica(Bebida):
  def __init__(self, name: str, price: int, temperature: int):
    super().__init__(name, price)
    self.temperature = temperature

  def print_info(self):
    return f"{self.name} {self.temperature}C ---------- ${self.price}\n"


