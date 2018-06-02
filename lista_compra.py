mi_lista = []
input_usuario = ""

while input_usuario != "FIN":
    input_usuario = input("¿Que quieres comprar?: (escrube FIN para salir) ")
    if input_usuario != "FIN":
        mi_lista.append(input_usuario)

for item in mi_lista:
    print(f"Tengo que comprar {input_usuario}")

print("Esta es la lista de la compra.")