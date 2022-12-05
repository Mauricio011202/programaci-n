#=======================================================================
#Mauricio Mendez
#Carnet= 20221110100
#=======================================================================
numero= input('Ingrese un numero: ')
is_repunit=True
count=[]
while not numero.isnumeric():
    numero= input('Ingrese un numero (Solo numeros): ')
count= list(numero)
for i in count:
    if i!=count[0]:
            print(f"El numero {numero} no es repunit")
            is_repunit= False
if is_repunit== True:
        print(f"El numero {numero} es repunit ")