B = True
I = 2
S = 0
while I <= 1800:
    S += I
    print(I)
    if B == True:
        B = False
        I += 3
    else:
        B = True
        I += 2
print(S)
