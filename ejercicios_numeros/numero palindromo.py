numero_introducido= (input('Ingrese un numero: '))

if numero_introducido==numero_introducido[::-1]:
    print('Es un palindromo')
else:
    print('No es palindromo')