traductor={}
palabras= input("Ingrese las traducciones en el siguiente formato palabra:traduccion separadas por una coma:\n ej casa:House, hola:hello: ")

for i in palabras.split(","):
    llave,valor= i.split(":")
    traductor[llave]=valor
frase= input("Ingrese una frase en espanol")

for i in frase.split():
    if i in traductor:
        print(traductor[i], end= " ")
    else:
        print(i , end= " ")
