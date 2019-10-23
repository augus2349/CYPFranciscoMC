SP = 0
SIP = 0
NP = 0
for i in range(1,271,1):
    N=int(input("ingrese un numero entero"))
    if N != 0:
        if (N**(-1))>0:
            SP += N
            NP += 1
        else:
            SP += N
PP=SP/NP
print(f"El promedio de los pares es { PP } y la suma de los impares es { SIP }")

