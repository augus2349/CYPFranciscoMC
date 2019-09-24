A = int(input("ingrese un valor"))
B = int(input("ingrese otro valor"))
C = int(input("ingrese el ultimo valor"))
if A!=B and A!=C and B!=C:
    if A>B and A>C:
        print(f"{ A } es mayor")
    else:
        if B>A and B>C:
            print(f"{ B } es mayor")
        else:
            print(f"{ C } es mayor")
print("return 0")
