lista= 'bienvenidos a la prepa de algoritmos al'

count= 0
for i in lista:
    if i == 'a':
        if lista[count+1] == 'l':
            print(f'hay una al en el punto {count} y {count+1}')

    count+=1