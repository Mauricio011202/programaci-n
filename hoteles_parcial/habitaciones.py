class Habitacion:
    def __init__(self, camas, baños, precio):
        self.camas= camas
        self.baños= baños
        self.precio= precio
    def mostrar_hab(self):
        print(f"Hbitaciones de {self.precio} con {self.baños}baños y {self.camas}camas ")

class Suite(Habitacion):
    def __init__(self, camas, baños, precio, jacuzzi):
        super().__init__(camas, baños, precio)
        self.jacuzzi= jacuzzi

class Doble(Habitacion):
    def __init__(self, camas, baños, precio, tipo):
        super().__init__(camas, baños, precio)
        self.tipo= tipo

class Sencilla(Habitacion):
    def __init__(self, camas, baños, precio, tv):
        super().__init__(camas, baños, precio)
        self.tv= tv




