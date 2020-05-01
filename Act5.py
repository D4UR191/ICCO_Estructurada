# Media aritmética, moda y desviación estándar


def media(lista):
    media = 0
    for i in range(0, len(lista)):
        media += (datos[i] / n)
    return media


def moda(lista):
    moda = []
    contador = 0
    for x in lista:
        apariciones = lista.count(x)
        if apariciones > contador:
            contador = apariciones
    for x in lista:
        apariciones = lista.count(x)
        if apariciones == contador and x not in moda:
            moda.append(x)
    return moda


def desviacion(lista, media):
    from math import sqrt
    varianza = 0
    for i in range(0, len(lista)):
        varianza += (datos[i] - media)**2
    return sqrt(varianza / (n-1))


datos = []
print("\nMedia aritmética, moda y desviación estandar")
n = int(input("Cantidad de datos: "))
for i in range(0, n):
    nuevo = float(input("\tNuevo dato: "))
    datos.append(nuevo)
x = media(datos)
mo = sorted(moda(datos))
s = desviacion(datos, x)
print("\nMedia aritmética:", "{:.2f}".format(x))
print("Moda: ", end="")
for i in range(0, len(mo)-1):
    print("{:.2f}".format(mo[i]), end=", ")
print("{:.2f}".format(mo[len(mo)-1]))
print("Desviación estándar:", "{:.2f}".format(s))
