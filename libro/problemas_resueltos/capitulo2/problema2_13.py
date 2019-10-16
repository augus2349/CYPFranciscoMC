M = int(input("ingrese la matricula del alumno"))
CAR = str(input("ingrese la carrera en la que esta el alumno (EN MAYUSCULAS)"))
S = int(input("ingrese el semetre del alumno"))
P = float(input("ingrese el promedio del alumno"))
if CAR == "ECONOMIA":
    if S >= 6 and P >= 8.8:
        print(M," ,",CAR," ACEPTADO")
    else:
        print("RECHAZADO")
elif CAR == "COMPUTACION":
    if S >= 6 and P >= 8.5:
        print(M," ,",CAR," ACEPTADO")
    else:
        print("RECHAZADO")
elif CAR == "CONTABILIDAD":
    if S >= 6 and P >= 8.5:
        print(M," ,",CAR," ACEPTADO")
    else:
        print("RECHAZADO")
elif CAR == "ADMINISTRACION":
    if S >= 6 and P >= 8.5:
        print(M," ,",CAR," ACEPTADO")
    else:
        print("RECHAZADO")
else:
    print("sin resultados verifique que los datos esten correctos")
print("fin")
