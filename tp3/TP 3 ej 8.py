#Ejercicio 8: Una empresa factura a sus clientes el último día de cada mes. Si el cliente paga
#su factura dentro de los primeros 10 días del mes siguiente, tiene un descuento
#de $120 o del 2% de la factura, lo que resulte menor. Si paga en los siguientes
#10 días del mes deberá pagar el importe original de la factura, mientras que si
#paga después del día 20 deberá abonar una multa de $150 o del 10% de su factura, lo que resulte mayor. Desarrolle un programa que lea el número del cliente
#y el total de la factura, y emita un informe donde conste el número del cliente y
#los tres importes que podrá abonar según la fecha de pago.

cliente=input("Ingrese su número de cliente:")
factura=int(input("Ingrese el total de la factura:"))
print("Su número de cliente:", cliente)
if factura-(factura/50)<factura-120:
    monto1=factura-(factura/50)
else:
    monto1=factura-120
print("Si paga la factura dentro de los primero 10 días del mes, su importe será de $", monto1)
print("Si paga en los siguientes 10 días del mes deberá pagar $", factura)
if factura+(factura/10)>factura+150:
    monto2=factura+(factura/10)
else:
    monto2=factura+150
print("Y si paga la factura después del día 20, su importe será de $", monto2)
#Si monto<120?
