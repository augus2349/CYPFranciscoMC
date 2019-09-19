NOM = str(input("ingrese el nombre del dinosaurio "))
PES = float(input("ingrese el peso (en toneladas) del dinosaurio "))
LON = float(input("ingrese la longitud (en pies) del dinosaurio "))
PESKIL = PES * 1000
LONMET = LON * 0.3047
print(f"el dinosario { NOM }, tiene un peso de { PESKIL }kg y una longitud de { LONMET }mts. ")
