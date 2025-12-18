# Importamos la librería random para trabajar con valores aleatorios
import random

# FUNCIÓN: obtener_palabra_aleatoria
# -----------------------------
# Esta función se encarga de seleccionar una palabra al azar
# desde una lista predefinida de palabras culturales ecuatorianas
def obtener_palabra_aleatoria():

    # Lista de palabras que el jugador deberá adivinar
    palabras = ["ecuador", "pasillo", "chuchaqui", "hornado", "fritada", "iglesia"]

    # random.choice selecciona un elemento aleatorio de la lista
    palabra_aleatoria = random.choice(palabras)

    # Se retorna la palabra seleccionada para ser usada en el juego
    return palabra_aleatoria



# FUNCIÓN: mostrar_tablero
# Esta función muestra el estado actual del juego
# Es decir, las letras adivinadas y los guiones bajos
def mostrar_tablero(palabra_secreta, letras_adivinadas):

    # Variable donde se construye el tablero visual
    tablero = ""

    # Bucle for que recorre cada letra de la palabra secreta
    for letra in palabra_secreta:

        # Verificamos si la letra ya fue adivinada por el jugador
        if letra in letras_adivinadas:
            tablero += letra
        else:
            # Si no ha sido adivinada, se muestra un guion bajo
            tablero += "_"

    # Se imprime el tablero actualizado en pantalla
    print(tablero)

# FUNCIÓN PRINCIPAL: jugar_ahorcado
# Esta función controla toda la lógica del juego
def jugar_ahorcado():

    # Se obtiene una palabra secreta usando la función anterior
    palabra_secreta = obtener_palabra_aleatoria()

    # Lista vacía donde se almacenan las letras ingresadas por el jugador
    letras_adivinadas = []

    # Número máximo de intentos permitidos
    intentos_restantes = 7

    # Mensaje inicial de bienvenida al jugador
    print("¡Bienvenido al juego del ahorcado!")

    # Línea de depuración (DEBUG)
    # Sirve para verificar la palabra secreta durante pruebas
    
    # Bucle while que mantiene el juego activo
    # Se ejecuta mientras el jugador tenga intentos disponibles
    while intentos_restantes > 0:

        # Se muestran los intentos restantes
        print(f"\nTe quedan {intentos_restantes} intentos.")

        # Se muestra el tablero actual del juego
        mostrar_tablero(palabra_secreta, letras_adivinadas)

        # Se solicita al usuario ingresar una letra
        # lower() convierte la entrada a minúsculas
        # strip() elimina espacios innecesarios
        letra = input("Ingresa una letra: ").lower().strip()  
        # Se verifica que el usuario ingrese solo una letra
        # y que sea un carácter alfabético
        if len(letra) != 1 or not letra.isalpha():
            print("Debes ingresar solo UNA letra.")
            continue  # Regresa al inicio del bucle

        # Se verifica si la letra ya fue ingresada antes
        if letra in letras_adivinadas:
            print("Ya has introducido esa letra. Prueba otra vez :)")
            continue  # Evita repetir letras

        # Se agrega la letra ingresada a la lista
        letras_adivinadas.append(letra)

 
        # VERIFICACIÓN DE LETRA CORRECTA
        # Se comprueba si la letra está en la palabra secreta
        if letra in palabra_secreta:
            print("¡Bien! Esa letra está en la palabra :)")

            # Se verifica si todas las letras ya fueron adivinadas
            # all() devuelve True si todas las condiciones se cumplen
            if all(l in letras_adivinadas for l in palabra_secreta):
                mostrar_tablero(palabra_secreta, letras_adivinadas)
                print("\n¡Felicidades! Eres todo un detective de las palabras.")
                return  # Finaliza el juego al ganar
        else:
            # Si la letra no está en la palabra, se pierde un intento
            intentos_restantes -= 1
            print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")

    # Si el bucle termina, el jugador se quedó sin intentos
    print(f"\nHas perdido. Pero no te preocupes, la palabra secreta era: {palabra_secreta}")

# Inicia el juego del ahorcado
jugar_ahorcado()