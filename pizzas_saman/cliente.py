class Cliente:
    def __init__(self, nombre, apellido, ci, telefono, alergico):
        self.nombre= nombre
        self.apellido=apellido
        self.ci=ci
        self.telefono=telefono
        self.alergico=alergico
    def print_info(self):
        return f'Nombre:{self.nombre}--apellido:{self.apellido}----ci:{self.ci}----telefono: {self.telefono}---alergias: {self.alergico}'