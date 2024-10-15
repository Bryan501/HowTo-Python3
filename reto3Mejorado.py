def get_nums():
    while True:
        try:
            num1 = int(input("Introduce el primer número: "))
            num2 = int(input("Introduce el segundo número: "))
            operation(num1, num2)
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
        oper = input("Selecciona la operación a realizar (+, -, *, /): ")
        if oper == "+":
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif oper == "-":
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif oper == "*":
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif oper == "/":
            if num2 == 0:
                print(f"ERROR: No se puede dividir entre cero.")
            else:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("ERROR: Operación no válida. Por favor, selecciona una de estas: +, -, *, /")
            continue

        if not confirmar():
            break
    return


get_nums()
