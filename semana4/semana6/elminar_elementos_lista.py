lista=[[1,2],[3,4]]
for index in lista:
    for i in index:
        if i == 1:
            index.remove(i)
print(lista)