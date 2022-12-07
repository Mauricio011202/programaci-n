

def area_circunferencia():
    radio= input('Por favor ingrese el radio de la circunferencia: ')
    while not radio.isnumeric():
        radio= input('Por favor ingrese el radio de la circunferencia: ')
        
    area= (int(radio)**2)*3,1416
    return area

def area_elipse():
    radio_mayor= input('Por favor ingrese el radio mayor del elipse: ')
    while not radio_mayor.isnumeric():
        radio_mayor= input('Por favor ingrese el radio de la circunferencia: ')
    radio_menor= input('Por favor ingrese el radio menor del elipse: ')
    while not radio_menor.isnumeric():
        radio_menor= input('Por favor ingrese el radio de la circunferencia: ')
    area= int(radio_menor)*(radio_mayor)*3,1416
    return area

def area_cuadrado():
    lado= input('Por favor ingrese cuando mide el lado del cuadrado: ')
    while not lado.isnumeric():
        lado= input('Por favor ingrese el radio de la circunferencia: ')
    lado= int(lado)
    area= lado**2
    return area



def main():
    while True:
        print('Bienvedioa la calculadora de areas')
        option= input('Ingrese el area que deee calcular: \n1. Cirunferencia. \n2. Elipse \n3. Cuadrados. \n4. Salir \n=>')
        while option not in ['1','2','3','4']:
            option= input('ERROR! Ingrese el area que deee calcular: \n1. Cirunferencia. \n2. Elipse \n3. Cuadrados. \n4. Salir ')
        if option== '1':
            area = area_circunferencia()
            print('El area de la circunferencia es {}mts '.format(area))
        elif option== '2':
            area = area_elipse()
            print('El area del elipse es {}mts '.format(area))
        elif option== '3':
            area= area_cuadrado()
            print('El area del uadrado es {}mts '.format(area))
        elif option == '4':
            print('POWER OFF')
            break



main()