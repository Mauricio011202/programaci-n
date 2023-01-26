diccionario= {'numero': [1,2,3,4,5], 'letras':{'vocales':['a','e','i', ''],'consonates': ['aunfnunun']}}

for k,v in diccionario.items():
    if k == 'letras':
        for k2, v2 in v.items():
            if k2 == 'vocales':
                print(v2[2])