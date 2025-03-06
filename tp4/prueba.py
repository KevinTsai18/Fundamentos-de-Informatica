monto = int(input("Ingrese el monto de la compra: "))
cont15 = 0
cont20 = 0
monto15 = 0
monto20 = 0
montodesc = monto15 + monto20
montototal = 0
while monto > 0:
    if monto > 1000 and monto <= 2000:
        monto = monto * 0.85
        monto15 = monto15 + monto * 0.15
        cont15 = cont15 + 1
        montototal = montototal + monto
    if monto > 2000:
        monto = monto * 0.80
        monto20 = monto20 + monto * 0.20
        cont20 = cont20 + 1
        montototal = montototal + monto
    monto = int(input("Ingrese el monto de la compra: "))
montodesc = monto15 + monto20
print("Monto total a pagar: ", montototal)
print("Cantidad de compras con 15% de descuento: ", cont15)
print("Cantidad de compras con 20% de descuento: ", cont20)
print("Monto descontado (15%): ", monto15)
print("Monto descontado (20%): ", monto20)
print("Monto descontado total: ", montodesc)