operacion= int(input("""Seleccione que condicion desea realizar:
           1. Suma
           2. Resta
           3. Multiplicación
           4. División
           5. Potencia
           6. Módulo
           7. Comparar (mayor o menor que)
           8. Valor absoluto
"""))

if operacion== 1:
    a= int(input("Ingrese un numero"))
    b= int(input("Ingrese otro numero"))
    print(a+b)

if operacion== 2:
    a= int(input("Ingrese un numero"))
    b= int(input("Ingrese otro numero"))
    print(a-b)

if operacion== 3:
    a= int(input("Ingrese un numero"))
    b= int(input("Ingrese otro numero"))
    print(a*b)


if operacion== 4:
    a= int(input("Ingrese un numero"))
    b= int(input("Ingrese otro numero"))
    print(a/b)

if operacion== 5:
    a= int(input("Ingrese un numero"))
    b= int(input("Ingrese otro numero"))
    print(a**b)

if operacion== 6:
    a= int(input("Ingrese un numero"))
    b= int(input("Ingrese otro numero"))
    print(a%b)

if operacion== 7:
    a= int(input("Ingrese un numero"))
    b= int(input("Ingrese otro numero"))
    if a>b:
        print(f"{a}>{b}")
    elif a<b:
        print(f"{a}>{b}")
        
    else:
        print('Los numeros son iguales')
elif operacion== 8:
    a= int(input("Ingrese un numero"))
    if a>0:
        print(a)
    else:
        print(-a)
    
