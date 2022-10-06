colegio = []

print("Bienvenido!")
while True:
    option = input("""
    1. Agregar estudiante
    2. Mostrar datos
    3. Borrar estudiante
    4. Calcular notas
    5. Ver estudiantes por año
    6. Sumar indice 2 y 7 de la ci
    7. Ver colegio
    Cuaquier otra tecla. Salir
    Elije la opcion que quieras realizar: """)

    if option == "1":
        estudiante = []
        calificaciones = []
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        ci = input("Ingrese la cedula: ")
        curso = input("Ingrese el año: ")
        calif1 = input("Ingrese calificacion del primer parcial: ")
        calif2 = input("Ingrese calificacion del segundo parcial: ")

        estudiante.append(nombre)
        estudiante.append(apellido)
        estudiante.append(ci)
        estudiante.append(curso)
        calificaciones.append(calif1)
        calificaciones.append(calif2)
        estudiante.append(calificaciones)

        colegio.append(estudiante)

        print("Se ha registrado el estudiante exitosamente!")




    elif option == "2":
        option = input("1. Buscar por nombre\n2. Buscar por Cedula\nPulse cualquier otra tecla para retroceder\nIngrese el numero de la opcion que quiere realizar: ")
        if option == "1":
        
            if len(colegio) != 0:
                buscar = input("Ingrese el nombre del estudiante: ")
                conseguido = False
                for i in colegio:
                    if buscar == i[0]:
                        print(f"\nNombre: {i[0]}\nApellido: {i[1]}\nCedula: {i[2]}\nCurso: {i[3]}\nCalificaciones:\n  1. {i[4][0]}\n  1. {i[4][1]}")
                        conseguido == True
                if conseguido == False:
                    print("\nEl estudiante no se encuentra registrado")
            else:
                print("No hay estudiantes en el colegio")

        elif option == "2":

            if len(colegio) != 0:
                buscar = input("Ingrese la cedula del estudiante: ")
                conseguido = False
                for i in colegio:
                    if buscar == i[2]:
                        print(f"\nNombre: {i[0]}\nApellido: {i[1]}\nCedula: {i[2]}\nCurso: {i[3]}\nCalificaciones:\n  1. {i[4][0]}\n  1. {i[4][1]}")
                        conseguido == True
                if conseguido == False:
                    print("\nEl estudiante no se encuentra registrado")
            else:
                print("No hay estudiantes en el colegio")
    


    elif option == "3":
        borrar = input("Ingrese la cedula del estudiante que quiere borrar: ")
        conseguido = False
        for i in colegio:
            if borrar == i[2]:
                colegio.remove(i)
                print("Se ha borrado el estudiante existosamente")
                conseguido = True
        if conseguido == False:
            print("El estudiante no se encuentra registrado")
        
    
    elif option == "4":
        nota = input("Ingrese la cedula del estudiante que quiere calcular nota: ")
        conseguido = False
        for i in colegio:
            if nota == i[2]:
                promedio = (int(i[4][0]) + int(i[4][1]))/2
                print(f"El estudiante {i[0]} saco {promedio}")
                conseguido == True
        if conseguido == False:
            print("El estudiante no se encuentra registrado")

    elif option == "5":
        curso = input("Ingrese el curso que desea ver: ")
        conseguido = False
        for i in colegio:
            if curso == i[3]:
                print(f"\nNombre: {i[0]}\nApellido: {i[1]}\nCedula: {i[2]}")
                conseguido == True
        if conseguido == False:
            print("\nNo hay estudiantes registrados")

    elif option == "6":
        calcular_ci = input("Ingrese la cedula del estudiante que quiere calcular ci: ")
        conseguido = False
        for i in colegio:
            if calcular_ci == i[2]:
                ci_lista = list(i[2])
                ci_lista = int(ci_lista[2]) + int(ci_lista[7])
                print(f"La ci es {i[2]} suma de los dos digitos (indice 2 y 7) es: {ci_lista}")
                conseguido == True
        if conseguido == False:
            print("\nNo hay estudiantes registrados")

    elif option == "7":
        print(colegio)

    else:
        print("Muchas gracias por usarme")
        break