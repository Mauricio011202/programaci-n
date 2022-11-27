correo= input("Ingrese su correo:")
while len(correo) > 50:
    correo= input("Ingrese su correo:")
while True:
    contador= 0
    for i in correo:
        
        if i== "@":
            contador+=1
        
        if i == " ":
            correo= input("Ingrese su correo:")
            break 


    if contador!= 1:
        correo= input("Ingrese su correo:")
