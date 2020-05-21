# Contador de consonantes


def contador_consonantes(cadena):
    vocales = list("AaEeIiOoUu")
    contador = 0
    for i in range(0, len(cadena)):
        if cadena[i].isalpha() and cadena[i] not in vocales:
            contador += 1
    return contador


entrada = input("Ingrese la cadena: ")
print("Número de consonantes:", contador_consonantes(entrada))
