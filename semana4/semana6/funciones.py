def funcion(edad,nombre):
    print(edad)
    print(nombre)
    edad= int(edad)
    edad=  edad*2
    return edad



#el  main no se pasan parametros
def main():
    y=input("ingrese su edad")
    x= input("Ingrese su nombre ")
    resultado= funcion(y,x)
    print(resultado)
    
main()




