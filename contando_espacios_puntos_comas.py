
texto = input("Intrduce una frase: ")

n_espacios = 0
espacios = " "

n_puntos = 0
puntos = "."

n_comas = 0
comas = ","


for letra in texto:
    if letra in espacios:
        n_espacios += 1
    elif letra in puntos:
        n_puntos += 1
    elif letra in comas:
        n_comas += 1



print("Tu frase tiene: ")
print(f"espacios = {n_espacios}")
print(f"puntos = {n_puntos}")
print(f"comas = {n_comas}")