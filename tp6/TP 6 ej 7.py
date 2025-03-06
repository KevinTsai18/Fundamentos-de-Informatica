"""Ejercicio 7: Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del año,
con el propósito de ofrecerles un agasajo especial en su día.
Desarrollar un programa que lea el número de legajo y fecha de nacimiento
(día, mes y año) de cada uno de los alumnos que concurren a dicha escuela.
La carga finaliza con un número de legajo igual a -1.
Emitir un informe donde aparezca -mes por mes- cuántos alumnos cumplen años a lo largo del año.
Imprimir también una leyenda que indique cuál es el mes con mayor cantidad de cumpleaños."""

#func alumnos
def funcalumnos():
    cumpleaños=crearlistacumple()
    legajo=int(input("Ingrese el número de legajo:"))
    if legajo==-1:
        print("No se ingresaron datos.")
    else:
        while legajo!=-1:
            mes=int(input("Ingrese el mes de nacimiento: "))
            while mes<0 or mes>13:
                mes=int(input("MES INVÁLIDO. Ingrese el mes de nacimiento: "))
            cumpleaños[mes]=cumpleaños[mes]+1
            print(cumpleaños)
            legajo=int(input("Ingrese el número de legajo:"))
    return cumpleaños



#Funcion lista cumple
def crearlistacumple():
    MESES=12
    listac=[]
    for i in range(MESES+1):
        listac.append(0)
    print(listac)
    return listac

    


#Prog ppal.
cumplealumnos=funcalumnos()
for j in range(1,13):
    print("En el mes", j, "hay", cumplealumnos[j],"cumpleaños")
mayor=1
for k in range(2,13):
    if cumplealumnos[k]>cumplealumnos[mayor]:
        mayor=k
print("El mes con mas cumpleaños es el mes", mayor)