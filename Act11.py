# Actividad 11


def glosario(num):
    if num == 1:
        return 'uno'
    elif num == 2:
        return 'dos'
    elif num == 3:
        return 'tres'
    elif num == 4:
        return 'cuatro'
    elif num == 5:
        return 'cinco'
    elif num == 6:
        return 'seis'
    elif num == 7:
        return 'siete'
    elif num == 8:
        return 'ocho'
    elif num == 9:
        return 'nueve'
    elif num == 10:
        return 'diez'


lista = []
contador = 0
n = int(input("Cantidad de numeros: "))
print(f"\nIntroduce numeros flotantes entre 1.0 y 10.0")
while contador < n:
    numero = float(input("\tNuevo numero: "))
    if numero >= 1 and numero <= 10:
        lista.append(numero)
        contador += 1
    else:
        print("\nNumero fuera de rango, intenta nuevamente.")
ordenada = sorted(lista)
print(f"\nLa lista ordenada es: {ordenada}")
print(f"El mayor es: {ordenada[n-1]} ({glosario(int(ordenada[n-1]))}...)")
