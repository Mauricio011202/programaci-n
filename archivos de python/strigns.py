# STRINGS O CADENAS
myStr= "hello world"
print(dir(myStr))
# dir nos permite saber que podemos hacer con las variables, comopodemos jugar con ellas
print(myStr.upper())
# Todo MAYUSCULA
print(myStr.lower())
# Todo minisucla
r= "HOLA BUENOS DIAS ESTOY APRENDIENDO PYTHON"
print(r.lower())
print(r.capitalize())
#mayuscula la primera
print(r.replace("ESTOY APRENDIENDO", "YA APRENDÍ").capitalize())
#reemplazar parte de la variable por otro y mayuscula junto
print(r.count("E"))
#para contar el numero de caracteres se un .count
print(r.startswith("HOLA"))
print(r.endswith("HOLA"))
#ver si empiza con diferentes caracteres
print(r.split())
#split separa a partir de none pero puede ser mediante otro caracter que sea asignado
print(r.find("n"))
# parabuscar el numero de la osiscion de un caracter

print(len(r))
#para buscar el numero decaracteres del strings
print(r.index("S"))
print(r.isnumeric())
print(r.isalpha())

print(r[4])
#para imprimir directamenteun caracter 
