#16
#c. 1, 2, 4, 7, 11, 16, 22, 29… es decir 1, (1+1), (2+2), (4+3), (7+4), (11+5), (16+6), (22+7)…
#(el primer término es 1 y cada nuevo término se obtiene sumando el término anterior más el número de orden del término actual)
n=1
termino=0
while termino<20:
    print(n+termino)
    n=n+termino
    termino=termino+1
    
    