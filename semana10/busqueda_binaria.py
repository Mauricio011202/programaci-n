
def main():
    lista= [6,5,3,1,7,2,4]
    number = int(input("please ingrese un numero"))
    if binaria_search(lista, number):
        print("EL numero")

    def binaria_search(lista, number):
        for n in lista:
            if n == number:
                return number
main()

