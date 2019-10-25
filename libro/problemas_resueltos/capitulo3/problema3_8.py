NUM = int(input("ingrese un numero entero: "))
if NUM > 0:
    while (NUM != 1):
        print(NUM)
        if ((-1)**NUM)>0:
            NUM = NUM/2
        else:
            NUM = NUM*3+1
    print(NUM)
else:
    print("el numero tiene que ser positivo")
