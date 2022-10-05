a= [1, 2, 3]
b= [-1, 0, 2]
acumulador= 0

for index in range(len(a)):
    acumulador+= (a[index]*b[index])

print("resultado", acumulador)