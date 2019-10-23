N=0
S=float(input("ingrese el sueldo"))
while S != (-1):
    if S < 1000:
        NS = S*1.15
    else:
        NS = S*1.12
    N += NS
    print(NS)
    S=float(input("ingrese el sueldo"))
print(N)
