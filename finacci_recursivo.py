def dar_suce_fibonacci(numero_parada,num1= 0,num2=1):
    print(num1, end= " ")
    if num2 > numero_parada:
        return num2
    return dar_suce_fibonacci(numero_parada,num2,num1+num2)

print(dar_suce_fibonacci(21))