N = int(input("ingrese un numero entero positivo"))
CUECER = 0
for v in range(1,N+1,1):
    NUM = int(input("ingrese un numero entero: "))
    if NUM == 0:
        CUECER += 1
print("el numero de 0 capturados fue:",CUECER)
