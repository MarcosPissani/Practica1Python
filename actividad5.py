precio = float(input("Ingrese un numero : "))
acumular = 0
while precio != 0:
    acumular += precio
    precio = float(input("Ingrese un numero : "))

print("El total es : ", acumular)