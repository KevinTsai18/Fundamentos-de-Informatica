"""Ejercicio 1: Escribir una función para ingresar desde el teclado una serie de números entre 1 y 20
y guardarlos en una lista.
En caso de ingresar un valor fuera de rango el programa mostrará un mensaje de error
y solicitará un nuevo número. Para finalizar la carga se deberá ingresar -1.
La función no recibe ningún parámetro, y devuelve la lista cargada
(o vacía, si el usuario no ingresó nada) como valor de retorno. """

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
lista_ej1=serie1_20()
print(lista_ej1)
            
        
            
    