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
p_random = random.choice(p_animales)

print(f"La palabra secreta tiene {len_random} letras. ¡Adivina la palabra!\n"
      "Temática de animales\nTienes 5 intentos.\n")

def respuesta():
    palabra = input("Introduce tu intento: ")
    if palabra.strip():
       comprobar(palabra)
    else:
        print(f"deberias de introducir una cadena de texto cumpliendo el rango de palabras")

def repeticion():
 intentos = 6
 intentos -= 1
 while intentos != 0:
  print(f"Incorrecto. Te quedan {intentos} intentos.")
  respuesta()

def comprobar(palabra):
    if len(palabra) == len_random:
        if palabra == p_random:
            print(f"¡Felicidades! Has adivinado la palabra secreta: {p_random}")
        elif palabra != p_random:
         repeticion()
        else:
           pass
        
    else:
        print(f"debes de poner una palabra que tenga {len_random} palabras")
        respuesta()

respuesta()