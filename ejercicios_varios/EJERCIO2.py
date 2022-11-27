name= input("Nonmbre:  ").capitalize()
apellido= input("Apellido: ").capitalize()
id= input("Cedula:")
if (not id.isnumeric()):
    print("Ingreso no valido, reinicie el sistema")
peso= input("Peso: ")
altura= input("Altura: ")

sport= input("Deporte faorito: ")
nota= input("Promedio academico: ")
idm= float(peso)/float(altura)**2

print(f"""
     Hola, {name} {apellido}.
          Tú numero de cedula es {id}
          Tú peso en kg es {peso}
          Tú altura en mts es{altura}
          Tú deprotefavorito es {sport}
          tú indice de masa muscular es {idm}
          tu promedio academico es {nota}.
          Hasta luego.
            """)
            

    