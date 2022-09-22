
nombre= input("Inresa tu nombre: ")
sex= input("Ingresa tu sexo (M o F)")
if sex== "M":
    if nombre.lower() < "m":
      group= "A"
    else: 
        group= "B"
else:
    if nombre.lower() > "n":
        group= "A"
    else:
        group= "B"
print('Tu grupo es '+ group)
    

