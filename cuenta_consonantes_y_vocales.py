
frase = input("Escribe una frase. ")

vocales = ["a", "e", "i", "o", "u"]

n_vocales = 0
n_consonantes = 0

for letra in frase:
    if letra in vocales:
        n_vocales += 1

    else:
        n_consonantes += 1

print(f"En la frase {frase} tienes: ")
print(f"Las vocales son {n_vocales}.")
print(f"Las consonantes son {n_consonantes}.")