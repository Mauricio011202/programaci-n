def producto_primos(n):
    '''
    Función para verificar si un número es el producto de dos números primos.

    Argumentos => 'n': número ingresado por teclado.

    Retorna => impresión de la respuesta.

    '''

    # listas para guardar los números que irán ayudando a llegar a la respuesta y variable booleana que condicionará el output
    divisores = []
    primos = []
    producto = False

    # se buscan los divisores de n y se guardan en la lista correspondiente
    for x in range(2,n):
        if n%x == 0:
            divisores.append(x)


    # se recorre la lista de divisores comenzando cada iteración con la variable booleana primo en True. Con otro for loop se divide d entre un rango de números para ver si es un número primo o no. La variable primo cambia de True a False si d es divisible entre w, haciendo que al llegar al condicional para agregar a d a los primos, solo se ejecute si primo es verdadero
    for d in divisores:
        primo = True
        for w in range(2,d):
            if d%w == 0:
                primo = False
                break
        if primo:
            primos.append(d)


    # se buscan entre los números de la lista de primos dos números cuyo producto sea igual al número ingresado por teclado. EL valor de verdad de la variable 'producto' ayuda a detener el loop si ya se comprobó que n = p*q
    for p in primos:
        for q in primos:
            if n == p*q:
                producto = True
                print(f"{n} es producto de los primos {p} y {q}.")
                break
        if producto: break
                
    # si producto nunca cambió su valor a True, eso significa que n no es un producto de primos y se notifica en pantalla
    if not producto:
        print(f"{n} no es un producto de primos.")





def main():
    # validación para asegurar que n cumpla con las condiciones de ejecución del programa
    try:
        n = int(input("Ingrese un número entero: "))
        # se ejecuta la función
        producto_primos(n)
    except:
        print("Ingreso inválido, intente de nuevo.")

# se ejecuta el main
main()

    


