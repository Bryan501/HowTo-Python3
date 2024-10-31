"""
----------------------------------------------------------------------------------
FUNCIÓN: analizar_lista_numeros
----------------------------------------------------------------------------------
Descripción:
  Esta función recibe una lista de números y calcula la suma, el promedio, el número
  máximo y el número mínimo de la lista.

Parámetros:
  lista (list) : Lista de números enteros o flotantes.

Retorno:
  dict : Diccionario que contiene la suma, el promedio, el máximo y el mínimo de la lista.

Ejemplo:
  Entrada: [5, 2, 9, 1, 7, 4]
  Salida: {'suma': 28, 'promedio': 4.67, 'maximo': 9, 'minimo': 1}
----------------------------------------------------------------------------------
"""

def analizar_numeros(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    maximo = max(lista)
    minimo = min(lista)

    resultado = {
        "suma": suma,
        "promedio": round(promedio, 2),
        "maximo": maximo,
        "minimo": minimo,
    }

    return resultado

def obtener_numeros():
    lista1 = []
    while len(lista1) < 5:
        try:
            num = float(input("Pomn los números para lalista (entero o no. máximo 5): "))
            lista1.append(num)
        except ValueError:
            print("ERROR: Debes de ingresar un número.")
    return lista1

if __name__ == "__main__":
    lista = obtener_numeros()
    resultado_final = analizar_numeros(lista)
    print("Resultado:", resultado_final)
