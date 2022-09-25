x= input('Ingrese un numero entero o una palabra: \n')

if x == x[::-1]:
    print(f'{x} es palindromo')
else:
    print(f'{x} no es palindromo')


lista= "1, 2, 3, 4, 5"
#Se usa para leer al reves un string o una lista
print(lista[::-1])


