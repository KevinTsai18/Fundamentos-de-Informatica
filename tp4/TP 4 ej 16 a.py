#Ejercicio 16: Dadas las siguientes series numéricas, desarrollar programas que muestren los primeros 20 términos de cada una de ellas.
#a. 1, 1, 2, 3, 4, 9, 8, 27, 16… es decir 2**0, 3**0, 2**1, 3**1, 2**2, 3**2, 2**3, 3**3…
n=0
termino=0
while termino<20:
    print(2**n)
    termino=termino+1
    if termino<20:
        print(3**n)
    n=n+1
    termino=termino+1