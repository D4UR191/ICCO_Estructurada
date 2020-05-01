# Escribir un archivo 2

print("\nNuevo documento")
texto = input(">>\t")
nombre = input("Nombre del archivo: ")
file = open(f"C:/Users/OVN91/Desktop/{nombre}.txt", "w")
file.write(texto)
file.close()
print("\nGuardado")
