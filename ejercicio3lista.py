num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
impar=0
suma=0
total= 0
for i in range(0, len(num_list)-1):
    while (num_list[i] %2 != 0) and (impar < 5):
        suma +=num_list[i]
        impar += 1
        total +=1
        
