print('Bievenido al cine ')
edad= input('Por favo ingrese su edad: ')

while not edad.isnumeric():
    edad= input('Por favo ingrese su edad: ')

edad= int(edad)
monto= 0
if edad < 4:
    monto= 0
elif 4<=edad<18: 
    monto= 10
elif edad>= 18:
    monto= 14
if monto == 0:
    monto= 'GRATIS'
print('********FACTURA********')
print(f'Edad: {edad}')
print(f'Monto: {monto} $')