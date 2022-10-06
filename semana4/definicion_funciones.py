#la variable vive solodentro del def
def simple_fun():
    msg="Mensaje"
#print(msg) no existe
#labeled argment, permite colocar un tercer parametropredeterminado se escriben de la forma base=2

def area_rectangulo(base=1,height=10):
    return base*height
#Si no colocamos un return va a devolver  none camos  y se puede almacenar en una variable.
