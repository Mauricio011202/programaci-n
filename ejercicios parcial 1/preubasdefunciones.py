info=[{"Codigo":"v", "Destino":"Valencia", "Costo":500, "Capacidad":30},
    {"Codigo":"p", "Destino":"Puerto La Cruz", "Costo":700,"Capacidad":30},
    {"Codigo":"b","Destino":"Barquisimeto", "Costo":800,"Capacidad":30}]
viaje= None
ticket=int(input("Cuándo tickets desea comprar? "))
for dict in info:
            if dict["Codigo"]=='v':
                if ticket<=dict["Capacidad"]:
                    viaje=dict 
                    other_bool=False
                    dict["Capacidad"]-=ticket
print(viaje)
        