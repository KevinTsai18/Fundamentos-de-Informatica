"""Ejercicio 2: Calcular la suma de los números de una lista (EJ1)."""
#Func
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



#Prog ppal.
suma=0
lista_ej2=serie1_20()
print(lista_ej2)
largo=len(lista_ej2)
for term in range(largo):
    suma=suma+lista_ej2[term]
print(suma)