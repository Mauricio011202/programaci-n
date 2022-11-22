
# Simulacro Parcial II

Utilizando Programación Orientada a Objetos, construya un programa que le permita al Saman Bar hacer el control y seguimiento de su inventario de bebidas, así como llevar un control de sus clientes y las cuentas que deberán pagar.

El bar posee multiples opciones de bebidas, los tragos que son bebidas alcohólicas y se caracterizan por el grado alcohólico; y las bebidas no alcohólicas se caracterizan por la temperatura en la que se beben; adicionalmente se conoce de las bebidas, su precio y su nombre.

De los clientes se conoce el nombre, la edad y su cedula de identidad.

Por mesa de servicio solamente se podrá tener un cliente quien será el que pague la cuenta de las bebidas adquiridas por dicha mesa.

El programa debe poder:

1. El programa deberá permitir el registro de nuevas bebidas (2 ptos)
2. El programa deberá permitir a un cliente realizar un o multiples compras (2 ptos)
3. Si la edad del cliente es menor a 18 años no deberá mostrarle las bebidas alcohólicas. (2 ptos)
4. Al cliente finalizar su comprar se le deberá mostrar la factura, la cual deberá contener (4 ptos):
   1. Los datos personales del cliente
   2. Los datos de cada bebida y la cantidad de bebidas compradas
   3. El total de la compra
   4. El descuento de acuerdo a los siguientes criterios:
      1. Si la edad del cliente pertenece a la sucesión de Fibonacci(\*) se le otorgara un 5%
      2. Si el total de la cuenta es un número primo se le otorga un 10%

El programa debe poder producir las siguiente estadísticas:

1. Cuanto debidas se vendieron por tipo (2 ptos)
2. Cuanto clientes compraron (2 ptos)
3. Cual es la bebida alcohólica y no alcohólica mas vendida (2 ptos)
4. Cual es el promedio de compra (2 ptos)

**(\*)**: Un número de la succión de Fibonacci es aquel que se define como la suma de los dos anteriores `a_n = a_{n-1} - a_{n-2}`, considerando que `a_0=0` y `a_1=1` **IMPORTANTE**: este algoritmo debe ser recursivo (2 ptos)

**Nota**: Deberá agregar al menos 3 productos iniciales con los que arranque la venta en el bar

1. Coca-Cola 2$
2. Cerveza 1.5$
3. Red Bull 3$
