"""Ejercicio 6: Ídem anterior, utilizando búsqueda binaria sobre una lista ordenada.
(Escribir una función para devolver la posición que ocupa un valor pasado como parámetro,
utilizando búsqueda secuencial en una lista desordenada.
La función debe devolver -1 si el elemento no se encuentra en la lista.)"""

#Func. Lista
def serie1_20():
    lista=[]
    n=int(input("Ingrese un número entre 1 y 20:"))
    if n==-1:
        print("No se ingresaron datos")
    else:
        while n!=-1:
            while n>20 or n<1:
                n=int(input("Error. Ingrese un número entre 1 y 20:"))
            lista.append(n)
            n=int(input("Ingrese un número entre 1 y 20:"))
    return lista


#Función met selecc
def metodoseleccion(v):
    largo=len(v)
    for i in range(largo-1):
        for j in range(i+1,largo):
            if v[i]>v[j]:
                aux=v[i]
                v[i]=v[j]
                v[j]=aux
    return v




#Func busq bin
def busquedabinaria(lista,dato):
    izq=0
    der=len(lista)-1
    pos=-1
    while izq<=der and pos==-1:
        centro=(izq+der)//2
        if lista[centro]==dato:
            pos=centro
        elif lista[centro]<dato:
            izq=centro+1
        else:
            der=centro-1
    return pos






#Prog ppal
milista=serie1_20()
print(milista)
milista=metodoseleccion(milista)
print(milista)
x=int(input("Ingrese el valor al que se le desea buscar su posición:"))
posfinal=busquedabinaria(milista,x)
if posfinal==-1:
    print("No se encuentra el valor en la lista")
else:
    print(x, "se encuentra en la posición", posfinal)



