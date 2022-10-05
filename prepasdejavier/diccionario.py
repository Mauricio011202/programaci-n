from tkinter.messagebox import YES


datos= {}
nombres= []
apellidos= []
edades= []
x= 'yes'
while x== 'yes':
    given_name= input("Por favor ingresa tu nombre:  ").capitalize()
    nombres.append(given_name)
    datos["Nombres"]= nombres
    dame_apellido= input("Por favor ingresa tu apellido:  ").capitalize() 
    apellidos.append(dame_apellido)
    datos["Apellidos"]= apellidos
    pedir_edad= input("Por favor ingresa tu edad:  ").capitalize() 
    edades.append(pedir_edad)
    datos["Edades"]= edades
    run= input("Quieresseguir agregando datos Y/Yes or N/Nos:  ")
print(datos)

