class Persona:
    def __init__(self,nombre: str, apellido:str) :
        self.nombre= nombre
        self.apellido= apellido
        
class Ingeniero(Persona):
    def __init__(self, nombre: str, apellido: str, tipo: str, horas_de_trabajo: int, sueldo):
        super().__init__(nombre, apellido)
        self.tipo= tipo
        self.horas_de_trabajo= horas_de_trabajo
        self.sueldo= sueldo
    def print_info(self):
        return f'{self.nombre}{self.apellido}-------------especialidad:{self.tipo}horas trebajadas:{self.horas_de_trabajo}'

class Arquitecto(Persona):
    def __init__(self, nombre: str, apellido: str, tipo: str, horas_de_trabajo: int, sueldo):
        super().__init__(nombre, apellido)
        self.tipo= tipo
        self.horas_de_trabajo= horas_de_trabajo
        self.sueldo= sueldo
    def print_info(self):
        return f'{self.nombre}{self.apellido}-------------especialidad:{self.tipo}horas trebajadas:{self.horas_de_trabajo}'

class Obrero(Persona):
    def __init__(self, nombre: str, apellido: str, tipo: str, horas_de_trabajo: int, sueldo):
        super().__init__(nombre, apellido)
        self.tipo= tipo
        self.horas_de_trabajo= horas_de_trabajo
        self.sueldo= sueldo
    def print_info(self):
        return f'{self.nombre}{self.apellido}-------------especialidad:{self.tipo}horas trebajadas:{self.horas_de_trabajo}'