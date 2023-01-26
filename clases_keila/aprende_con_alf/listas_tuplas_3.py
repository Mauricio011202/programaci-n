materias= []
notas= []
nombre= input('Ingrese su nombre: ')
while True:

    opcion= input('1.Inscribir materia \n2. ver notas \n3.Salir')
    if opcion== '1':
        materia= input('Ingrese el nombre de la mateia que desee registrar: ')
        materias.append(materia)
        nota= input('Ingrese la nota obtenida: ')
    elif opcion== '2':
        print(f'Las notas del estudiante {nombre} obtuvo las siguientes notas: ')
        
        for i in range(len(materias)):
            print(f'En la materia {materias[i]} has sacado {notas[i]}')

    elif opcion== '3':
        print('Gacias por venir')
        break
        