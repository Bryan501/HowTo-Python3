import random

n_aleatorio = random.randint(1, 100)
trys = 0

print("¡Bienvenido al juego de Adivina el Número!")
print("He seleccionado un número entre 1 y 100. ¡Intenta adivinarlo!")

while True:
    try:
        num_user = int(input("Adivina el número (entre 1 y 100): "))
        
        if num_user < 1 or num_user > 100:
            print("ERROR: El número se encuentra fuera del rango 1-100")
            print("USAGE: Números válidos [1-100]")
            continue
        
        trys += 1
        
        if num_user > n_aleatorio:
            print("El número es menor.")
        elif num_user < n_aleatorio:
            print("El número es mayor.")
        else:
            print(f"¡Felicidades! Has adivinado el número en {trys} intentos.")
            break
    except ValueError:
        print("ERROR: Por favor, ingresa un número válido.")