number= int(input('Ingrese un numero: '))
def vampire_number(number:int):
# Separa el número en dos partes
    first_half = number // 100
    second_half = number % 100

# Si la suma de las dos partes es igual al número original,
# entonces es un número vampiro
    if first_half + second_half == number:
        return True
    else:
        return False
vampire_number(number)