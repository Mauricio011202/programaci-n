


numero= input("Ingrese un numero:  ")
count=[]
is_repunit=True
suma= 0
while not numero.isnumeric():
    numero= input("Ingrese un numero valido: ")
count= list(numero)
for i in count:
    if i != i[0]:
        print("El numero no es repunit")
        is_repunit= False
if is_repunit == True:
    print("El Numero es repunit")
    for s in numero:
        suma+= int(s)
        
        
