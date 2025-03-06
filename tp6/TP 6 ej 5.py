"""Ejercicio 5: Escribir una función para devolver la posición que ocupa un valor pasado como parámetro,
utilizando búsqueda secuencial en una lista desordenada.
La función debe devolver -1 si el elemento no se encuentra en la lista."""


#Preguntar por valores repetidos

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

#Func Posición
def posicionar(a,lista_pos):
    largo=len(lista_pos)
    posfinal=-1
    flag=True
    for c in range(largo):
        if lista_pos[c]==a and flag==True:
            posfinal=c
            flag=False
    return posfinal



#Prog ppal
lista_ej5=serie1_20()
v=int(input("Ingrese el valor al que se le desea buscar su posición:"))
posppal=posicionar(v,lista_ej5)
print(posppal)


