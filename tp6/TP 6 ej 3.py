"""Ejercicio 3: Determinar si una lista es capicúa (EJ1)."""


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
lista_ej3=serie1_20()
print(lista_ej3)
largo=len(lista_ej3)
largo=largo-1
for c in range(largo):
    if lista_ej3[c]==lista_ej3[largo]:
        capic=True
        largo=largo-1
    else:
        capic=False
if capic==True:
    print("Es capicua")
else:
    print("No es capicua")