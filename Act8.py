# ComparaciÃ³n de cadenas

nombre = []
intentos = 1
print("\nTest Dragon Ball")
while nombre != 'GINE':
    print(f"\nIntento: {intentos}", end="")
    nombre = input("¿Cual es el nombre de la madre de Goku? ").upper()
    intentos += 1
print("\nCorrecto!")
