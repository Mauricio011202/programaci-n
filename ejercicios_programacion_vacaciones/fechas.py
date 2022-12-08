mes= input('Por favor ingrese un mes: ')
while not mes.isnumeric() and int(mes) not in range(1,13):
    mes= input('Por favor ingrese un mes: ')
if mes in ['4','6','9','11']:
    dia= input('Ingrese el dia del mes: ')
    while not dia.isnumeric() and int(dia) not in range(1,31):
        dia= input('Ingrese el dia del mes valido: ')
elif mes== '2':
    dia= input('Ingrese el dia del mes: ')
    while not dia.isnumeric() and int(dia) not in range(1,29):
        dia= input('Ingrese el dia del mes valido: ')
else:
    dia= input('Ingrese el dia del mes: ')
    while not dia.isnumeric() and int(dia) not in range(1,32):
        dia= input('Ingrese el dia del mes valido: ')
        


