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


historial= {}
while True:
        capitulos_vistos= 0
        option= input(""""Ingrese una opcion:
            1. Ver catalogo
            2. Ver historial
            3. Salir
            -->""")
        
        while not (option== "1" or option== "2" or option== "3"):
            option= input("Ingrese una opcion valida: ")
        
        if option== "1":
            
            print("Catalogo disponible:")
            capitulos_vistos+= 1
            for key in anime:
                    print(f"- {key}")
            serie_elegida= input("Por favor ingrese el nombre de la serie que desea ver tal como se muestra en pantalla: ")
            print("*****TEMPORADAS DISPONBLES****")
            for temporada in anime[serie_elegida].keys():
                print(temporada)
            temporada_elegida= input("Seleccione la temporada que desea ver escrito como se muestra en pantalla: ")
            for temporadas in anime[serie_elegida][temporada_elegida]:
                for capitulos, valores in temporadas.items():
                    print(f'{capitulos}: {valores} ')
                print("\n")
            cap_elegido= int(input("Ingrese el numero del capitulo que desea ver"))
            for temporadas in anime[serie_elegida][temporada_elegida]:
                for key, cap in temporadas.items():
                    if key == "cap" and cap == cap_elegido:
                        llave_cap= temporadas
                        
            historial[serie_elegida]= [llave_cap]
        
        if option == "2":
            print('Historial de vistas: ')
            print(historial, end=' ')
            print(f"Numero de capitulos vistos:{capitulos_vistos} ")
        if option == '3':
            print('Gracias por venir. ')