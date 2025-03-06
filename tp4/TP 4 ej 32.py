#Ejercicio 32: La sucesión de Fibonacci es una sucesión de números enteros
#donde cada término se obtiene como suma de los dos anteriores,
#siendo los dos primeros 1 y 1. Por lo tanto, Fib=1, 1, 2, 3, 5, 8, 13, 21....
#Realizar un programa que lea N e imprima los N primeros términos de esta sucesión, como así también la suma de los mismos.
N=int(input("Ingrese un número:"))
num1=1
num2=1
cant=2
suma=2
if N==1:
    print(num1)
elif N==2:
    print(num1)
    print(num2)
else:
    print(num1)
    print(num2)
    while cant<N:
        num3=num1+num2
        print(num3)
        num1=num2
        num2=num3
        cant=cant+1
        suma=suma+num3
print("La suma de los terminos es", suma)
    