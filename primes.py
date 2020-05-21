# Buscador de números primos


def primos(lista):
    primo = []
    for x in lista:
        divisor = 1
        if x == 2:
            primo.append(x)
        else:
            while divisor < x:
                divisor += 1
                if x % divisor == 0:
                    break
                elif divisor + 1 == x:
                    primo.append(x)
    return primo


n = 100
num = []
for i in range(0, n + 1):
    num.append(i)
print(f"\nPrimos encontrados del 1 al {n}: {primos(num)}")
