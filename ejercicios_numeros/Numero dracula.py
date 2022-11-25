n= input('Ingrese un numero: ')

while not n.isnumeric() and len(n)<4:
    print('Ha ingresado un numero incorrecto')
    n=input ('Ingrese un numero: ')
else:
    for i in range(1,int(n)):
        for j in range(1,int(n)):
            i=int(i)
            j=int(j)
            n=int(n)
            if i*j==n and len(j)==len(i) and (j[0]==0 and i[0]!=0) or 