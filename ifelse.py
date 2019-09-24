edad = int(input("dame tu edad: "))
INE = bool(int(input("Tienes INE (0 NO / 1 SI)?: ")))

if edad >= 18 and INE == True:
    print("Es mayor de edad")
    print("peda en terrazas")
else:
    print("Eres menor de edad")
    print("A la choza de los pequeñines")
print("fin")
