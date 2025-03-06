#Ejercicio 16: Dadas las siguientes series numéricas, desarrollar programas que muestren los primeros 20 términos de cada una de ellas.
#b.-1, 2, -3, 4, -5, 6, -7…  es decir 1*(-1)**1, 2*(-1)**2, 3*(-1)**3, 4*(-1)**4, 5*(-1)**5, 6*(-1)**6, 7*(-1)**7…
n=1
termino=0
while termino<20:
    print(n*(-1)**n)
    n=n+1
    termino=termino+1