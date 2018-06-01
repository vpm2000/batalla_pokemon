print("¿Que operacion desea hacer?")
print("a) Sumar")
print("b) Restar")
print("c) Multiplicar")
print("d) Dividir")

opcion = input('Elija una opcion ---> ')

numero = int(input('Introduce un numero ---> '))
numero2 = int(input('Introduce otro numero ---> '))

if opcion == 'a':
    suma = numero + numero2
    print("El resultado es {}".format(suma))
if opcion == 'b':
    resta = numero - numero2
    print("El resultado es {}".format(resta))
if opcion == 'c':
    multi = numero * numero2
    print("El resultado es {}".format(multi))
if opcion == 'd':
    divi = numero / numero2
    print("El resultado es {}".format(divi))