# Ordanamieto Burbuja

import random


def bubbleSort(vector):  # Bubble sort
    bandera = 1
    contador = 0
    while bandera == 1:
        bandera = 0
        contador += 1
        for i in range(0, len(vector) - contador):
            if vector[i] > vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i]
                bandera = 1
    return vector


numeros = 10
lista = [random.randint(0, 100) for _ in range(numeros)]
print(f"\nOrdenamiento de {numeros} números: {lista}")
lista = bubbleSort(lista)
print(f"\nLista ordenada (creciente): {lista}")
print(f"\nLista ordenada (decreciente): {lista[::-1]}")
