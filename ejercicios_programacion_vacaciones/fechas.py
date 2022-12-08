
valido= True
mes= input('Por favor ingrese un mes: ')
while not mes.isnumeric():
    mes= input('Por favor ingrese un mes: ')
while  int(mes) not in range(1,13):
    valido= False
    break
if mes in ['4','6','9','11']:
    dia= input('Ingrese el dia del mes: ')
    while not dia.isnumeric() :
        dia= input('Ingrese el dia del mes valido: ')
    while int(dia) not in range(1,31):
        valido= False
        break
elif mes== '2':
    dia= input('Ingrese el dia del mes: ')
    while not dia.isnumeric() :
        dia= input('Ingrese el dia del mes valido: ')
    if  int(dia) not in range(1,29):
        valido= False
else:
    dia= input('Ingrese el dia del mes: ')
    while not dia.isnumeric() :
        dia= input('Ingrese el dia del mes valido: ')
    if  int(dia) not in range(1,29):
        valido= False
anio= input('Ingrese el anio')
if valido== True:
    print('La fecha dia {} del mes {} del anio{} es valida'.format(dia,mes,anio))
elif valido== False:
    print('La fecha ingresada no es valida')






