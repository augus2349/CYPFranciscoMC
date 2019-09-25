SUE = float(input("ingrese el sueldo "))
if SUE < 1000:
    NSUE = SUE * 1.15
else:
    NSUE = SUE * 1.12
print(f"el nuevo sueldo es: { NSUE }")

