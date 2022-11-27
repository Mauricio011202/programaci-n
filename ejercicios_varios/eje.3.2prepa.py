x = "Outside of that, Hu argues that the royalties can be more reliable than the entropy of Wall Street. No matter what happens to the stock market, people are always going to be listening to music."
y = "CBD, which comes from either a marijuana or hemp plant, is non-psychoactive, so it won’t get you high like THC (tetrayhydrocannabinol). It may, however, offer anti-inflammatory, antioxidant, anti-psychotic, anti-convulsant, and antidepressant properties. Because it can hemp is legal in all 50 states, hemp-derived CBD products are becoming more readily available online and in stores all over the country."
z = "According to a report published by Fast Company, apparel sales have plummeted by 50 percent. It’s a margin that will be difficult to recover from, especially for small businesses that don’t have the backing of major conglomerates. These independent companies rely on seasonal buys from retailers to stay afloat. But with the bevy of store closures and restrictions on online sales, these behemoth retailers are facing hard times of their own."

contador_x= 0
index_x= ""
for i in range(len(x)):
    if x[i]== 'a'and x[i+1]== 't':
     contador_x+= 1
     index_x+= f" {i};{i+1}"
print(F"Indice en x {index_x}")
print(f"Numero de at en x es {contador_x}")

contador_y= 0
indice_y= ""
for i in range(len(y)):
    if y[i]== 'o'and y[i+1]== 'm':
     contador_y+= 1
     indice_y+= f"{i};{i+1}"
print(f"Numero de om en y es {contador_y}")
print(f"El indice en y es {indice_y}")
contador_z= 0
indice_z= ""

for i in range(len(z)):
    if z[i]== 'i' and z[i+1]=='n':
        contador_z+= 1
        indice_z+= f" {i}; {i+1} "
print(f"El numero de in en z es {contador_z}")
print(f"los idices en z son {indice_z}")
