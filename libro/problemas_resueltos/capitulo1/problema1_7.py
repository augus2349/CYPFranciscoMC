L1 = float(input("ingrese el primer lado del triangulo: "))
L2 = float(input("ingrese el segundo lado del triangulo: "))
L3 = float(input("ingrese el tercer lado del triangulo: "))
S = (L1 + L2 + L3) / 2
AREA = (S * (S - L1) * (S - L2) * (S - L3)) ** (1 / 2)
print(f"el area del triangulo es: { AREA }")
