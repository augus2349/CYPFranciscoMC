E = int(input("ingrese el numero de empleado"))
N = 0
for v in range(1,E+1,1):
    SUE = float(input(f"ingrese el sueldo del emplado {v}: "))
    N += SUE
print(f" la nomina es de: { N }")
