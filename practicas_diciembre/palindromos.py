algo= input('Por favor un ingreses una palabra o numero paraverificar si es palindromo o no: \n =>').lower()

if algo == algo[::-1]:
    print('El dato introducido es palindromo')
else:
    print('El dato introducido no es palindromo')