S = float(input("ingrese el sueldo base del trabajador"))
C = int(input("ingrese la categoria del trabajador"))
H = int(input("ingrese las horas extras"))
if C == 1:
    PH = 30
elif H == 2:
    PH = 38
elif H == 3:
    PH = 50
elif H == 4:
    PH = 70
else:
    PH = 0
if H > 50:
    NS = S+30*PH
else:
    NS = S+H*PH
print(f"el sueldo del trabajador categoria { C } es de { NS }")
