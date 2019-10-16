C = int(input("ingrese la clave de telefonica"))
M = int(input("ingrese la duuracion de la llamada (en minutos)"))
if C == 12:
    CO = M*2
elif C == 15:
    CO = M*2.2
elif C == 18:
    CO = M*4.5
elif C == 19:
    CO = M*3.5
elif C == 23 or C == 25:
    CO = M*6
elif C == 29:
    CO = M*5
else:
    CO = "error"
print(f"costo total de la llamada { CO }")
