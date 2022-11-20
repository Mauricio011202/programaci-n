class Cliente:
  def __init__(self, name: str, age: int, ci: str):
    self.name = name
    self.age = age
    self.ci = ci

  def print_info(self):
    return f"{self.name} ---------- CI: {self.ci}\n"
