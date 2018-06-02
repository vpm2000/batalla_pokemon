
texto = input("Introduce un texto: ")

mayusculas = len([c for c in texto if c.isupper()])
minusculas = len([c for c in texto if c.islower()])
numeros = len([c for c in texto if c.isdigit()])

print(f"En la frase {texto} contiene lo siguiente: ")
print(f"Mayusculas = {mayusculas}")
print(f"Minusclas = {minusculas}")
print(f"Numeros = {numeros}")