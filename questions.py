import random

words = {
    "informatica" : ["python", "programa" ,"variable" ,],
    "tipos de datos" : ["cadena", "entero", "lista"],
    "estructuras de control" : ["funcion", "bucle"],
}

print("¡Bienvenido al Ahorcado!")
print("")
print("Quieres comenzar el juego? si/no")
start = input().lower()
print("")
while start == "si":
    print("Categorías disponibles:")
    for category in words.keys():
        print(f"- {category}")
    category = input("Elegí una categoría: ").lower()
    while category not in words:
        print("Categoría no válida")
        category = input("Elegí una categoría: ").lower()

    print(f"Has elegido la categoría: {category}")
    print("")
    #Tomamos de forma random todas las palabras de la categoria elegida
    word_list = random.sample(list(words[category]),len(words[category]))
    #Quitamos de la lista la ultima palabra de la lista random y la guardamos en word
    word = word_list.pop()
    guessed = []
    attempts = 6
    print()
    puntaje = 0
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntaje += 6
            print (f"Puntos obtenidos: {puntaje}")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")
        if len(letter) == 1 and letter.isalpha():
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:   
                guessed.append(letter)
                attempts -= 1
                print("Esa letra no está en la palabra.")
                puntaje -= 1
        else:
            print ("Entrada no válida")

        print()

    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje = 0
        print (f"Puntos obtenidos: {puntaje}")


    print("¿Quieres jugar de nuevo? si/no")
    start = input().lower()

print("Fin del juego")