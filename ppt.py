import random
import time

def elige():
    print ("Selecciona: ")
    print ("Piedra, papel o tijera")
    eleccion = input()
    eleccion = eleccion.lower()

#Creamos una lista conlos tres elementos
opciones = ["piedra", "papel", "tijera"]
eleccion = ""
marcador_jugador1 = 0
marcador_jugador2 = 0

print("Bienvenido a nuestro juego de piedra, papel o tijera.")

jugador1 = input("Inserta tu nombre: ")
jugador2 = "La maquina"
time.sleep(.5)
print("Hola " + jugador1 + ". ¿Listo para jugar contra " + jugador2 + "?")

print ("Selecciona: ")
print ("Piedra, papel o tijera")
eleccion = input()
eleccion = eleccion.lower()

while eleccion != "piedra" and eleccion != "papel" and eleccion != "tijera":
    print("Solo puedes escojer piedra, papel o tijera:")
    eleccion = input()
    eleccion = eleccion.lower()

def eljuego():
    global eleccion
    global marcador_jugador1
    global marcador_jugador2
    maquina = random.choice(opciones)
    time.sleep(1)
    if eleccion == maquina:
        print("Ambos habeis elegido " + maquina + ". Intentemoslo otra vez.")
        time.sleep(1)
        print ("Selecciona: ")
        print ("Piedra, papel o tijera")
        eleccion = input()
        eleccion = eleccion.lower()
        eljuego()
    elif eleccion == "piedra" and maquina == "papel":
        print("Has elejido " + eleccion + ". " + jugador2 + " ha elegido " + maquina + ".")
        time.sleep(1)
        print(jugador2 + " ha ganado.")
        marcador_jugador2 = marcador_jugador2 + 1
        print(jugador1 + ": " + str(marcador_jugador1))
        print(jugador2 + ": " + str(marcador_jugador2))
    elif eleccion == "piedra" and maquina == "tijera":
        print("Has elejido " + eleccion + ". " + jugador2 + " ha elegido " + maquina + ".")
        time.sleep(1)
        print(jugador1 + ", has ganado.")
        marcador_jugador1 = marcador_jugador1 + 1
        print(jugador1 + ": " + str(marcador_jugador1))
        print(jugador2 + ": " + str(marcador_jugador2))
    elif eleccion == "papel" and maquina == "tijera":
        print("Has elejido " + eleccion + ". " + jugador2 + " ha elegido " + maquina + ".")
        time.sleep(1)
        print(jugador2 + " ha ganado.")
        marcador_jugador2 = marcador_jugador2 + 1
        print(jugador1 + ": " + str(marcador_jugador1))
        print(jugador2 + ": " + str(marcador_jugador2))
    elif eleccion == "papel" and maquina == "piedra":
        print("Has elejido " + eleccion + ". " + jugador2 + " ha elegido " + maquina + ".")
        time.sleep(1)
        print(jugador1 + ", has ganado.")
        marcador_jugador1 = marcador_jugador1 + 1
        print(jugador1 + ": " + str(marcador_jugador1))
        print(jugador2 + ": " + str(marcador_jugador2))
    elif eleccion == "tijera" and maquina == "piedra":
        print("Has elejido " + eleccion + ". " + jugador2 + " ha elegido " + maquina + ".")
        time.sleep(1)
        print(jugador2 + " ha ganado.")
        marcador_jugador2 = marcador_jugador2 + 1
        print(jugador1 + ": " + str(marcador_jugador1))
        print(jugador2 + ": " + str(marcador_jugador2))
    elif eleccion == "tijera" and maquina == "papel":
        print("Has elejido " + eleccion + ". " + jugador2 + " ha elegido " + maquina + ".")
        time.sleep(1)
        print(jugador1 + ", has ganado.")
        marcador_jugador1 = marcador_jugador1 + 1
        print(jugador1 + ": " + str(marcador_jugador1))
        print(jugador2 + ": " + str(marcador_jugador2))

    time.sleep(1)
    print("¿Quieres jugar otra vez?")
    repetir = input("y/n:  ")
    repetir = repetir.lower()
    if repetir == "n":
        print("Has ganado: " + str(marcador_jugador1) + " veces.")
        print(jugador2 + " ha ganado " + str(marcador_jugador2) + " veces.")
        print("Hasta la próxima.")
        time.sleep(2)
        exit()
    else: 
        time.sleep(1)
        print ("Selecciona: ")
        print ("Piedra, papel o tijera")
        eleccion = input()
        eleccion = eleccion.lower()
        time.sleep(1)
        eljuego()
        
eljuego()
