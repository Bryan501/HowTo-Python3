def filtrar_ordenar_lista(lista, umbral):
    resultado = []

    for i in lista:
        if i >= umbral:
            resultado.append(i)  # Agregar a resultado si cumple con el umbral
    return resultado

# Aquí puedes probar la función
if __name__ == "__main__":
    # Lista de prueba
    lista_prueba = []
    repes = 0

    # Ingresar números a la lista
    while repes < 5:
        num = int(input("Pon los números para la lista: "))  # Ingreso del usuario
        lista_prueba.append(num)
        repes += 1

    umbral = int(input("Pon el umbral que prefieras: "))  # Ingreso del umbral

    # Llamar a la función con los parámetros necesarios
    resultado_final = filtrar_ordenar_lista(lista_prueba, umbral)

    print("Resultado:", resultado_final)  # Mostrar el resultado
