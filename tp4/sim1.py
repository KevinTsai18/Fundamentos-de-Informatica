#Simulacro 1
cant=0
legajo=0
nota=0
promedio=0
al7_10=0
al4_7=0
al1_3=0
legajo=int(input("Ingrese el número de legajo:"))
while legajo!=-1:
    nota=int(input("Ingrese la nota:"))
    while nota<1 or nota>10:
        nota=int(input("Nota inválida.Ingrese otra nota:"))
    if 10>=nota>=7:
        al7_10=al7_10+1
        promedio=promedio+nota
        cant=cant+1
    elif 7>nota>=4:
        al4_7=al4_7+1
        cant=cant+1
    else:
        al1_3=al1_3+1
        cant=cant+1
    legajo=int(input("Ingrese el número de legajo:"))
if cant!=0:
    print(al7_10)
    print(al4_7)
    print(al1_3/cant*100)
    print(cant)
    print(al1_3)
    print(promedio/al7_10)