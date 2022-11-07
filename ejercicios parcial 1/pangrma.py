#Dada una oración, escriba un programa Python para verificar si esa oración es un
#pangrama o no. Un pangrama es una oración que contiene todas las letras del alfabeto inglés.

from string import ascii_lowercase
def pangrama(frase):
    alfabeto= set(ascii_lowercase)
    return alfabeto <= set(frase.lower())
letras_en_la_frase= {}
def contador_de_letras(frase):
    for letra in frase:
        if letra in letras_en_la_frase:
            letras_en_la_frase[letra]= letras_en_la_frase[letra]+1
        else:
            letras_en_la_frase[letra]= 1
    return letras_en_la_frase
def main():
    frase= input("Ingrese una frase: ")
    print("La frase es pangrama:")
    print(pangrama(frase))
    letras_en_la_frase =contador_de_letras(frase)
    for k,v in letras_en_la_frase.items():
        print(f'letra:{k}, cantidad: {v}')


main()