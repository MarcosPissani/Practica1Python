num = int(input("Ingrese un numero entero: "))
lista5 = []
lista = []
for i in range (1, num + 1):
    if i % 5 == 0:  
        lista5.append(i)
    else:
        lista.append(i)

print(lista)
print(f"{"-"*30}")
print(lista5)