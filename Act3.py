# Eliminador de vocales


def eliminador_vocales(cadena):
    vocales = list("AaEeIiOoUu")
    nueva = ""
    for i in range(0, len(cadena)):
        if cadena[i] not in vocales:
            nueva += cadena[i]
    return nueva


original = input("Ingrese la cadena: ")
print("Cadena sin vocales:", eliminador_vocales(original))
