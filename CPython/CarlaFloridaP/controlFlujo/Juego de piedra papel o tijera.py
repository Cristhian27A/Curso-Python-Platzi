# piedra, papel o tijera, para evaluar la entrada de dos jugadores, utilizar estructura condicionales para ver quien es el ganador
print("BIENVENIDO A EL JUEGO DE PIEDRA, PAPEL O TIJERA")

j1 = input("Ingrese el nombre del jugador 1: ")
j2 = input("Ingrese el nombre del jugador 2: ")

opciones = ['piedra', 'papel', 'tijera']

jugador1 = input(f"jugador {j1} Elige: piedra, papel o tijera: ")
if jugador1 not in opciones:
    print("Opcion no valida elige nuevamente")
    jugador1 = input(f"jugador {j1} Elige: piedra, papel o tijera: ")

jugador2 = input(f"jugador {j2} Elige: piedra, papel o tijera: ")
if jugador2 not in opciones:
    print("Opcion no valida elige nuevamente")
    jugador2 = input(f"jugador {j2} Elige: piedra, papel o tijera: ")

if jugador1 == jugador2:
    print("ES UN EMPATE")
elif (jugador1 == 'piedra' and jugador2 == 'tijera') or (jugador1 == 'papel' and jugador2 == 'piedra') or (jugador1 == 'tijera' and jugador2 == 'papel'):
    print(f"El jugador {j1} GANO")
else:
    print(f"{jugador2} GANO")