lista_A= []
    
lista_B= []
promedio_a=[]
promedio_b=[]
promedio_r=[]
rechazado= []
estudiantes= {}
estudiante={}
print("*****BIENVENIDO A LA UNIVERSIDAD*****")
while True:
    option= input("""Seleccione una opcion:
                    1. Agregar un estudiante
                    2. Ver en que grupo estan los estudiantes
                    3. Ver informacion de un estudiante
                    4. Ver cantidad total de aspirantes.
                    5. Ver cantidad de alumnos por cada grupo.
                    6. Ver el promedio por trimestre.
                    7. Salir.
                    : """)
    if option == "1":
        estudiante= {"Nombre": input("Ingrese su nombre: ").capitalize(), 

                    "Cedula": input("Ingrese su cedula: "),

                    "promedio": int(input("Ingrese su promedio academico: "))

            }
        if estudiante["promedio"] >= 18:
            estudiante["lista"]="A"
            lista_A.append(estudiante)
        elif estudiante["promedio"] >= 12:
            estudiante["lista"]="B"
            lista_B.append(estudiante)
        elif estudiante["promedio"] <= 12:
            estudiante["lista"]="Rechazado"
            rechazado.append(estudiante)
        estudiantes[estudiante["Cedula"]]=estudiante
        print("El estudiante fue agregado con exito")
    elif option == "2":
        print(f"lista A: {lista_A} ")
        print(f"lista B: {lista_B} ")
        print(f"lista de Rechazados: {rechazado} ")
    elif option == "3":
        buscar_estudiante= input("Ingrese la cedula del estudiante que desea buscar: ")
        for k,v in estudiantes.items():
            if k == buscar_estudiante:
                print("**** INFO DEL ESTUDIANTE ****")
                for datos, resultados in v.items():            
                
                    print(f"{datos} : {resultados}")
    elif option == "4":
        aspirantes_en_a=(len(lista_A))
        aspirantes_en_b=len(lista_B)
        aspirantes_en_r=len(rechazado)
        total_aspirantes= aspirantes_en_a + aspirantes_en_b + aspirantes_en_r
        print(f"Cantidad total de aspitante: {total_aspirantes}")
    elif option== "5":
        if len(aspirantes_en_a)>0:
            print(f"Cantidad de aspirantes en el grupo A :{aspirantes_en_a}")
        elif len(aspirantes_en_b)>0:
            print(f"Cantidad de aspirantes en el grupo B :{aspirantes_en_b}")
        elif len(aspirantes_en_r)>0:
            print(f"Cantidad de aspirantes en el grupo de rechazados: {aspirantes_en_r}")
        else:
            print("No hay estudiantes")
    elif option== "6":
        for i in lista_A:
            for k,v in i.items():
                if k == "promedio":
                    promedio_a.append(v)
                    promedi_final_a= sum(promedio_a)/len(promedio_a)
                    print(f"El promedio en el curso A es de {promedi_final_a}")
        for i in lista_B:
            for k,v in i.items():
                if k == "promedio":
                    promedio_b.append(v)
                    promedi_final_b= sum(promedio_b)/len(promedio_b)
                    print(f"El promedio en el curso B es de {promedi_final_b}")
        for i in rechazado:
            for k,v in i.items():
                if k == "promedio":
                    promedio_r.append(v)
                    promedi_final_r= sum(promedio_r)/len(promedio_r)
                    print(f"El promedio en el curso Rechazados es de {promedi_final_r}")
    elif option== "7":
        print("Gracias por venir vuelva pronto")
        break



