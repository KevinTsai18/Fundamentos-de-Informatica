#Ejercicio 5: Desarrollar un programa para leer la base y la altura de un triángulo e imprimir
#su superficie. El algoritmo debe validar los datos de entrada, verificando que
#éstos sean números positivos. En caso contrario debe imprimirse el dato erróneo
#junto con una leyenda aclaratoria. Se recuerda que Sup = (Base * Altura) / 2.

B=float(input("Ingrese la medida de la base del triángulo:"))
H=float(input("Ingrese la medida de la altura del triángulo:"))
if B<=0:
    print(B, "es una medida inválida")
elif H<=0:
    print(H, "es una medida inválida")
elif B<=0 and H<=0:
    print(B, "y", H, "son medidas inválidas")
else:
    print("Su superficie es:", (B*H)/2)
