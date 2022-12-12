num= int(input('Ingrese el numerador: '))
divisor= int(input('Ingrese el divisor:'))

try:
    divivion= num/divisor
    print(divivion)
except ZeroDivisionError:
    print('No se puede dividir entre 0')