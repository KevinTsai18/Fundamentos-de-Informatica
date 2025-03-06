"""Ejercicio 17: Modificar el programa anterior para que las pistas brindadas por el programa
no sean del tipo "es mayor" o "es menor" sino "M dígitos correctos y N dígitos aproximados".
Se considera que un dígito es correcto cuando tanto su valor como su posición coinciden con los del número secreto,
mientras que un dígito es aproximado cuando coincide el valor pero no su posición.
Ejemplos:
Número secreto: 5739
• Intento 1: 1234 -> 1 correcto
• Intento 2: 5678 -> 1 correcto y 1 aproximado
• Intento 3: 9375 -> 4 aproximados"""
import random


#Funcion ver si hay correctos
def haycorrectos(ns,ni):
    c=0
    while ns//10!=0:
        if ns%10==ni%10:
            c=c+1
        ns=ns//10
        ni=ni//10
    if ns==ni:
        c=c+1
    return(c)
        
    
#funcion ver si hay aproximados
def hayaproximados(ns,ni):
    a=0
    vns=[]
    vni=[]
    while ns//10!=0:
        vns.append(ns%10)
        ns=ns//10
    vns.append(ns)
    while ni//10!=0:
        vni.append(ni%10)
        ni=ni//10
    vni.append(ni)
    for i in range(len(vns)):
        for j in range(len(vni)):
            if vns[i]==vni[j]:
                a=a+1
        j=j+1
    return a

            





#Func checkear numero con secreto
def checknum(secreto,ingreso):
    correctos=haycorrectos(secreto,ingreso)
    aproximados=hayaproximados(secreto,ingreso)
    print("Hay", correctos, "numeros correctos y", aproximados-correctos, "aproximados.")


#Func juego
def funcjuego(cantpunt,intentos,puntos,n,listanombre):
    while n!=-1:
        n=int(input("Ingrese el número que cree que es:"))
        NS=random.randint(1000,9999)
        print(NS)
        while n!=NS and n!=-1:    
            checknum(NS,n)
            n=int(input("Ingrese el número que cree que es:"))
            while n<-1 or n>9999:
                n=int(input("NUMERO INVALIDO!!! Ingrese otro numero:"))
            intentos=intentos+1
        if n==NS:
            print("Número encontrado!")
            cantpunt.append(intentos)
            nombre=input("Ingrese su nombre")
            listanombre.append(nombre)
        puntos=intentos
        intentos=0
    if n==-1:
        print("Fin del juego")
    largo=len(cantpunt)
    if largo<=1:
        print(cantpunt)
        print(listanombre)
    else:
        for i in range(largo-1):
            for j in range(i+1,largo):
                if cantpunt[i]>cantpunt[j]:
                    auxpunt=cantpunt[i]
                    auxnom=listanombre[i]
                    cantpunt[i]=cantpunt[j]
                    listanombre[i]=listanombre[j]
                    cantpunt[j]=auxpunt
                    listanombre[j]=auxnom
        print(cantpunt)
        print(listanombre)
        if largo>5:
            listadef=[]
            nombredef=[]
            for k in range(5):
                listadef.append(cantpunt[k])
                nombredef.append(listanombre[k])
            print(listadef)
            print(nombredef)
    continuar()




#Funcion continue
def continuar():
    print("Desea seguir jugando?")
    resp=input()
    if resp=="si":
        cantpunt=[]
        intentos=0
        puntos=0
        n=0
        listanombre=[]
        funcjuego(cantpunt,intentos,puntos,n,listanombre)
    else:
        print("Fin del juego")



#Prog ppal
cantpunt=[]
intentos=0
puntos=0
n=0
listanombre=[]
funcjuego(cantpunt,intentos,puntos,n,listanombre)