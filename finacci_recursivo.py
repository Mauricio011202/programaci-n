
def dar_suce_fibonacci(numero_parada,lista= [],num1= 0,num2=1,):
    lista.append(num1)
    if num2 > numero_parada:
        return lista
    return dar_suce_fibonacci(numero_parada,lista,num2,num1+num2)

