option= int(input("Por favor eliga una opcion valida: \n1- Vegetariana \n2-No vegetariana-> "))
is_valid= True


if option== 1:
    ingredientes= int(input("Eliga el ingrediente que desea: \n1-Pimiento \n2-Tofu ->"))
    if ingredientes== 1:
        ingredientes= 'Pimiento'
    elif ingredientes== 2:
        ingredientes= 'Tofu'
    print(f'La pizza es vegetariana y sus ingredientes son mozarella, tomate y {ingredientes}')
    

elif option== 2:
    ingredientes= int(input("Eliga el ingrediente que desea: \n1-Peperoni \n2-Jamon \n 3-Salmon -> "))
    if ingredientes== 1:
        ingredientes= 'Peperoni'
    elif ingredientes== 2:
        ingredientes= 'Jamon'
    else:
        ingredientes= 'Salmon'
        print(f'La pizza no es vegetariana y sus ingredientes son mozarella, tomate y {ingredientes}')
else:
    print('Ingrese un caracter valido')
