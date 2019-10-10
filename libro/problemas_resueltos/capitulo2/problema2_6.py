A = int(input("ingrese un numero entero"))
B = (-1)**A
if A == 0:
    print(f"el numero { A } es NULO")
else:
    if B > 0:
        print(f"el numero { A } es PAR")
    else:
        print(f"el numero { A } es IMPAR")
