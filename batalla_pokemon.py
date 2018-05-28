pokemon_elegido = input("Contra que pokemon quieres luchar (Squertle / Charmander / Bulbasur): ")

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_elegido == "Squertle":
    vida_enemigo = 90
    nombre_pokemon = "Squertle"
    ataque_pokemon = 8

elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    nombre_pokemon = "Charmander"
    ataque_pokemon = 7

elif pokemon_elegido == "Bulbasur":
    vida_enemigo = 100
    nombre_pokemon = "Bulbasur"
    ataque_pokemon = 10

print("{} tiene {} de vida".format(nombre_pokemon, vida_enemigo))

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque quieres usar? (Chispazo / Bola voltio)")

    if ataque_elegido == "Chispazo":
        print("Pikachu te hace un ataque de 10 de daño")
        vida_enemigo -= 10
    elif ataque_elegido == "Bola voltio":
        print("Pikachu te hace un ataque de 12 de daño")
        vida_enemigo -= 12

    print("La vida de {} ahora es de {}".format(nombre_pokemon, vida_enemigo))

    print("{} te hace un ataque de {} de daño".format(nombre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon

    print("La vida de Pikachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Pikachu has ganado!")
elif vida_pikachu <= 0:
    print("¡{} ha ganado!".format(pokemon_elegido))

print("El combate ha terminado")