#Desarrollar un programa para leer las longitudes de los tres lados de un triángulo
#L1, L2, L3 y determinar qué tipo de triángulo es según la siguiente clasificación:
#· Si A >= B + C no se trata de un triángulo.
#· Si A² = B² + C² se trata de un triángulo rectángulo.
#· Si A² > B² + C² se trata de un triángulo obtusángulo.
#· Si A² < B² + C² se trata de un triángulo acutángulo.
#Tener en cuenta que A denota el mayor de los lados L1, L2 y L3, mientras que B
#y C corresponden a los dos lados restantes.
A=int(input("Ingrese un lado del triángulo:"))
B=int(input("Ingrese otro lado del triángulo:"))
C=int(input("Ingrese el tercer lado del triángulo:"))
if A>B and A>C:
    L1=A
    L2=B
    L3=C
elif B>A and B>C:
    L1=B
    L2=A
    L3=C
else:
    L1=C
    L2=A
    L3=B
if L1>=L2+L3:
    print("No se trata de un triángulo.")
elif L1**2==L2**2+L3**2:
    print("Se trata de un triángulo rectángulo.")
elif L1**2>L2**2+L3**2:
    print("Se trata de un triángulo obtusángulo.")
else:
    print("Se trata de un triángulo acutángulo.")
