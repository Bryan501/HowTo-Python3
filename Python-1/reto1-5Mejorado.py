"""
-------------------------------------------------
              JUEGO DE ADIVINANZA DE PALABRAS
-------------------------------------------------
Descripción:
  Este programa es un juego en el que el usuario
  debe adivinar una palabra secreta elegida al azar
  de una lista de palabras. El usuario tiene un número
  limitado de intentos para adivinar la palabra.

Requisitos:
  - Una lista de al menos 5 palabras.
  - El programa elegirá una palabra secreta al azar.
  - El usuario ingresará sus intentos para adivinar.
  - El programa informará si el intento es correcto
    o incorrecto y cuántos intentos le quedan.
  - Si el usuario adivina la palabra, se mostrará un
    mensaje de felicitación y terminará el juego.
  - Si no adivina en el número de intentos permitidos,
    se revelará la palabra secreta.

Ejemplo de ejecución:
-----------------------------------------------
La palabra secreta tiene 5 letras. ¡Adivina la palabra!
Tienes 5 intentos.

Introduce tu intento: casa
Incorrecto. Te quedan 4 intentos.

Introduce tu intento: perro
Incorrecto. Te quedan 3 intentos.

Introduce tu intento: playa
¡Felicidades! Has adivinado la palabra secreta: playa.
-------------------------------------------------
"""

import random

len_random = random.randint(4,6)
p_animales = ["perro", "gato", "tigre", "cebra", "ratón", "rana", "águila", "lobo"]

palabras_filtradas = []
for palabra in p_animales:
    if len(palabra) == len_random:
        palabras_filtradas.append(palabra)

p_random = random.choice(palabras_filtradas)

print(f"La palabra secreta tiene {len_random} letras. ¡Adivina la palabra!\n"
      "Temática de animales\nTienes 5 intentos.\n")

def respuesta(intentos):
    palabra = input("Introduce tu intento: ").strip().lower()
    if not palabra:
        print(f"deberias de introducir una cadena de texto cumpliendo el rango de palabras")
        return respuesta(intentos)
    comprobar(palabra, intentos)

def comprobar(palabra, intentos):
    if len(palabra) != len_random:
        print(f"La palabra debe tener {len_random} letras. Inténtalo de nuevo.")
        respuesta(intentos)
    elif palabra == p_random:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {p_random}")
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Incorrecto. Te quedan {intentos} intentos.")
            respuesta(intentos)
        else:
            print(f"¡Has agotado todos tus intentos! La palabra secreta era: {p_random}.")
respuesta(5)
