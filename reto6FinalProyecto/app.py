import sys
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

historial = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        num1 = int(request.form.get("num1"))
        num2 = int(request.form.get("num2"))
        oper = request.form.get("operacion")
        resultado = operation(num1, num2, oper)
        historial.append(resultado)
        return redirect(url_for("index"))
    return render_template("index.html", historial=historial)

def operation(num1, num2, oper):
    if oper == "+":
        return f"{num1} + {num2} = {num1 + num2}"
    elif oper == "-":
        return f"{num1} - {num2} = {num1 - num2}"
    elif oper == "*":
        return f"{num1} * {num2} = {num1 * num2}"
    elif oper == "/":
        if num2 == 0:
            return "ERROR: No se puede dividir entre cero."
        else:
            return f"{num1} / {num2} = {num1 / num2}"
    elif oper == "^":
        return f"{num1} ^ {num2} = {num1 ** num2}"
    elif oper == "%":
        return f"{num1} % {num2} = {num1 % num2}"
    else:
        return "ERROR: Operación no válida."

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
            oper = input("Selecciona la operación a realizar (+, -, *, /, ^, %): ")
            resultado = operation(num1, num2, oper)
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
            return False
        else:
            print("ERROR: Debes elegir 's' para sí o 'n' para no.")

def history():
    print("\n---------------------------------\n   HISTORIAL DE OPERACIONES         \n---------------------------------\n")
    if historial:
        for i, operacion in enumerate(historial, 1):
            print(f"{i}. {operacion}")
    else:
        print("No hay operaciones en el historial.")
    input("\nPresiona Enter para regresar al menú principal.")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
