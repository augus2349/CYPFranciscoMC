# print tiene 4 fromas de uso
"""
1.- con comas
2.- con signo '+'
3.- con la funcion formart()
4.- Es con una varible de format()
"""
# con comas
edad = 10
nombre = "juan"
estatura = 1.65
print(edad , estatura, nombre)
# con '+' hace lo mismo pero no hace el cambio automatico
print(str(edad) + str(estatura) + nombre)
# funcion format ()
print("nombre: {}, edad: {}".format(nombre, edad))
#varainte format () simplificada
print(f"Nombre \"{nombre}\" \nEdad:\t{edad}")
# print y el argumento end
print("solo hay 10 tipos de personas, las que saben binario y las que no",end=" ")
print("otra linea")
