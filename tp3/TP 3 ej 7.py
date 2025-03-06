#Ejercicio 7: Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
#Aplica el precio base a la primera docena de unidades.
#Aplica un 10% de descuento a todas las unidades entre 13 y 100.
#Aplica un 25% de descuento a todas las unidades por encima de las 100.
#Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio
#base es 100. El cálculo resultante sería:
#100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04
#Desarrollar un programa que lea la cantidad solicitada de un producto y su precio base, e imprima el valor total de la venta y el precio promedio.
cantidad=int(input("Ingrese la cantidad del producto:"))
precio=float(input("Ingrese el precio del producto:"))
precio90=precio*9/10
precio75=precio*3/4
if cantidad<=12:
    print("Valor total:$", cantidad*precio)
    print("Precio promedio:$", cantidad*precio/cantidad)
elif 12<cantidad<100:
    print("Valor total:$", 12*precio+(cantidad-12)*precio90)
    print("Precio promedio:$", (12*precio+(cantidad-12)*precio90)/cantidad)
else:
    print("Valor total:$", 12*precio+88*precio90+(cantidad-100)*precio75)
    print("Precio promedio:$", (12*precio+88*precio90+(cantidad-100)*precio75)/cantidad)
