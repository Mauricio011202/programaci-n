class Herramienta:
    def __init__(self,marca,color,precio,tipo):
        self.marca=marca
        self.color=color
        self.precio=precio
        self.tipo=tipo


class Plomeria(Herramienta):
    def __init__(self, marca, color, precio, tipo,pulgadas,ajustable,mantenimiento):
        super().__init__(marca, color, precio, tipo)
        self.pulgadas=pulgadas
        self.ajustable=ajustable
        self.mantenimiento=mantenimiento
    
    def mostrar_herramienta(self):
        plomeria=[self.marca,self.color,self.precio,self.tipo,self.pulgadas,self.ajustable,self.mantenimiento]
        return plomeria


class Herreria(Herramienta):
    def __init__(self, marca, color, precio, tipo,grados_celsius):
        super().__init__(marca, color, precio, tipo)
        self.grados_celsius=grados_celsius
    
    def mostrar_herramienta(self):
        herreria=[self.marca,self.color,self.precio,self.tipo,self.grados_celsius]
        return herreria

class Carpinteria(Herramienta):
    def __init__(self, marca, color, precio, tipo,garantia):
        super().__init__(marca, color, precio, tipo)
        self.garantia=garantia

    def mostrar_herramienta(self):
        carpinteria=[self.marca,self.color,self.precio,self.tipo,self.garantia]
        return carpinteria


