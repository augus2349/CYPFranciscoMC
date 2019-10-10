A = int(input("ingrese un numero entero positivo"))
B = int(input("ingrese un numero entero positivo"))
C= int(input("ingrese un numero entero positivo"))
if A > B:
    if A > C:
        print(f"A ({ A }) es el mayor")
    elif A == C:
        print(f"A y C ({ A }) son los mayores")
    else:
        print(f"C ({ C }) es el mayor")
elif A == B:
    if A > C:
        print(f"A y B ({ A }) son los mayores")
    elif A == C:
        print(f"los tres numeros son iguales a { A }")
    else:
        print(f"C ({ C }) es el mayor")
elif B > C:
    print(f"B ({ B }) es el mayor")
elif B == C:
    print(f"B y C ({ B }) son los mayores")
else:
    print(f"C ({ C }) es el mayor")
