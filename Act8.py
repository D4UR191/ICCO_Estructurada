# Comparación de cadenas

nombre = []
intentos = 1
print("\nTest Dragon Ball")
while nombre != 'GINE':
    print(f"\nIntento: {intentos}", end="")
    nombre = input("¿Cuál es el nombre de la mamá de Gokú? ").upper()
    intentos += 1
print("\nCorrecto!")
