import random

#funcion cargar lista
def cargarlista(N):
    lista=[]
    for i in range(N):
        lista.append(random.randint(0,20))
    print(lista)
    return lista

#funcion ordenar lista
def ordenarasc(v):
    for i in range(len(v)-1):
        for j in range(i+1,len(v)):
            if v[i]>v[j]:
                aux=v[i]
                v[i]=v[j]
                v[j]=aux
    print(v)
    return v
#funcion busqueda binaria
def busqbin(v,n):
    izq=0
    der=len(v)-1
    pos=-1
    while izq<=der and pos==-1:
        centro=(izq+der)//2
        if v[centro]==n:
            pos=centro
        elif v[centro]<n:
            izq=centro+1
        else:
            der=centro-1
    return pos
#funcion eliminar nro
def eliminarnro(v):
    i=0
    while i!=len(v)-1:
        if v[i]==v[i+1]:
            del v[i]
        else:
            i=i+1
    print(v)
    return v



def imprimirlista(v):
    for i in range(len(v)):
        print(v[i],end=" ")



#prog ppal
N=int(input('Ingrese un numero:'))
lista=cargarlista(N)
lista=ordenarasc(lista)
M=int(input('Ingrese otro numero para buscarlo en la lista:'))
posicion=busqbin(lista,M)
if posicion==-1:
    print('No se encontro el nro.')
else:
    print('el nro se encuentra en el subindice', posicion)
lista=eliminarnro(lista)
#print(lista)
imprimirlista(lista)