A = float(input("ingrese el valor de A"))
B = float(input("ingrese el valor de B"))
C = float(input("ingrese el valor de C"))
DIS = B**2-(4*A*C)
if DIS>=0:
    X1=((-B)+DIS**0.5)/2*A
    X2=((-B)-DIS**0.5)/2*A
    print(f"raices relaes son: x1:{ X1 }, x2:{ X2 }")
print("fin del programa")
