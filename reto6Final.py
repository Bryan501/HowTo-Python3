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

import sys

historial = []

def inicio():
    while True:
        try:
            print("\n---------------------------------\n         MENÚ DE OPCIONES         \n---------------------------------\n1.Realizar una nueva operación\n2.Ver historial de operaciones\n3.Salir\n")
            decision = int(input("Seleccione una opción: "))
            if decision == 1:
                get_nums()
            elif decision == 2:
                history()
            elif decision == 3:
                print("¡Gracias por usar la calculadora!")
                sys.exit()
            else:
                print("ERROR: Opción no valida.")
        except ValueError:
            print("ERROR: Por favor, ingrese 1, 2 o 3 como indica en el texto.")

def get_nums():
    while True:
        try:
            num1 = int(input("Introduce el primer número: "))
            num2 = int(input("Introduce el segundo número: "))
            resultado = operation(num1, num2)
            print(resultado)
            historial.append(resultado)
            if not confirmar():
                sys.exit()
        except ValueError:
            print("ERROR: Por favor, ingrese un número entero válido.")

def confirmar():
    while True:
        oper = input("¿Deseas realizar otra operación? (s/n): ").lower()
        if oper == "s":
            return True
        elif oper == "n":
            return inicio()
        else:
            print("ERROR: Debes elegir 's' para sí o 'n' para no.")

def operation(num1, num2):
    while True:
        oper = input("Selecciona la operación a realizar (+, -, *, /, ^, %): ")
        if oper == "+":
            return f"{num1} + {num2} = {num1 + num2}"
        elif oper == "-":
            return f"{num1} - {num2} = {num1 - num2}"
        elif oper == "*":
            return f"{num1} * {num2} = {num1 * num2}"
        elif oper == "/":
            if num2 == 0:
                print(f"ERROR: No se puede dividir entre cero.")
            else:
                return (f"Resultado: {num1} / {num2} = {int((num1 / num2))}")
        elif oper == "^":
            return f"{num1} ^ {num2} = {num1 ** num2}"
        elif oper == "%":
            return f"{num1} % {num2} = {num1 % num2}"
        else:
            print("ERROR: Operación no válida.")
            continue

def history():
    print("\n---------------------------------\n   HISTORIAL DE OPERACIONES         \n---------------------------------\n1.Realizar una nueva operación\n2.Ver historial de operaciones\n3.Salir\n")
    if historial:
        for i, operacion in enumerate(historial, 1):
            print(f"{i}. {operacion}")
    else:
        print("No hay operaciones en el historial.")

    input("\nPresiona Enter para regresar al menú principal.")
inicio()
