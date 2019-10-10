A = int(input("ingrese un numero entero positivo"))
B = int(input("ingrese un numero entero positivo diferente"))
C = int(input("ingrese un numero entero positivo diferente a los dos anteriores"))
if A > B:
    if A > C:
        if B > C:
            print(f"{A}>{B}>{C}")
        else:
            print(f"{A}>{C}>{B}")
    else:
        print(f"{C}>{A}>{B}")
else:
    if B>C:
        if A>C:
            print(f"{B}>{A}>{C}")
        else:
            print(f"{B}>{C}>{A}")
    else:
        print(f"{C}>{B}>{A}")
print("fin")
