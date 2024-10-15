"""
-------------------------------------------------
            CALCULADORA BÁSICA EN PYTHON
-------------------------------------------------
Descripción:
  Este programa es una calculadora sencilla que permite
  realizar operaciones básicas entre dos números. El
  usuario podrá elegir entre las siguientes operaciones:

  - Suma (+)
  - Resta (-)
  - Multiplicación (*)
  - División (/)
  
  El programa pedirá al usuario que ingrese dos números 
  y seleccione la operación a realizar. Además, maneja el
  error de división por cero y muestra un mensaje adecuado
  si el usuario introduce una operación no válida.

Instrucciones:
  1. Introduce el primer número.
  2. Introduce el segundo número.
  3. Selecciona la operación a realizar (+, -, *, /).
  4. El programa mostrará el resultado de la operación.
  5. Podrás decidir si deseas realizar otra operación.

Ejemplo de Ejecución:
  Introduce el primer número: 10
  Introduce el segundo número: 5
  Elige una operación (+, -, *, /): /
  El resultado es: 2.0
  ¿Deseas realizar otra operación? (s/n): s

  Introduce el primer número: 6
  Introduce el segundo número: 0
  Elige una operación (+, -, *, /): /
  ERROR: No se puede dividir entre cero.
-------------------------------------------------
"""

def get_nums():
    try:
        num1 = int(input("Introdueix el primer número: "))
        if type(num1) != int:
            pass  
        else:
            num2 = int(input("Introdueix el segón número: "))
            return operation(num1, num2)

    except ValueError:
        print("ERROR: Por favor, ingrese un número entero")  

def confirmar(oper):
    if oper == "s":
        return get_nums()
    elif oper == "n":
        return False
    else:
        print("Debes de elegir sí o no, añadiendo s/n ")


def operation(num1, num2):
    while True:
        try:
            oper = input("Selecciona la operación a realizar (+, -, *, /): ")
            if type(oper) != str:
                pass  
            else:
                if oper == "+":
                    sumar = num1 + num2
                    print(sumar)
                elif oper == "-":
                    restar = num1 - num2
                    print(restar)
                elif oper == "*":
                    multiplicar = num1 * num2
                    print(multiplicar)
                elif oper == "/":
                    if num2 == 0:
                         print(f"ERROR: No se puede dividir entre cero el número {num1}")
                         break
                    else:
                        dividir = num1 / num2
                        print(dividir)
            
            oper = input("¿Deseas realizar otra operación? (s/n): ")
            
            if confirmar(oper) == True:
                return confirmar(oper)
            else:
                break

        except ValueError:
            print("ERROR: Por favor, ingrese un operador correcto ")  

get_nums()
