MAT = int(input("ingrese la matricula del alumno"))
CAL1 = float(input("ingrese la primer calificacion"))
CAL2 = float(input("ingrese la segunda calificacion"))
CAL3 = float(input("ingrese la tercer calificacion"))
CAL4 = float(input("ingrese la cuarta calificacion"))
CAL5 = float(input("ingrese la quinta calificacion"))
PRO = (CAL1 + CAL2 + CAL3 + CAL4 + CAL5)/5
if PRO>=6:
    print(f"el alumno No { MAT } aprobo con un promedio de { PRO }")
else:
    print(f"el alumno No { MAT } no aprobo con un promedio de { PRO }")
