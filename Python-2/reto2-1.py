"""
----------------------------------------------------------------------------------
FUNCIÓN: filtrar_ordenar_lista
----------------------------------------------------------------------------------
Descripción:
  Esta función recibe una lista de números y un valor umbral.
  Filtra los valores de la lista para que solo queden aquellos mayores o iguales al umbral,
  y luego los ordena en orden ascendente.

Parámetros:
  lista   (list) : Lista de números enteros o flotantes.
  umbral  (int/float) : Valor umbral usado para filtrar la lista.

Retorno:
  list : Nueva lista ordenada de números mayores o iguales al umbral.

Ejemplo:
  Entrada: [5, 2, 9, 1, 7, 4], umbral=5
  Salida: [5, 7, 9]
----------------------------------------------------------------------------------
"""

def filtrar_ordenar_lista(lista, umbral):
    resultado = []

    for i in lista:
        if i >= umbral:
            resultado.append(i)
    resultado.sort()
    return resultado

if __name__ == "__main__":
    lista = []
    repes = 0

    while repes < 5:
        num = int(input("Pon los números para la lista: "))
        lista.append(num)
        repes += 1

    umbral = int(input("Pon el umbral que prefieras: "))

resultado_final = filtrar_ordenar_lista(lista, umbral)
print("Resultado:", resultado_final)
