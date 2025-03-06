d=int(input("Ingrese el dia de la fecha:"))
m=int(input("Ingrese el mes de la fecha:"))
a=int(input("Ingrese el año de la fecha:"))
n=int(input("Ingrese una cantidad de dias:"))
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10:
    if d+n<=31:
        print(d+n, "/", m, "/", a)
    else:
        print(d+n-31, "/", m+1, "/", a)
elif m==4 or m==6 or m==9 or m==11:
    if d+n<=30:
        print(d+n, "/", m, "/", a)
    else:
        print(d+n-30, "/", m+1, "/", a)
elif m==2:
    if a%4==0 and a%100!=0 or a%400==0:
        if d+n<=29:
            print(d+n, "/", m, "/", a)
        else:
            print(d+n-29, "/", m+1, "/", a)
    else:
        if d+n<=28:
            print(d+n, "/", m, "/", a)
        else:
            print(d+n-28, "/", m+1, "/", a)
elif m==12:
    if d+n<=31:
        print(d+n, "/", m, "/", a)
    else:
        print(d+n-31, "/", m-11, "/", a+1)