S = 0
N = int(input("ingrese un numero entero positivo"))
B = True
for I in range(1,N+1,1):
    if B == True:
        S += 1/I
        B = False
    else:
        S -= 1/I
        B = True
print(S)
