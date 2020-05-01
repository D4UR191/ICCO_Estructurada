# Ordenamiento de números


def ordenador(vector):  # Bubble sort
    bandera = 1
    contador = 0
    while bandera == 1:
        bandera = 0
        contador += 1
        for i in range(0, len(vector) - contador):
            if vector[i] < vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i]  # Cambiar
                bandera = 1
    return vector


lista = []
numeros = 10
print(f"\nOrdenamiento de {numeros} números")
for i in range(0, numeros):
    lista.append(int(input("\tNuevo número: ")))
print(f"\nLista ordenada (decreciente): {ordenador(lista)}")
