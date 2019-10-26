N = int(input("ingrese el numero hasta el cual acabara la serie"))
S=0
for i in range(1,N+1,1):
    S += i**i
print(S)
