# NÃºmeros de Fibonacci

# import math


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-2) + fibonacci(num-1)


# Método alternativo
"""
def fibonacci(num):
    phi = (1 + math.sqrt(5)) / 2
    return int(phi**num / math.sqrt(5) + 1/2)
"""

n = int(input("Escribe un numero entero: "))
print(f"\nSu fibonacci es: F({n}) = {fibonacci(n)}")

lista = []
for i in range(0, n+1):
    lista.append(fibonacci(i))
print(f"\nLa sucesion de fibonacci hasta n = {n} es: {lista}")
