#Ejercicio 12: Leer tres números correspondientes al día, mes y año de una fecha e imprimir
#un mensaje indicando si la fecha es válida o no.
día=int(input("Ingrese el número del día de la fecha:"))
mes=int(input("Ingrese el número del mes de la fecha:"))
año=int(input("Ingrese el año de la fecha:"))
if año<0:
    print("La fecha es inválida")
elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    if 0<día<=31:
        print("La fecha es válida")
    else:
        print("La fecha es inválida")
elif mes==4 or mes==6 or mes==9 or mes==11:
    if 0<día<=30:
        print("La fecha es válida")
    else:
        print("La fecha es inválida")

elif mes==2:
    if año%4==0 and año%100!=0 or año%400==0:
        if día<=29:
            print("La fecha es válida")
        else:
            print("La fecha es inválida")
    else:
        if día<=28:
            print("La fecha es válida")
        else:
            print("La fecha es inválida")
else:
    print("La fecha es inválida")