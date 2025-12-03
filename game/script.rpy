
# Declara los personajes usados en el juego
define s = Character("Sayori", color = "#2F9BF7")

# El juego comienza aqui
label start:

    # Detener musica del menu antes de iniciar el juego
    stop music fadeout 1.0
    # Iniciar musica de fondo del juego
    play music "Doki Doki Literature Club! OST - Your Reality.mp3"

    # Muestra una imagen de fondo
    scene bg-aula

    # Muestra un personaje
    show sayori-neutral

    # Presenta las lineas del dialogo antes de elegir el mini juego
    s "¡Bienvenido al juego RPG-Math!"
    s "Mas exactamente un juego para practicar tu habilidad en Matematicas Computacionales."

    # Cambiar la expresion de Sayori a feliz
    hide sayori-neutral
    show sayori-bien

    s "¡Es hora de empezar a jugar!"
    s "Elige uno de los minijuegos para comenzar."

    # Mostrar el menu de seleccion de minijuegos
    menu:
        "Simplificación de Jeroglíficos Fraccionarios (Algoritmo de euclides)":
            hide sayori-bien
            show sayori-neutral at Position(xalign=0.9, yalign=1.0)
            jump AlgoritmoEuclides

        "El Enigma de los Ciclos Cósmicos (mcm - minimo comun multiplo)":
            hide sayori-bien
            show sayori-neutral at Position(xalign=0.9, yalign=1.0)
            jump MinimoComunMultiplo

        "El Rompecabezas del Templo Antiguo (MCD - Maximo Comun Divisor)":
            hide sayori-bien
            show sayori-neutral at Position(xalign=0.9, yalign=1.0)
            jump MaximoComunDivisor

    return
