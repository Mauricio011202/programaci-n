class Cliente:
    def __init__(self, nombre, edad, ci, telf) :
        self.nombre= nombre
        self.edad= edad
        self.ci = ci
        self.telf = telf
    def mostrar(self):
        print(f'Nombre: {self.nombre} edad: {self.edad} ci: {self.ci} telf: {self.telf}')
        