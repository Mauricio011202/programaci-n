def jugar(intento: int):
    respuesta = input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print ("\nFallaste! Inténtalo de nuevo")
            intento += 1
            jugar(intento)
        else:
            print ("\nPerdiste!")
    else:
        print ("\nGanaste!")
jugar(1)
