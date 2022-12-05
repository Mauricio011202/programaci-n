class Herramientas:
    def __init__(self, marca, color, precio, tipo):
        self.marca= marca
        self.color= color
        self.precio= precio
        self.tipo= tipo

class Plomeria(Herramientas):
    def __init__(self, marca, color, precio, tipo, pulgadas, ajustables, mantenimiento,cantidad):
        super().__init__(marca, color, precio, tipo)
        self.pulgadas= pulgadas
        self.ajustables= ajustables
        self.mantenimiento= mantenimiento
        self.cantidad= cantidad
    def mostrar(self):
        print(f'''{self.cantidad}x  {self.marca}--- Color:{self.color} Precio por unidad: {self.precio}
        Requiere mantenimiento: {self.mantenimiento} pulgadas: {self.pulgadas} Ajustables: {self.ajustables}''')
   

class Herreria(Herramientas):
    def __init__(self, marca, color, precio, tipo, grados, cantidad):
        super().__init__(marca, color, precio, tipo)
        self.grados= grados
        self.cantidad= cantidad
    def mostrar(self):
        print(f'''{self.cantidad}x  {self.marca}--- Color:{self.color} Precio por unidad: {self.precio}
        Soporte de calor en grados: {self.grados} ''')

class Carpinteria(Herramientas):
    def __init__(self, marca, color, precio, tipo,garantia, cantidad):
        super().__init__(marca, color, precio, tipo)
        self.garantia= garantia
        self.cantidad= cantidad
    def mostrar(self):
        print(f'''{self.cantidad}x  {self.marca}--- Color:{self.color} Precio por unidad: {self.precio}
        Meses de garantia: {self.garantia} ''')


  


        