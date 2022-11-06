class Employee:
  def __init__(self, firstName: str, lastName: str, id: int, pay: int):
    self.firstName = firstName
    self.lastName = lastName
    self.id = id
    self.pay = pay

  def information(self):
    print(f"Nombre: {self.firstName} {self.lastName}\nSueldo: ${self.pay}\n")

class Developer(Employee):
  def __init__(self, firstName: str, lastName: str, id: int, pay: int, prog_lang: str):
    super().__init__(firstName, lastName, id, pay)
    self.prog_lang = prog_lang

class Accountant(Employee):
  def __init__(self, firstName: str, lastName: str, id: int, pay: int, title: str):
    super().__init__(firstName, lastName, id, pay)
    self.title = title

class HR(Employee):
  def __init__(self, firstName: str, lastName: str, id: int, pay: int, psychologist: bool):
    super().__init__(firstName, lastName, id, pay)
    self.psychologist = psychologist
