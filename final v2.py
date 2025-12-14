import random

def obtener_palabra_aleatoria():
    palabras = ["ecuador", "pasillo", "chuchaqui", "hornado", "fritada", "iglesia"]
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra
        else:
            tablero += "_"
    print(tablero)

def jugar_ahorcado():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos_restantes = 7

    print("¡Bienvenido al juego del ahorcado!")
    # Descomenta esta línea solo para pruebas:
    # print("DEBUG - Palabra secreta:", palabra_secreta)

    while intentos_restantes > 0:
        print(f"\nTe quedan {intentos_restantes} intentos.")
        mostrar_tablero(palabra_secreta, letras_adivinadas)

        letra = input("Ingresa una letra: ").lower().strip()

        # Validación básica
        if len(letra) != 1 or not letra.isalpha():
            print("Debes ingresar solo UNA letra.")
            continue

        if letra in letras_adivinadas:
            print("Ya has introducido esa letra. Prueba otra vez :)")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Bien! Esa letra está en la palabra :)")

            # Comprobamos si ya se adivinó toda la palabra
            if all(l in letras_adivinadas for l in palabra_secreta):
                mostrar_tablero(palabra_secreta, letras_adivinadas)
                print("\n¡Felicidades! Eres todo un detective de las palabras.")
                return
        else:
            intentos_restantes -= 1
            print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")

    # Si sale del while por quedarse sin intentos
    print(f"\nHas perdido. Pero no te preocupes, la palabra secreta era: {palabra_secreta}")

jugar_ahorcado()

