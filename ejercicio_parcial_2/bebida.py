class Bebida:
    def __init__(self, nombre: str, precio: int):
        self.nombre= nombre
        self.precio= precio
    
    

class Alcoholica(Bebida):
    def __init__(self, nombre, precio, grado_alcohol):
        super().__init__(nombre, precio)
        self.grado_alcohol= grado_alcohol
    
    def print_info(self):
        return f'{self.nombre} {self.grado_alcohol}'
    

class NoAlcoholica(Bebida):
    def __init__(self, nombre, precio, temperatura):
        super().__init__(nombre, precio)
        self.temperatura= temperatura
    def print_info(self):
        return f'{self.nombre}{self.temperatura}'
        



    


        