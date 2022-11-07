class Redactor:
    def __init__(self, nombre, ci, seccion) -> None:
        self.nombre=nombre
        self.cedula= ci
        self.seccion= seccion
    def escribir_articulo(self):
        print('Estoy escribiendo un articulo')

class JefeRedactor(Redactor):
    def __init__(self, nombre, ci, seccion, redactores) -> None:
        super().__init__(nombre, ci, seccion)
        grupo_de_redactores= redactores
    def surpervisar(self):
        print('Todo esta bien')
    def decidir(self, articulo):
        print('El articulo fue aprobado')