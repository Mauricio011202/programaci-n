from Trabajador import *

def main():
    honorarios_ing= 25
    honorarios_arq=10
    honorarios_obr=5

    ingenieros=[]
    arquitectos=[]
    obreros=[]
    empleados_totales=[]
    recargo_primo=5/100
    recargo_deficiente=10/100
    recargo_factorial=15/100
    
    montos_pagados=[]
    montos_pagados_ing=[]
    montos_pagados_arq=[]
    montos_pagados_obr=[]


    print('***BIENVENIDO***')
    nombre=input('Escriba el nombre: ')
    apellido= input('Escriba el apellido: ')
    cedula= input('Introduzca la cedula:')
    tipo_trabajador=input('Seleccione:\n 1-Ingeniero\n2-Arquitecto\n3-Obrero\n==>')
    horas_trabajadas=input('Escriba la horas trabajadas:')
    mes= input('Escriba el mes :')
    if tipo_trabajador=='1':
        especialidad= input('Seleccione el tipo de especialidad:\n1-Civil\n2-Electrica\n==>')
        if especialidad=='1':
            especialidad_escogida='Civil'
        else:
            especialidad_escogida='Electricista'
    elif tipo_trabajador=='2':
        especialidad= input('Seleccione el tipo de especialidad:\n1-Exterior\n2-Interior\n==>')
        if especialidad=='1':
            especialidad_escogida='Exterior'
        else:
            especialidad_escogida='Interior'
    elif tipo_trabajador=='3':
        especialidad=input('Seleccione la especialidad:\n1-Capataz\n2-Novato\n==>')
        if especialidad=='1':
            especialidad_escogida='Capataz'
        else:
            especialidad_escogida='Novato'
        
    trabajador= Trabajador(nombre,apellido,cedula,tipo_trabajador,horas_trabajadas,mes,especialidad_escogida)
    trabajador_generado=trabajador.empleado()
    horas_trabajadas=int(horas_trabajadas)
    if tipo_trabajador=='1':
        ingenieros.append(trabajador_generado)
        empleados_totales.append(trabajador_generado)
        monto_a_pagar=horas_trabajadas*honorarios_ing
        primo= True
        for n in range(2,horas_trabajadas):
            if horas_trabajadas % n == 0:
                primo= False
        if primo==True:
            recargo= monto_a_pagar*recargo_primo
            monto_a_pagar=monto_a_pagar+recargo
        lista_divisores=[]
        n=horas_trabajadas
        while n>1:
            for e in range(2,n):
                if n%e==0:
                    lista_divisores.append(e)
            break
        suma=sum(lista_divisores)
        if suma<int(horas_trabajadas):
            recargo=monto_a_pagar*recargo_deficiente
            monto_a_pagar=monto_a_pagar+recargo
        montos_pagados_ing.append(monto_a_pagar)
        montos_pagados.append(monto_a_pagar)
        

    elif tipo_trabajador=='2':
        arquitectos.append(trabajador_generado)
        empleados_totales.append(trabajador_generado)
        monto_a_pagar=horas_trabajadas*honorarios_arq
        primo= True
        for n in range(2, horas_trabajadas):
            if horas_trabajadas % n == 0:
                primo= False
        if primo==True:
            recargo= monto_a_pagar*recargo_primo
            monto_a_pagar=monto_a_pagar+recargo
        lista_divisores=[]
        n=horas_trabajadas
        while n>1:
            for e in range(2,n):
                if n%e==0:
                    lista_divisores.append(e)
            break
        suma=sum(lista_divisores)
        if suma<horas_trabajadas:
            recargo=monto_a_pagar*recargo_deficiente
            monto_a_pagar=monto_a_pagar+recargo
        montos_pagados_arq.append(monto_a_pagar)
        montos_pagados.append(monto_a_pagar)

    elif tipo_trabajador=='3':
        obreros.append(trabajador_generado)
        empleados_totales.append(trabajador_generado)
        monto_a_pagar=horas_trabajadas*honorarios_obr
        primo= True
        for n in range(2, horas_trabajadas):
            if horas_trabajadas % n == 0:
                primo= False
        if primo==True:
            recargo= monto_a_pagar*recargo_primo
            monto_a_pagar=monto_a_pagar+recargo
        lista_divisores=[]
        n=horas_trabajadas
        while n>1:
            for e in range(2,n):
                if n%e==0:
                    lista_divisores.append(e)
            break
        suma=sum(lista_divisores)
        if suma<horas_trabajadas:
            recargo=monto_a_pagar*recargo_deficiente
            monto_a_pagar=monto_a_pagar+recargo
        
        montos_pagados_obr.append(monto_a_pagar)
        montos_pagados.append(monto_a_pagar)

    monto_final_dia= sum(montos_pagados)
    cantidad_ingenieros= len(ingenieros)
    cantidad_arq= len(arquitectos)
    cantidad_obr=len(obreros)
    print(f'El monto total pagado {monto_final_dia}')
    print(f'La cantidad empleados ingenieros {cantidad_ingenieros}')
    print(f'La cantidad de empleados arquitectos {cantidad_arq}')
    print(f'La cantidad de empleados obreros: {cantidad_obr}')
    promedio_ingenieros= sum(montos_pagados_ing)
    if ingenieros!=[]:
        promedio_ingenieros= promedio_ingenieros/len(ingenieros)
        ing_mejor_pagado=max(montos_pagados_ing)
        ing_m=montos_pagados_ing.index(ing_mejor_pagado)
        ing_mp=ingenieros[ing_m]

        aux=ing_mp.split('//')

    else:
        promedio_ingenieros=0
        ing_mp='No hubo'
    promedio_arq= sum(montos_pagados_arq)
    if arquitectos!=[]:
        promedio_arq= promedio_arq/len(arquitectos)
        arq_mejor_pagado=max(montos_pagados_arq)
        arq_m=montos_pagados_arq.index(arq_mejor_pagado)
        arq_mp=ingenieros[arq_m]

        aux1=arq_mp.split('//')
    else:
        promedio_arq=0
        arq_mp='No hubo'
    promedio_obr= sum(montos_pagados_obr)

    if obreros!=[]:
        promedio_obr= promedio_obr/len(obreros)
        obr_mejor_pagado=max(montos_pagados_obr)
        obr_m=montos_pagados_obr.index(obr_mejor_pagado)
        obr_mp=ingenieros[obr_m]

        aux2=obr_mp.split('//')

    else:
        promedio_obr=0
        obr_mp='No hubo'

    print(f'El promedio de pago de los ingenieros es {promedio_ingenieros}')
    print(f'El promedio de pago de los arquitectos  es {promedio_arq}')
    print(f'El promedio de pago de los obreros es {promedio_obr}')

    if ingenieros!=[]:
        print(f'El ingeniero mejor pagado fue: {aux[0]} {aux[1]} ') 
    if arquitectos!=[]:   
        print(f'El arquitecto mejor pagado fue: {aux1[0]} {aux1[1]} ')    
    if obreros!=[]:
        print(f'El obrero mejor pagado fue: {aux2[0]} {aux2[1]}')    

    

main()


