class Cliente:
    def __init__(self, nombre, edad, ci):
        self.nombre = nombre
        self.edad = edad
        self.ci = ci
    def prin_info(self):
        return f'{self.nombre}-------------{self.ci}'
