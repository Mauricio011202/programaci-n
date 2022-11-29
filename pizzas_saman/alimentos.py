class Alimentos():
    def __init__(self, tipo, precio):
        self.tipo= tipo
        self.precio= precio
        
class Pizza(Alimentos):
    def __init__(self, tipo, precio, sabor):
        super().__init__(tipo, precio)
        self.sabor= sabor
    def print_info(self):
        return f'Plato:{self.tipo}--sabor:{self.sabor}----precio:{self.precio}'

class Panuzzo(Alimentos):
    def __init__(self, tipo, precio, acompa):
        super().__init__(tipo, precio)
        self.acompa= acompa

    def print_info(self):
        return f'Plato:{self.tipo}--acompanate:{self.acompa}----precio:{self.precio}'
