n=int(input("Ingrese un número positivo:"))
while n<0:
    n=int(input("Número inválido.Ingrese un número positivo:"))
nec=0
while nec*(nec+1)<=n:
    ob=nec*(nec+1)
    nec=nec+1
if ob==n:
    print(n, "es oblongo")
else:
    print(n, "no es oblongo")
primo=1
divisores=0
while primo<=n:
    if n%primo==0:
        divisores=divisores+1
    primo=primo+1
if divisores<=2:
    print(n, "es primo")
else:
    print(n, "no es primo")