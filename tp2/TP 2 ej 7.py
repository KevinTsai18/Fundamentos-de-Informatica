print("hola mundo")
print("Ingrese un período en segundos")
s=input()
s=int(s)
s1=int(s%60)
m=int(s/60)
m1=int(m%60)
h=int(m/60)
h1=int(h%24)
d=int(h/24)
print(s, "segundos equivalen a", d, "días", h1, "horas", m1, "minutos", s1, "segundos")
