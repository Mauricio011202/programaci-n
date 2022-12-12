def paridad():
    num= input('Ingrese un numero para verificar si es par o impar:\n=>')
    while not num.isnumeric():
        num= input('ERROR! Ingrese un numero para verificar si es par o impar:\n=>')
    
    if num[-1] in ['0','2','4','6','8']:
        print('El numero {} es par'.format(num))
    else:
        print('El numero {} es impar'.format(num))
def main():
    paridad()
main()