
label AlgoritmoEuclides:

    stop music fadeout 1.0
    play music "Katawa Shoujo OST - Ease.mp3"

    python:
        
        import random

        # -------------------------
        # FUNCIONES DE LoGICA
        # -------------------------

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def simplify_fraction(n, d):
            if d == 0:
                return n, d
            g = gcd(n, d)
            return n // g, d // g

        def generate_incorrect_option(correct_n, correct_d, level):
            while True:
                mod = max(1, level // 2 + 1)
                n = correct_n + random.choice([-mod, -1, 1, mod])
                d = correct_d + random.choice([-mod, -1, 1, mod])

                if n > 0 and d > 0:
                    sn, sd = simplify_fraction(n, d)
                    if (sn, sd) != (correct_n, correct_d):
                        return (n, d)

        def generate_question(level):
            min_val = 2 + (level - 1) * 3
            max_val = 50 + (level - 1) * 10

            while True:
                n = random.randint(min_val, max_val)
                d = random.randint(min_val, max_val)
                if d != 0 and n > 1 and d > 1:
                    break

            correct_n, correct_d = simplify_fraction(n, d)

            opts = [(correct_n, correct_d)]
            opt1 = generate_incorrect_option(correct_n, correct_d, level)
            opt2 = generate_incorrect_option(correct_n, correct_d, level)

            while opt2 == opt1 or opt2 == (correct_n, correct_d):
                opt2 = generate_incorrect_option(correct_n, correct_d, level)

            opts.append(opt1)
            opts.append(opt2)
            random.shuffle(opts)

            return n, d, opts, (correct_n, correct_d)


    # -------------------------
    # VARIABLES DEL JUEGO
    # -------------------------
    default level_ae = 1
    default current_original_n_ae = 0
    default current_original_d_ae = 0
    default current_options_ae = []
    default correct_answer_ae = (0, 0)
    default last_message_ae = ""


    # -------------------------
    # PANTALLA DE PREGUNTA
    # -------------------------
    screen question_screen_ae():
        modal True
        tag question

        frame:
            xalign 0.5
            yalign 0.5
            has vbox

            text "Nivel [level_ae]" size 40
            text "Simplifica: [current_original_n_ae]/[current_original_d_ae]" size 55

            for i, pair in enumerate(current_options_ae):
                $ num, den = pair
                textbutton "[num]/[den]":
                    action Function(handle_choice_ae, i)
                    xminimum 300
                    yminimum 60

            textbutton "Salir al menu principal":
                action Return()


    # -------------------------
    # MANEJO DE OPCIONES
    # -------------------------
    init python:
        def handle_choice_ae(index):
            global last_message_ae, level_ae

            selected = current_options_ae[index]

            if selected == correct_answer_ae:
                last_message_ae = "¡Correcto! Avanzas al siguiente nivel."
                level_ae += 1
                # Reproducir sonido de acierto y una sayori feliz :D
                renpy.play("bien.wav")
                renpy.hide("sayori-neutral")
                renpy.show("sayori-bien", at_list=[Position(xalign=0.9, yalign=1.0)])

            else:
                last_message_ae = "Incorrecto."
                renpy.play("mal.wav")
                renpy.hide("sayori-neutral")
                renpy.show("sayori-mal", at_list=[Position(xalign=0.9, yalign=1.0)])

            renpy.jump("resultado_ae")


    # -------------------------
    # LABEL PRINCIPAL
    # -------------------------
    label play_ae:

        hide sayori-bien
        show sayori-neutral at Position(xalign=0.9, yalign=1.0)
        # Generar pregunta nueva
        $ current_original_n_ae, current_original_d_ae, current_options_ae, correct_answer_ae = generate_question(level_ae)

        call screen question_screen_ae

        return


    # -------------------------
    # RESULTADO
    # -------------------------
    label resultado_ae:

        if last_message_ae == "¡Correcto! Avanzas al siguiente nivel.":
            s "[last_message_ae]"
            jump play_ae
        else:
            s "[last_message_ae]"
            s "La respuesta correcta era: [correct_answer_ae[0]]/[correct_answer_ae[1]]"

            menu:
                s "¿Que quieres hacer?"

                "Reintentar (volver a Nivel 1)":
                    $ level_ae = 1
                    jump play_ae

                "Salir al menu principal":
                    return
