#=======================================================================
#Mauricio Mendez
#Carnet= 20221110100
#=======================================================================
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


while True:
    opcion= input("""
            1.Ver una serie
            2.Salir
            """)
    if opcion== "1":
        lista_series= {
            "1":"Demon Slayer",
            "2":"Spy × Family",
            "3":"Attack on Titan",
            
            }
        print("Series disponibles:")
        for k,v in lista_series.items():
            
            print(f"{k}:{v}")
          
    serie_elegida= input("Seleccione que serie desea ver marcando un numero: ")
    if serie_elegida== "1":
            for k,v in anime["Demon Slayer"].items():
                
                print(f"{k}:{v}")
            
            
            temporada_elegida= input("Seleccione la temporada que desea ver: ")
            if temporada_elegida== "1":
                
                for k,v in anime["Demon Slayer"]["Temporada 1"][0].items():
                    print(f"{k}:{v}")
            if temporada_elegida== "2":
                
                for k,v in anime["Demon Slayer"]["Temporada 1"][0].items():
                    print(f"{k}:{v}")
    
    if serie_elegida== "2":
            for k,v in anime["Spy × Family"].items():
                
                print(f"{k}:{v}")
            
            
            temporada_elegida= input("Seleccione la temporada que desea ver: ")
            if temporada_elegida== "1":
                lista_de_caps= anime["Spy × Family"]["Temporada 1"]
                for k,v in anime["Spy × Family"]["Temporada 1"][0].items():
                    print(f"{k}:{v}")
                    
        


