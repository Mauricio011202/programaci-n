class Cliente:
    def __init__(self, nombre, edad , ci, telf, num_personas):
        self.nombre= nombre
        self.edad= edad
        self.ci= ci
        self.telf= telf
        self.num_personas= num_personas

    def mostrar(self):
        print(f'El cliente {self.nombre} de {self.edad}años de ci: {self.ci} con {self.num_personas} acompanantes reservo:')


        

        