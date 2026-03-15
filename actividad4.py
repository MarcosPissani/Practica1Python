num = int(input("Ingrese un numero entero: "))

for i in range (1, num + 1):
    if i % 5 == 0:  
        continue
    else:
        print(i)
        