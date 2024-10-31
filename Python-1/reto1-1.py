"""
-------------------------------------------------
             JUEGO: ADIVINA EL NÚMERO
-------------------------------------------------
Descripción:
  Este programa genera un número aleatorio entre 1 y 100,
  y desafía al usuario a adivinarlo. El usuario ingresará
  sus intentos y el programa le dará pistas sobre si su
  número es mayor o menor que el número a adivinar.

Instrucciones:
  1. Inicia el juego y espera que se genere un número.
  2. Ingresa tu intento para adivinar el número.
  3. Recibirás pistas hasta que adivines el número correcto.
  4. El programa mostrará el número total de intentos al
     finalizar el juego.

    Pistas Adicionales:
        1. Puedes agregar la opción de que el usuario elija si quiere jugar nuevamente después de adivinar el número.
        2. Si el usuario ingresa un valor no válido (como una letra), el programa debe manejar ese error de manera adecuada.

-------------------------------------------------
                EJEMPLO DE EJECUCIÓN
-------------------------------------------------

Adivina el número (entre 1 y 100): 50
El número es mayor.
Adivina el número: 75
El número es menor.
Adivina el número: 60
¡Felicidades! Has adivinado el número en 3 intentos.

-------------------------------------------------
"""

import random

n_aleatorio = random.randint(1, 100)
trys = 1

num_user = int(input("Adivina el número (entre 1 y 100): "))

while num_user < 100 and num_user > 1:
  if num_user > n_aleatorio:
    print("El número es menor.")
    num_user = int(input("Adivina el número: "))
    trys += 1

  elif num_user < n_aleatorio:
    print("El número es mayor.")
    num_user = int(input("Adivina el número: "))
    trys += 1

  elif num_user == n_aleatorio:
    print(f"¡Felicidades! Has adivinado el número en {trys} intentos.")
    break

  else:
    print("ERROR: El número se encuentra fuera del rango 1-100")
    print("USAGE: Números validos [1-100]")
