"""
El programa deberá ofrecer las siguientes funcionalidades:
- Guardar el nombre de estudiantes ingresados por consola, su cédula y sus asignaturas
cursantes.
- Imprimir el nombre de los estudiantes almacenados en la base de datos, seguido de
su respectiva cédula y las asignaturas que cursa. De esta forma:
“Nombre: Rommel Sanzonetti,
Cédula: 28013672,
Asignaturas: Matemáticas 3, Algoritmos, Estructuras de Datos”.
- Eliminar el estudiante del simulador de base de datos (eliminando así su respectiva
cédula y las respectivas materias cursantes del mismo).

"""
while True:
        option=input("""
        1. ingrese alumno
        2. Mostrar alumnos
        3. Eliminar alumno
        4. Salir
        """)
        while option != "1" and option != "2" and option != "3" and option != "4":
            option=input("Ingrese una opcion valida")
