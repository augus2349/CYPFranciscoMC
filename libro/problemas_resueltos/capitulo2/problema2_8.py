C = float(input("ingrese el valor de la compra"))
if C < 500:
    D = C
elif C <= 1000:
    D = C-C*0.05
elif C <= 7000:
    D = C-C*0.11
elif C <= 15000:
    D = C-C*0.18
else:
    D = C-C*0.25
print(f"la cantidad a pagar es { D }")
