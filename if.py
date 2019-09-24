edad = int(input("dame tu edad "))
INE = bool(int(input("tienes INE (0 NO / 1 SI) ")))
if edad >= 18 and INE == True:
    print("es mayor de edad")
    print("aun dentro de if")
print("fin")
