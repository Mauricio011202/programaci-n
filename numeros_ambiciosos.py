def ambicious_number():
     divisores_a=[]
    
     num_a=int(input("Ingrese un número para verificar si es ambicioso: "))
     for j in range(1,num_a):
         if num_a%j==0:
             divisores_a.append(num_a//j)
     print(divisores_a)
ambicious_number()