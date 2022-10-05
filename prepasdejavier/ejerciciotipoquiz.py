

mayus= False
minus= False
todo_listo=False
numeric= False
while todo_listo== False:
    contraseña= input("Ingrese una contrasena :  ")
    
    if len(contraseña) < 8:
        print("debe tener al menos 8 caracteres")
        continue
    contraseña2= list(contraseña) 
    for i in contraseña2:
            if i == i.upper():
                mayus= True
            elif i == i.lower():
                minus= True
    if minus== False or mayus== False:
        print("Debe tener una letra mayuscula y una minuscula")
        continue
    
    if contraseña.isalnum():
        print("Ingrese almenos un caracter alphanumerico")
        continue
    for i in contraseña:
        if i.isnumeric()== True:
            numeric= True
    if numeric!= True:
        print('Ingrese amenos un numero')
    
        continue
    else:
        todo_listo= True
print(f"Su contrasena fue guardada con exito y es {contraseña}")

        
          

        
    
 