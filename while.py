otra = bool(int(input("hay mas alumnos(1 si, 0 no):")))
suma = 0
p = 0
while(otra==True):
    cal = float(input("calificaciones: "))
    p += 1
    suma += cal
    otra = bool(int(input("hay mas alumnos(1 si, 0 no):")))
print("suma: ", suma)
print("promedio", suma/p)
print("se acabo")
