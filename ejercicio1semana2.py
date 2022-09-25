x= (input("Escriba un numero"))
#input nos da un string hay pasarlo a int o float
y= (input("Escriba otro un numero"))
is_valid= True

if x.isnumeric():
    x= float(x)
else:
    is_valid= False


if y.isnumeric():
    y= float(y)
else:
    is_valid= False


if is_valid :
    if x== 0:
        print('Error, no se divide entre cero')
    else:
        print(x/y)
else: 
    print('Numeros invalidos ')
    