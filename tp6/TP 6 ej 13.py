"""Ejercicio 13: Realizar un programa que permita ingresar números en una lista,
finalizando la lectura con -1.
Informar si la secuencia de elementos ingresada es ascendente, descendente,
todos sus valores son iguales o se encuentra desordenada."""

#func cargar lista
def cargarlista():
    lista=[]
    n=int(input("Ingrese un numero para la lista:" ))
    if n==-1:
        print("No se ingresaron datos")
    else:
        while n!=-1:
            lista.append(n)
            print(lista)
            n=int(input("Ingrese un numero para la lista:" ))
    return lista





#func orden igual
def ordenigual(v):
    for i in range(len(v)-1):
        if v[i]==v[i+1]:
            igual=True
        else:
            igual=False
    return igual

###PARA ASCENDENTE Y DESCENDENTE



#func ordasc
def ordenasc(v):
    vasc=[]
    largov=len(v)
    for h in range(largov):
        vasc.append(v[h])
    for i in range(largov-1):
        for j in range(i+1,largov):
            if vasc[j]<vasc[i]:
                aux=vasc[j]
                vasc[j]=vasc[i]
                vasc[i]=aux
    print(vasc)
    for k in range(largov):
        if v[k]==vasc[k]:
            ascendente=True
        else:
            ascendente=False
    return ascendente




#func orddesc
def ordendesc(v):
    vdesc=[]
    largov=len(v)
    for h in range(largov):
        vdesc.append(v[h])
    for i in range(largov-1):
        for j in range(i+1,largov):
            if vdesc[j]>vdesc[i]:
                aux=vdesc[j]
                vdesc[j]=vdesc[i]
                vdesc[i]=aux
    print(vdesc)
    for k in range(largov):
        if v[k]==vdesc[k]:
            descendente=True
        else:
            descendente=False
    return descendente



#prog ppal
listappal=cargarlista()
print(listappal)
listaigual=ordenigual(listappal)
if listaigual==True:
    print("Los valores de la secuencia son iguales.")
else:
    listaasc=ordenasc(listappal)
    listadesc=ordendesc(listappal)
    if listaasc==True:
        print("La secuencia ingresada es ascendente.")
    elif listadesc==True:
        print("La secuencia ingresada es descendente.")
    else:
        print("La secuencia está desordenada.")



