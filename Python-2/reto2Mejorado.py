
def filtrar_ordenar_lista(lista, umbral):
    resultado = []

    for i in lista:
        if i >= umbral:
            resultado.append(i)
    resultado.sort()
    return resultado

def obtener_numeros():
    lista = []
    while len(lista) < 5:
        try:
            num = int(input("Pon los números para la lista: "))
            lista.append(num)
        except ValueError:
            print("ERROR: Debes ingresar un número entero.")
    return lista

if __name__ == "__main__":
    lista = obtener_numeros()

    try:
        umbral = int(input("Pon el umbral que prefieras: "))
    except ValueError:
        print("ERROR: Debes ingresar un número entero.")

    resultado_final = filtrar_ordenar_lista(lista, umbral)
    print("Resultado:", resultado_final)
