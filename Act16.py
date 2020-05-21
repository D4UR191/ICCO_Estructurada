# Contador de una letra en un archivo

archivo = open('greetings.txt', 'w')
archivo.write('Hola\nQue tal!\nBuen dia\nComo estas?')
archivo.close()

caracter = 'a'
contador = 0

archivo = open('greetings.txt', 'r')
txt = archivo.read()
for linea in txt:
    linea = linea.lower()
    contador += linea.count(caracter)
archivo.close()

print(f'El archivo {archivo.name}:\n',
      f'\n"{txt}"\n\ntiene {contador} veces la letra "{caracter}"')
