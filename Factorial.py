# Factorial de un número


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


num = int(input("Escribe un numero entero: "))
print(f"\nSu factorial es: {num}! = {factorial(num)}")
