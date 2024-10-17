"""
---------------------------------------------------------
            CALCULADORA CON HISTORIAL DE OPERACIONES
---------------------------------------------------------
Descripción:
  Este programa es una calculadora que permite realizar
  operaciones básicas (suma, resta, multiplicación,
  división, potenciación y módulo) y almacena un historial
  de todas las operaciones realizadas. El usuario puede
  ver el historial en cualquier momento o salir del programa.

Menú de opciones:
  1. Realizar una nueva operación
  2. Ver historial de operaciones
  3. Salir

Operaciones permitidas:
  - Suma (+)
  - Resta (-)
  - Multiplicación (*)
  - División (/)
  - Potenciación (^)
  - Módulo (%)

Validaciones:
  - El programa debe validar que el usuario ingrese
    correctamente los números y operaciones.
  - No se permite la división entre 0.

---------------------------------------------------------
                  EJEMPLO DE EJECUCIÓN
---------------------------------------------------------

Menú de opciones:
1. Realizar una nueva operación
2. Ver historial de operaciones
3. Salir

Seleccione una opción: 1

Ingrese el primer número: 5
Ingrese el segundo número: 3
Seleccione la operación (+, -, *, /, ^, %): *

Resultado: 5 * 3 = 15

¿Desea realizar otra operación? (s/n): s

Menú de opciones:
1. Realizar una nueva operación
2. Ver historial de operaciones
3. Salir

Seleccione una opción: 2

Historial de operaciones:
1. 5 * 3 = 15

Menú de opciones:
1. Realizar una nueva operación
2. Ver historial de operaciones
3. Salir

Seleccione una opción: 3

¡Gracias por usar la calculadora!
---------------------------------------------------------
"""

def inicio():
    while True:
        try:
            print("\nMenú de opciones:\n1.Realizar una nueva operación\n2.Ver historial de operacione\n3.Salir\n")
            decision = input("Seleccione una opción: ")
            if decision == 1:
                get_nums()
            elif decision == 2:
                history()      
            elif decision == 3:
                break

        except ValueError:
            print("ERROR: Por favor, ingrese 1, 2 o 3 como indica en el texto.")  

def get_nums():
    while True:
        try:
            num1 = int(input("Introduce el primer número: "))
            num2 = int(input("Introduce el segundo número: "))
            operation(num1, num2)
            if not confirmar():
                break

        except ValueError:
            print("ERROR: Por favor, ingrese un número entero válido.")  

def confirmar():
    while True:
        oper = input("¿Deseas realizar otra operación? (s/n): ").lower()
        if oper == "s":
            return True
        elif oper == "n":
            return False
        else:
            print("ERROR: Debes elegir 's' para sí o 'n' para no.")

def operation(num1, num2):
    while True:
        guardar = []
        oper = input("Selecciona la operación a realizar (+, -, *, /, ^, %): ")
        if oper == "+":
            suma = (f"Resultado: {num1} + {num2} = {num1 + num2}")
            print(suma)
            guardar.append(suma)
            history(guardar)

        elif oper == "-":
            resta = (f"Resultado: {num1} - {num2} = {num1 - num2}")
            print(resta)
            guardar.append(resta)
            history(guardar)
        elif oper == "*":
            multi = (f"Resultado: {num1} * {num2} = {num1 * num2}")
            print(multi)
            guardar.append(multi)
            history(guardar)
        elif oper == "/":
            if num2 == 0:
                print(f"ERROR: No se puede dividir entre cero.")
            else:
                division = (f"Resultado: {num1} / {num2} = {int((num1 / num2))}")
                print(division)
                guardar.append(division)
                history(guardar)
        elif oper == "^":
            potencia = (f"Resultado: {num1} ^ {num2} = {num1 ** num2}")
            print(potencia)
            guardar.append(potencia)
            history(guardar)
        elif oper == "%":
            porcentage = (f"Resultado: {num1}% * {num2} = {int((num2 / 100 * num1))}")
            print(porcentage)
            guardar.append(porcentage)
            history(guardar)
        else:
            print("ERROR: Operación no válida. Por favor, selecciona una de estas: +, -, *, /")
            continue

        break

def history(guardados):
    listado = []

    print("Historial de operaciones:")
    
    for i in guardados[2]:
        listado.append(guardados)
    
    print(listado)

inicio()
