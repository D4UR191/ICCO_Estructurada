# Números primos


def primos(lista):
    primo = []
    for x in lista:
        divisor = 1
        if x == 2 and x not in primo:
            primo.append(x)
        else:
            while divisor < x:
                divisor += 1
                if x % divisor == 0:
                    break
                elif divisor + 1 == x and x not in primo:
                    primo.append(x)
    return primo


n = 5
num = []
print(f"\nIngresa hasta {n} numeros enteros")
for i in range(0, n):
    num.append(int(input("\tNuevo numero: ")))
print(f"\nPrimos encontrados: {sorted(primos(num))}")
