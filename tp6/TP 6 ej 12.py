"""Ejercicio 12: Leer una lista de números V. Luego se solicita:


• Calcular el producto de los elementos de subíndice par
y dividirlo por la suma de los elementos de subíndice impar,
sólo si esta suma es distinta de cero.
Imprimir la lista leída y el resultado calculado, o un mensaje de error en caso de no poder realizar la operación.


• Generar e imprimir otra lista tal que su primer elemento contenga la suma del primero
más el último elemento de la lista V; el segundo elemento contenga la suma del segundo más el penúltimo de V, etc.
La nueva lista contendrá la mitad de los elementos de la lista original.


• Imprimir un listado de aquellos elementos de V que cumplan con la condición de tener iguales sus dos elementos laterales
(el anterior y el siguiente).
Si ninguno cumple esta condición, se imprimirá una leyenda aclaratoria.
Considerar que los extremos de la lista se encuentran unidos,
de modo que el último elemento se encuentra antes que el primero, y que el primer elemento se encuentra después del último."""

#Func. Lista
def cargarlista():
    lista=[]
    n=int(input("Ingrese un número para la lista:"))
    if n==-1:
        print("No se ingresaron datos")
    else:
        while n!=-1:
            lista.append(n)
            n=int(input("Ingrese un número para la lista:"))
    return lista

#Func productosubpar
def prodsubpar(largo,listap):
    prodtotal=1
    if largo%2!=0:
        for c in range(0,largo+1,2):
            prodtotal=prodtotal*listap[c]
    else:
        for c in range(0,largo,2):
            prodtotal=prodtotal*listap[c]
    return prodtotal

#Func sumasubimpar
def sumasubimpar(largo,listas):
    sumatotal=0
    if largo%2==0:
        for c in range(1,largo+1,2):
            sumatotal=sumatotal+listas[c]
    else:
        for c in range(1,largo,2):
            sumatotal=sumatotal+listas[c]
    return sumatotal

#Func nueva lista
def nuevovector(lista,largo):
    nuevalista=[]
    j=largo-1
    for i in range(0,largo//2):
        nuevalista.append(lista[i]+lista[j])
        j=j-1
    return nuevalista

#Func laterales iguales
def lateraligual(lista3,largoL):
    nuevolateral=[]
    if lista3[1]==lista3[largoL-1]:
        nuevolateral.append(lista3[0])
    for c in range(1,largoL-1):
        if lista3[c-1]==lista3[c+1]:
            nuevolateral.append(lista3[c])
    if lista3[largoL-2]==lista3[0]:
        nuevolateral.append(lista3[largoL-1])
    return nuevolateral



#Prog ppal
V=cargarlista()
print(V)
largoV=len(V)
producto=prodsubpar(largoV,V)
suma=sumasubimpar(largoV,V)
if suma==0:
    print("La suma no se puede realizar")
else:
    print("""El resultado de calcular el producto de los elementos de subíndice par y
dividirlo por la suma de los elementos de subíndice impar es""", producto/suma)
nuevaV=nuevovector(V,largoV)
print(nuevaV)
if suma!=0:
    listalateral=lateraligual(V,largoV)
    print(listalateral)
else:
    print("No se puede formar la lista")

