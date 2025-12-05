import random

def obtener_palabra_aleatoria():
    palabras=["ecuador","pasillo","chuchaqui","hornado","fritada","iglesia"] 
    palabra_aleatoria=random.choice(palabras)   
    return palabra_aleatoria

def mostrar_tablero(palabra_secreta,letras_adivinadas):
    tablero=""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero+=letra
        else:
            tablero+="_"
    print(tablero)

def jugar_ahorcado():
    palabra_secreta=obtener_palabra_aleatoria()
    letras_adivinadas=[]
    intentos_restantes=7

    while intentos_restantes>0:
        mostrar_tablero(palabra_secreta, letras_adivinadas) 
        letra=input("Ingresa una letra: ").lower() 
        