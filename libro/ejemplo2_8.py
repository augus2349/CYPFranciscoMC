CATE = int(input("ingrese la categoria del trabajador (1-4) "))
SUE = float(input("ingrese el sueldo del trabajador "))
if CATE == 1:
    NSUE = SUE * 1.15
elif CATE == 2:
    NSUE = SUE * 1.10
elif CATE == 3:
    NSUE = SUE * 1.08
elif CATE == 4:
    NSUE = SUE * 1.07
else:
    print("error 404")
print(f"catergoria: { CATE }, el nuevo sueldo es: { NSUE }")
