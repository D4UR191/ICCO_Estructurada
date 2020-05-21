# Actividad 12

impuesto = 0.16
horas = int(input("Cantidad de hrs trabajadas: "))
sueldo = float(input("Sueldo por hr: $"))
print(f"\nDías Trabajados: {horas // 8} dias con {horas % 8} hrs")
print("Sueldo: $""{:.2f}".format(horas * sueldo))
print("Descuento: $""{:.2f}".format(horas * sueldo * impuesto))
print("Neto: $""{:.2f}".format(horas * sueldo * (1 - impuesto)))
