import requests
class Fifa:
    def __init__(self):
        self.lista_de_equipos = []
        pass
    def inicio(self):
        res= requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json')
        equipos_info= res.json()
        for i in len(equipos_info):
            equipo = Equipos(equipos_info[i])
            self.lista_de_equipos.append(equipo)

class Equipos:
    def __init__(self, diccinario ):
        self.nombre =  diccinario.get('name', 'N/A')
        self.bandera = diccinario.get('flag', 'N/A')
        self.fifa_code = diccinario.get('fifa_code', 'N/A')
        
