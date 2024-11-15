

import random


numero_secreto = random.randint(1,100)
cantidad_de_intentos = 0
cantidad_max = 10
adivinado =  False

print("Bienvenido al juego de adivinar")

while not adivinado and cantidad_de_intentos < cantidad_max:
    contador = input("Introduce un numero del 1 al 99: ")
    numero = int(contador)

    if numero == numero_secreto:
        print("Has adivinado")
        adivinado = True
    elif numero < numero_secreto:
        print("El numero es mayor")
    else:
        print("El numero es menor")
    
    cantidad_de_intentos += 1
if not cantidad_de_intentos < cantidad_max:
    print("Perdiste! Superaste los intentos")
