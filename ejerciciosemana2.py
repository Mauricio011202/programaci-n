from operator import truediv
from pickle import FALSE


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
if y == 0:
    print("Error")
z= print(x/y)

