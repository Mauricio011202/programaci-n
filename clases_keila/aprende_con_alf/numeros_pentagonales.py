numero= int(input('Ingrese la cantidad de numeros pentagonales que desee ver: '))
pentagonales= []
for i in range(1,numero):
        num= i*((3*i)-1)
        deno= 2
        penta= num/deno
        pentagonales.append(int(penta))
print(pentagonales)