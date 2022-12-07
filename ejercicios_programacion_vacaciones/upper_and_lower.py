
palabra= input('Ingree una palabra: \n=>')
palabra= palabra.split(' ')
 
while not palabra.isalpha():
    palabra= input('ERROR! Ingree una palabra: \n=>')

for i in palabra.lower():
    if i == 'a':
        palabra= palabra.replace('a', 'A')
    elif i == 'e':
        palabra= palabra.replace('e', 'E')
    elif i == 'i':
        palabra= palabra.replace('i', 'I')
    elif i == 'o':
        palabra= palabra.replace('o', 'O')
    elif i == 'u':
        palabra= palabra.replace('u', 'U')
print(palabra)
    
       