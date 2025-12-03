
label MaximoComunDivisor:

    stop music fadeout 1.0
    play music "Doki Doki Literature Club! OST - Dreams Of Love and Literature.mp3"

    python:

        import random

        # -------------------------
        # FUNCIONES DE LÓGICA
        # -------------------------

        # MCD
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Generar opciones incorrectas
        def generate_incorrect_gcd_option(correct_gcd, num1, num2):
            while True:
                strategy = random.randint(0,2)
                option = correct_gcd

                if strategy == 0:
                    option = correct_gcd + random.choice([-2,-1,1,2])
                    if option <= 0:
                        option = correct_gcd + abs(random.choice([1,2]))
                elif strategy == 1:
                    factors = [i for i in range(1, min(num1,num2)+1)
                    if num1 % i == 0 and num2 % i == 0 and i != correct_gcd]
                    if factors:
                        option = random.choice(factors)
                    else:
                        option = correct_gcd + random.choice([3,4])
                else:
                    option = random.randint(1, min(num1,num2)+5)

                if option > 0 and option != correct_gcd:
                    return option

        # Generar pregunta por nivel
        def generate_question(level):
            min_val = 10 + (level-1)*5
            max_val = 50 + (level-1)*10
            num1 = random.randint(min_val, max_val)
            num2 = random.randint(min_val, max_val)
            correct = gcd(num1, num2)

            opts = [correct]
            opts.append(generate_incorrect_gcd_option(correct, num1, num2))
            incorrect2 = generate_incorrect_gcd_option(correct, num1, num2)
            while incorrect2 in opts:
                incorrect2 = generate_incorrect_gcd_option(correct, num1, num2)
            opts.append(incorrect2)

            random.shuffle(opts)
            return num1, num2, opts, correct

    # -------------------------
    # VARIABLES DEL JUEGO
    # -------------------------
    default level_mcd = 1
    default current_num1_mcd = 0
    default current_num2_mcd = 0
    default current_options_mcd = []
    default correct_answer_mcd = 0
    default last_message_mcd = ""

    # -------------------------
    # PANTALLA DE PREGUNTA
    # -------------------------
    screen question_screen_mcd():
        modal True
        tag question

        frame:
            xalign 0.5
            yalign 0.5
            has vbox

            text "Nivel [level_mcd]" size 40
            text "Encuentra el MCD de: [current_num1_mcd] y [current_num2_mcd]" size 35
            text "¿Cuál es el lado de baldosa más grande que encaja?" size 30

            for i, val in enumerate(current_options_mcd):
                textbutton "[val]":
                    action Function(handle_choice_mcd, i)
                    xminimum 300
                    yminimum 60

            textbutton "Salir al menú principal":
                action Return()

    # -------------------------
    # MANEJO DE OPCIONES
    # -------------------------
    init python:
        def handle_choice_mcd(index):
            global last_message_mcd, level_mcd

            selected = current_options_mcd[index]

            if selected == correct_answer_mcd:
                last_message_mcd = "¡Correcto! Avanzas al siguiente nivel."
                level_mcd += 1
                renpy.play("bien.wav")
                renpy.hide("sayori-neutral")
                renpy.show("sayori-bien", at_list=[Position(xalign=1.15, yalign=1.0)])
            else:
                last_message_mcd = "Incorrecto."
                renpy.play("mal.wav")
                renpy.hide("sayori-neutral")
                renpy.show("sayori-mal", at_list=[Position(xalign=1.15, yalign=1.0)])

            renpy.jump("resultado_mcd")

    # -------------------------
    # LABEL PRINCIPAL
    # -------------------------
    label play_mcd:

        hide sayori-bien
        show sayori-neutral at Position(xalign=1.15, yalign=1.0)
        $ current_num1_mcd, current_num2_mcd, current_options_mcd, correct_answer_mcd = generate_question(level_mcd)
        call screen question_screen_mcd
        return

    # -------------------------
    # RESULTADO
    # -------------------------
    label resultado_mcd:

        if last_message_mcd == "¡Correcto! Avanzas al siguiente nivel.":
            s "[last_message_mcd]"
            jump play_mcd
        else:
            s "[last_message_mcd]"
            s "El MCD correcto era: [correct_answer_mcd]"
            menu:
                s "¿Qué quieres hacer?"

                "Reintentar (volver a Nivel 1)":
                    $ level_mcd = 1
                    jump play_mcd

                "Salir al menú principal":
                    return
