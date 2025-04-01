#funcion año bisiesto
def bisiesto(año):
    if año%4==0 or año%400==0 and año%100!=0:
        bis=True
    else:
        bis=False
    return bis



#funcion calcular dias
def calculardias(d,m,a):
    esbis=bisiesto(a)
    maux=1
    daux=1
    diastotales=0
    if esbis==True:
        while maux!=m or daux!=d:
            daux=daux+1
            diastotales=diastotales+1
            if (maux==1 or maux==3 or maux==5 or maux==7 or maux==8 or maux==10 or maux==12) and daux>31:
                daux=1
                maux=maux+1
            elif (maux==4 or maux==6 or maux==9 or maux==11) and daux>30:
                daux=1
                maux=maux+1
            elif maux==2 and daux>29:
                daux=1
                maux=maux+1
    else:
        while maux!=m or daux!=d:
            daux=daux+1
            diastotales=diastotales+1
            if (maux==1 or maux==3 or maux==5 or maux==7 or maux==8 or maux==10 or maux==12) and daux>31:
                daux=1
                maux=maux+1
            elif (maux==4 or maux==6 or maux==9 or maux==11) and daux>30:
                daux=1
                maux=maux+1
            elif maux==2 and daux>28:
                daux=1
                maux=maux+1
    print("han transcurrido", diastotales, "dias desde el comienzo del año.")          



#prog ppal
DIA=int(input('Ingrese el dia de la fecha:'))
MES=int(input('Ingrese el mes de la fecha:'))
AÑO=int(input('Ingrese el año de la fecha:'))
calculardias(DIA,MES,AÑO)
