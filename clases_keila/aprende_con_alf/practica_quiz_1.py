anime = {
    "Demon Slayer": {
        "Temporada 1": [
        {
            "cap": 1,
            "name": "Crueldad",
            "duration": "23:39"
        },
        {
            "cap": 4,
            "name": "Selección final",
            "duration": "23:40"
        },
        {
            "cap": 19,
            "name": "Dios del fuego",
            "duration": "23:40"
        },
        {
            "cap": 26,
            "name": "Una nueva misión",


            "duration": "24:10"
        }
    ],
        "Temporada 2": [
        {
            "cap": 26,
            "name": "Un sueño profundo",
            "duration": "22:55"
        },
        {
            "cap": 43,
            "name": "¡No me rendiré!",
            "duration": "23:40"
        }
    ]
 
        },
    "Spy × Family": {
       
        "Temporada 1":[
        {
            "cap": 4,
            "name": "Objetivo: pasar la entrevista",
            "duration": "24:10"
        },
        {
            "cap": 7,
            "name": "El segundo hijo del objetivo",
            "duration": "24:10"
        }
    ]
    },
    "Attack on Titan": {
        "Temporada 3": [
            {
                "cap": 46,
                "name": "La reina de la muralla",
                "duration": "23:55"
            },
            {
                "cap": 54,
                "name": "Héroe",
                "duration": "23:55"
            }
    ],
        "Temporada 4":[
            {
                "cap": 60,
                "name": "Al otro lado del mar",
                "duration": "23:55"
            },
            {
                "cap": 72,
                "name": "Los hijos del bosque",
                "duration": "23:55"
            }
        ]
        }
}

def mostrar_series_por_nombre(anime: dict):
    for nombre_serie, v in anime.items():
        print('SERIES DISPONIBLES: ')
        print(nombre_serie)

def mostrar_temporadas(anime: dict, serie:str):
    for k, v in anime.items():
        if k == serie:
            for temporada,v2 in v.items():
                print(temporada)
def mostrar_capitulos(anime: dict, serie: str, temporada: str):
    for k,v in anime.items():
        if k == serie:
            for temp, capis in v.items():
                if temp == temporada:
                    for capitulos in capis:
                        for k3,v3 in capitulos.items():
                            print(k3,v3)

def agregar_historial(anime: dict, serie: str, temporada: str,capitulo: str, historial: list):
    for k,v in anime.items():
        if k == serie:
            for temp, capis in v.items():
                if temp == temporada:
                    for capitulos in capis:
                        for k3,v3 in capitulos.items():
                            if k3 == 'cap' and v3== int(capitulo):
                                historial.append(capitulos)
                            
historial= []
def main():
    while True:
        option= input('1. Seleccionar una serie \n2. Ver historial de series vistas \n3. Salir\n=>')
        while option not in ['1','2','3']:
            option= input('1. Seleccionar una serie \n2. ')
        if option == '1':
            mostrar_series_por_nombre(anime)
            serie= input('Escriba el nombre de la serie que desea ver')
            if serie== "Demon Slayer":
                mostrar_temporadas(anime, serie)
                temporada= input('Ingrese el numero de la temporada que desea ver: ')
                temporada= 'Temporada '+temporada
                mostrar_capitulos(anime, serie, temporada )
                capitulo= input('Ingrese el  numero del capitulo que desea ver: ')
                agregar_historial(anime, serie, temporada,capitulo, historial)
                
                print('*****DISFRUTE SU PELICULA MMGVO*******')
            elif serie== "Spy × Family":
                mostrar_temporadas(anime, serie)
                temporada= input('Ingrese el numero de la temporada que desea ver: ')
                temporada= 'Temporada '+temporada
                mostrar_capitulos(anime, serie, temporada )
                capitulo= input('Ingrese el  numero del capitulo que desea ver: ')
                agregar_historial(anime, serie, temporada,capitulo, historial)
                print('*****DISFRUTE SU PELICULA MMGVO*******')
            elif serie== "Attack on Titan":
                mostrar_temporadas(anime, serie)
                temporada= input('Ingrese el numero de la temporada que desea ver: ')
                temporada= 'Temporada '+temporada
                mostrar_capitulos(anime, serie, temporada )
                capitulo= input('Ingrese el  numero del capitulo que desea ver: ')
                agregar_historial(anime, serie, temporada,capitulo, historial)
                print('*****DISFRUTE SU PELICULA MMGVO*******')
        elif option == '2':
            print('****************Tu historial de peliculas es**************************** :')
            for i in historial:
                for k,v in i.items():
                    print(k,v)
            print(f'Has visto {len(historial)} capitulos de series.')
        else:
            print('ADIOS.')




main()

