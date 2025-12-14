Juego del Ahorcado en Python (Ecuador Edition)
OBJETIVO DEL PROGRAMA

Desarrollar un juego interactivo de consola (terminal) en Python donde el usuario debe adivinar una palabra secreta letra por letra antes de quedarse sin intentos. El programa refuerza el uso de funciones, estructuras de control, validación de datos, listas y ciclos, aplicados en un caso práctico y entretenido.

CONTEXTO DEL PROYECTO

Se escogió el juego del ahorcado por la diversión que genera al adivinar palabras y por el reto progresivo que implica en cada intento. Además, para darle identidad al proyecto, el banco de palabras incluye términos relacionados con la cultura y el folklore ecuatoriano (por ejemplo, comida típica y expresiones comunes).

FUNCIONALIDADES PRINCIPALES

-Selección aleatoria de palabras: el programa elige una palabra al azar de una lista predefinida.

-Tablero visual en consola: muestra guiones bajos _ para letras no descubiertas y revela letras correctas.

-Sistema de intentos: el jugador empieza con 7 intentos; cada letra incorrecta resta 1 intento.

-Validación de entrada:

Solo permite ingresar una letra a la vez.

Verifica que el carácter ingresado sea una letra (a-z).

Evita repetir letras ya ingresadas.

-Mensajes de retroalimentación: informa si la letra es correcta/incorrecta y cuántos intentos quedan.

-Condición de victoria/derrota:

Gana si descubre todas las letras de la palabra.

Pierde si se quedan sin intentos y se muestra la palabra secreta.

TÉCNOLOGIAS USADAS

Lenguaje: Python 3

Librería estándar: random (para selección aleatoria)

CÓMO EJECUTAR EL PROGRAMA

1.Clona o descarga este repositorio.

2.Abre una terminal en la carpeta del proyecto.

Ejecuta:

python final_v2.py


Nota: El nombre del archivo puede variar según cómo lo guardes en tu repositorio.

COMO JUGAR

El programa mostrará un tablero con guiones bajos (ejemplo: _ _ _ _ _ _).

Ingresa una letra cuando te lo solicite.

Si aciertas, la letra aparecerá en el tablero.

Si fallas, perderás un intento.

El juego termina cuando:

adivinas la palabra, o

se acaban los intentos.

PALABRAS INCLUIDAS

El juego usa palabras como:

ecuador, pasillo, chuchaqui, hornado, fritada, iglesia

(La lista puede ampliarse fácilmente en la función obtener_palabra_aleatoria().)

ESTRUCTURA DEL CODIGO 
obtener_palabra_aleatoria(): define y selecciona la palabra secreta al azar.

mostrar_tablero(palabra_secreta, letras_adivinadas): construye e imprime el tablero en consola.

jugar_ahorcado(): contiene la lógica principal del juego (ciclo de intentos, validaciones, victoria/derrota).

Fecha

14 de diciembre de 2025

DARWIN ORQUERA

[Tu nombre aquí]
Asignatura: Lógica de Programación
