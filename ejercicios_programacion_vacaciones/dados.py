combinaciones = []

num1 = input('Ingree un numero entre 2 y 12: ')
while int(num1) not in range (2,13):
    num1 = input('Ingree un numeroentre 2 y 12: ')
num1 = int(num1)

for x in range(1,7):
    
    for y in range(1,7):
        
        if (x+y == num1):
            
            if sorted([x,y]) in combinaciones:
  
                continue
            else:
          
                combinaciones.append([x,y])


print(f"Combinaciones para {num1}:")
for i,combinacion in enumerate(combinaciones):
    print(f"\t* {combinacion[0]}-{combinacion[1]}")
    