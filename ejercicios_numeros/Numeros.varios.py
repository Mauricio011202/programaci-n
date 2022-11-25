#numeros primos
num= int(input('Ingresa'))
primo= True
for n in range(2, num):
    if num % n == 0:
       primo= False
if primo==True:
    print('Es primo')

  #Numeros pares 

if num%2==0:
    print('Es par')

#Numeros impares

if num%2!=0:
    print('Es impar')


#Divisores de un numero

for e in range(2,num):
        if num%e==0:
            print(e) #e sera el numero divisor de cada iteracion


#Numeros compuestos:Naturales no primos
compuesto= False
if num>1:
    for n in range(1,num):
        if num%n==0:
            compuesto=True
if compuesto==True:
    print('Compuesto')

#Numero cuadrado

    cuadrado= num**0.5 
    if num==cuadrado**2:
        print('Es cuadrado')

#Numero cubo
    cuadrado= num**(1/3)
    if num==cuadrado**3:
        print('Es cubo')


'''Número feliz: todo número natural que cumple que si sumamos los cuadrados de sus dígitos y seguimos el proceso con los resultados 
obtenidos el resultado es 1. Por ejemplo, el número 203 es un número feliz ya que 22+02+32=13; 12+32=10; 12+02=1.'''

numero = input("Ingrese un numero:")
while len(str(numero)) > 1:
    resultado = 0
    for i in numero:
        resultado += int(i)**2
    numero = str(resultado)
if resultado == 1:
    print("Feliz")
else:
    print("No es feliz")



'''Problema 1 (7pts):
	Se propone que se implemente un algoritmo que, dado un número introducido por el usuario*, diga si ese número es primo de Fermat.
 
Definiciones:
Número de Fermat: todo número natural de la forma (2^(2^n)) + 1 para algún n. Si ese número resulta ser primo, se denomina primo de Fermat.
 
*debe validarse que el input sea un número natural.'''



numero_introducido= int(input('Ingrese un numero: '))
primo=True



if numero_introducido>=1:
    for numeros in range(0,numero_introducido):
        if 2**(2**numeros)+1==numero_introducido:
            fermat=True
            break
        else:
            fermat=False
else:
    print('Debes introducir un numero natural')



for n in range(2,numero_introducido):
    if numero_introducido % n==0:
        primo=False
        break
    else:
        primo= True

if primo==True and fermat==True:
    print('Es un primo fermat')
elif primo==True and fermat==False:
    print('Es primo pero no fermat')
elif primo==False and fermat==True:
    print('No es primo pero es fermat')
else:
    print('No es fermat ni primo')



#Numero narcicista
num= input('Ingresa un numero: ')
largo= len(num)
contador=0
resultado=0

for digito in num:
    digito=int(digito)
    resultado= digito**largo
    contador+=resultado

if contador==int(num):
    print('Es narcicista') 


#Numero dracula
num = input('Ingrese un número: ')

if len(num) > 3:
  for i in range(num):
    for j in range(num):
      if (len(i) == len(j)) and (i*j == num):
        if (i[-1] == 0 and j[-1]!=0) or (i[-1] != 0 and j[-1] == 0):
          print('Es un número dracula')
        else:
          print('No cumple los parametros para ser un número dracula')
      else:
        print('El número ingresado no es un número dracula')

'''
Número poderoso: todo número natural n que cumple que si un primo p es un divisor suyo entonces p**2 también lo es. Por ejemplo, 
el número 36 es un número poderoso ya que los únicos primos que son divisores suyos son 2 y 3 y se cumple que 4 y 9 también son divisores
 de 36.'''

n= input('Ingresa un numero')
lista_divisores=[]
lista_primosd=[]
nueva=[]
primo= True

while n>1:
    for e in range(2,n):
        if n%e==0:
            lista_divisores.append(e)
    for k in lista_divisores:
        for l in range(2,k):
            if k % l == 0:
                primo==False
            else:
                lista_primosd.append(k)

if primo==True:
    for s in lista_primosd:
        cuadrados=s**2
        nueva.append(cuadrados)

if lista_divisores==lista_primosd:
    print('Es poderoso')

    

            
            



'''Número perfecto: todo número natural que es igual a la suma de sus divisores propios (es decir, todos sus divisores excepto el propio número).
 Por ejemplo, 6 es un número perfecto ya que sus divisores propios son 1, 2, y 3 y se cumple que 1+2+3=6. Los números 28, 496 y 8128 
 también son perfectos.'''

num= int(input('Ingresa un numero:'))
divisores= []
for e in range(2,num):
        if num%e==0:
            divisores.append(e)

suma_divisores= sum(divisores)
if suma_divisores==num:
    print('Es un numero perfecto')