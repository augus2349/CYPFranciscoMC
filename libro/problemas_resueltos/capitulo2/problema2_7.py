A = int(input("ingrese un numero entero positivo "))
B = int(input("ingrese un numero entero positivo diferente "))
C = int(input("ingrese un numero entero positivo diferente a los dos anteriores "))
if A < B:
    if B < C:
        print("los numeros estan en orden creciente")
    else:
        print("los numeros NO estan en orden creciente")
else:
    print("los numeros NO estan en orden creciente")
