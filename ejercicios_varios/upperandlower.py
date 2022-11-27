palabra= input("Ingrese una palabra \n").lower


if "a" in palabra:
    palabra = palabra.replace("a","A")

if "e" in palabra:
    palabra = palabra.replace('e','E')

if "i" in palabra:
    palabra = palabra.replace('i','I')

if "o" in palabra:
    palabra = palabra.replace('o','O')

if "u" in palabra:
    palabra = palabra.replace('u','U')

print(palabra)



