#Ejercicio 35: Se realizó una encuesta entre 100 consumidores.
#Por cada persona interrogada se ingresan dos valores:
#El primero indica la aceptación o no del producto A, mediante un 1 (acepta) o un 0 (no acepta).
#El segundo valor del par corresponde la producto B.
#or ejemplo, el par (1,0) señala que el encuestado acepta el producto A pero no el B.
#Se solicita informar el porcentaje de consumidores que aceptan:
#• El producto A. • El producto B. • El producto A solamente.
#• El producto B solamente. • Ninguno de los dos. • Ambos productos
c=0
pA=0
pB=0
soloA=0
soloB=0
ninguno=0
ambos=0
while c<10:
    A=int(input("Ingrese 1 si acepta el producto A, o, en caso contrario, 0:"))
    B=int(input("Ingrese 1 si acepta el producto B, o, en caso contrario, 0:"))
    c=c+1
    if A==1:
        pA=pA+1
    if B==1:
        pB=pB+1
    if A==1 and B!=1:
        soloA=soloA+1
    if B==1 and A!=1:
        soloB=soloB+1
    if A==1 and B==1:
        ambos=ambos+1
    if A!=1 and B!=1:
        ninguno=ninguno+1
print(pA)
print(pB)
print(soloA)
print(soloB)
print(ninguno)
print(ambos)
        