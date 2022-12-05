class Trabajador:
    def __init__(self,nombre,apellido,cedula,tipo_trabajador,horas_trabajo,month,especialidad):
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula
        self.tipo_trabajador=tipo_trabajador
        self.horas_trabajo=horas_trabajo
        self.month=month
        self.especialidad=especialidad


    def empleado(self):
        empleado=self.nombre+'//'+self.apellido+'//'+self.cedula+'//'+self.tipo_trabajador+'//'+self.horas_trabajo+'//'+self.month+'//'+self.especialidad
        return empleado