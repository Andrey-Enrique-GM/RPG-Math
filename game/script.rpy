
# Declara los personajes usados en el juego
define s = Character("Sayori", color = "#2F9BF7")
define ayame = Character("Ayame", color = "#d222f6")
define sasaki = Character("Sasaki", color = "#ec3737")
define akira = Character("Akira", color = "#1097db")

# El juego comienza aqui
label start:

    # Detener musica del menu antes de iniciar el juego
    stop music fadeout 1.0
    # Iniciar musica de fondo del juego
    play music "Doki Doki Literature Club! OST - Your Reality.mp3"

    # Muestra una imagen de fondo y aplica una transicion de oscuridad a color (no se como se llama)
    scene bg-inicio with fade

    # Muestra un personaje
    show ayame-neutral

    # Presenta las lineas del dialogo antes de elegir el mini juego
    ayame "¡Bienvenido al juego RPG-Math!"
    ayame "Mas exactamente un juego para practicar tu habilidad para resolver ejercicios de Matemáticas Computacionales."

    # Cambiar la expresion de Ayame a feliz
    hide ayame-neutral
    show ayame-bien

    ayame "¡Es hora de empezar a jugar!"
    ayame "¡Pero antes!"
    ayame "Elige uno de los minijuegos para comenzar."
    
    # Mostrar el menu de seleccion de minijuegos
    menu:
        "Simplificación de Jeroglíficos Fraccionarios (Algoritmo de euclides)":
            scene bg-euclides
            hide ayame-bien
            show sasaki-neutral at Position(xalign=1.0, yalign=1.0)
            show akira-neutral at Position(xalign=0.0, yalign=1.0)
            with fade
            jump AlgoritmoEuclides
            
        "El Enigma de los Ciclos Cósmicos (mcm - minimo comun multiplo)":
            scene bg-mcm
            hide ayame-bien
            show akira-neutral at Position(xalign=-0.2, yalign=1.0)
            with fade
            jump MinimoComunMultiplo

        "El Rompecabezas del Templo Antiguo (MCD - Maximo Comun Divisor)":
            scene bg-mcd
            hide ayame-bien
            show sasaki-neutral at Position(xalign=1.14, yalign=1.0)
            with fade
            jump MaximoComunDivisor

    return
