PREPRO = float(input("ingrese el precio del producto: "))
PAGO = float(input("ingrese el pago que se realizo: "))
DEVO = PAGO - PREPRO
print(f"se pago { PAGO }$ y el precio del producto es: { PREPRO }$\nel cambio del cliente es: { DEVO }$")
