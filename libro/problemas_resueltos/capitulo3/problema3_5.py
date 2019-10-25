N = int(input("ingrese el numero de datos a ingresar "))
SP = 0
SO = 0
CP = 0
for i in range(1,N+1,1):
    NUM = int(input("ingrese un numero entero "))
    if NUM > 0:
        SP += NUM
        CP += 1
    else:
        SO += NUM
PG = (SP+SO)/N
PP = SP/CP
print(f"hay { CP } numeros positivos, el promedio general es de { PG } y el promedio de los numeros positivos es de { PP }")
