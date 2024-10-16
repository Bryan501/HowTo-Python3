"""
-------------------------------------------------
       CONTADOR DE VOCALES Y CONSONANTES
-------------------------------------------------
Descripción:
  Este programa cuenta cuántas vocales y cuántas
  consonantes hay en una palabra o frase introducida
  por el usuario. Los espacios, números y símbolos
  especiales no se tienen en cuenta en el conteo.
  
Instrucciones:
  1. Introduce una palabra o frase.
  2. El programa calculará el número de vocales y
     consonantes en la palabra/frase.

Ejemplo de ejecución:
    Ingrese una palabra o frase: Hola Mundo!
    Vocales: 4
    Consonantes: 5
-------------------------------------------------
"""

abc = "abcdefghijklmnñopqrstuvwxyz"
vocales = 0
consonantes = 0

text = input("Ingrese una palabra o frase: ")
text_lower = text.lower()

for i in text_lower:
    if i == "a" or  i == "e" or  i == "i" or  i == "o" or  i == "u":
        vocales += 1
    elif  i == "b" or i == "c" or i == "d" or  i == "f" or  i == "g" or  i == "h" or  i == "j" or  i == "k" or i == "l" or  i == "m" or  i == "n" or  i == "ñ" or  i == "p" or  i == "q" or  i == "r" or  i == "s" or  i == "t" or  i == "v" or  i == "w" or  i == "x" or  i == "y" or  i == "z":
        consonantes += 1

print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")