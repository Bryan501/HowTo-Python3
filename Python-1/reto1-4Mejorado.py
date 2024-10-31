vocales_set = "aeiou"
consonantes_set = "bcdfghjklmnñpqrstvwxyz"

vocales = 0
consonantes = 0

text = input("Ingrese una palabra o frase: ").lower()

for i in text:
    if i in vocales_set:
        vocales += 1
    elif i in consonantes_set:
        consonantes += 1

print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")