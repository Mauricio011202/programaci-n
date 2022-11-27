

#Como lo hace el profe
diccionaro= {}
while True:
    key_name= input("Que tipo de daot quieres guardar? ejemplo: Nombre, TElefono")
    value=input("Por favor ingrese un dato : ")
    diccionaro[key_name]= value
    for key, value in diccionaro.items():
        print(f" Tu {key} is {value}")
    if input("Quieres seguir sali:  \n Y-Yes \n N-No ")== "Y":
        break
