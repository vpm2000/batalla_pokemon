mi_lista = []
input_usuario = ""

while input_usuario != "FIN":
    input_usuario = input("¿Que quieres comprar?: (escrube FIN para salir) ")
    if input_usuario != "FIN":
    mi_lista.append(input_usuario)

largo_lista = len(mi_lista)
indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1

print("Esta es la lista de la compra.")