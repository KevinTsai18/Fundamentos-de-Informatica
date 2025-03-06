import random


#func cargar lista
def cargarlista():
    lista=[]
    for i in range(10):
        lista.append(random.randint(0,20))
    return lista


#func lista eliminacion
def eliminarlista(listaor,listasec):
    lista=[]
    j=0
    for i in range(len(listaor)):
        while j<len(listaor) and listasec[j]!=listaor[i]:
            j=j+1
        if j!=len(listaor):
            lista.append(listasec[j])
        j=0
    return lista



#func eliminar valores
def borrarvalores(listaor,listaelim):
    largoor=len(listaor)
    largoelim=len(listaelim)
    j=0
    i=0
    while j!=largoelim:
        while i<largoor and listaor[i]!=listaelim[j]:
            i=i+1
        del listaor[i]
        i=0
        j=j+1
    return listaor



#Prog ppal
listaor=cargarlista()
print(listaor)
listasec=cargarlista()
print(listasec)
listaelim=eliminarlista(listaor,listasec)
print(listaelim)
listafinal=borrarvalores(listaor,listaelim)
print(listafinal)