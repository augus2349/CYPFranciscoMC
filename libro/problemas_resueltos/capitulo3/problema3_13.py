ARSU = 0 
ARNO = 0
MERSU = 50000
ARCE = 0
MES = 0
for i in range(1,13,1):
    print(f"Mes { i }")
    RNO = int(input("promedio de lluvia del mes en el norte: "))
    RCE = int(input("promedio de lluvia del mes en el centro: "))
    RSU = int(input("promedio de lluvia del mes en el sur: "))

    ARNO = ARNO + RNO
    ARCE = ARCE + RCE
    ARSU = ARSU + RSU

    if RSU < MERSU:
        MERSU = RSU
        MES = 1
PRORCE = ARCE / 12
print(f"promedio region centro: { PRORCE}")
print(f"mes con menor lluvia en reg. sur { MES }")
print(f"registor  del mes con menor lluvia es: { MERSU}")

if ARNO > ARCE:
    if ARNO > ARSU:
        print("la region con mayor lluvia es la region norte")
    else:
        print("la region con mayor lluvia es la region sur")
elif ARCE > ARSU:
    print("la region con mayor lluvia es la region centro")
else:
    print("la region con mayor lluvia es la region sur")
print("fin")
