class Alimento:
    def __init__(self, nombre: str, precio: int):
        self.nombre= nombre
        self.precio= precio

class Comida(Alimento):
    def __init__(self, nombre: str, precio: int, tipo: str, sabor: str):
        super().__init__(nombre, precio)
        self.tipo= tipo
        self.sabor= sabor

class Bebida(Alimento):
    def __init__(self, nombre: str, precio: int, grado_alcohol: str, temperatura: str):
        super().__init__(nombre, precio)
        self.grado_alcohol= grado_alcohol
        self.temperatura= temperatura

