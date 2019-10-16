A = float(input("ingrese el precio base"))
if A > 500:
    I = 20*0.3+(A-40)*0.40
elif A > 40:
    I = 20*0.3+(A-40)*0.40
elif A > 20:
    I = (A-20)*0.30
else:
    I = 0
P = A + I
print(f"el precio base es de { A } y el precio con impuesto es de { P }")
