SUE = float(input("ingrese el sueldo "))
if SUE < 1000:
    AUM = SUE * 0.15
    MSUE = SUE + AUM
    print(f"el aumento del sueldo fue de { AUM } y el sueldo sera de { MSUE }")
print("fin")
