def perfect_num():
    divisores_perfe=[]
    num=input("Ingrese un número para verificar si es perfecto: ")
    num=int(num)
    for i in range(1,num):
        if num%i==0:
            divisores_perfe.append(i)
    if sum(divisores_perfe)==num:
        print("Es perfecto")
    else:
        print("No es perfecto")
perfect_num()