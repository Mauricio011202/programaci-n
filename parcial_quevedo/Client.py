class Client:

  def __init__(self, name, dni, age):
    self.name= name
    self.dni= dni
    self.age= age

  def describe(self):
    return f'{self.name}, {self.dni}, {self.age}'
