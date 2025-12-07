
label MinimoComunMultiplo:

    stop music fadeout 1.0
    play music "Doki Doki Literature Club! OST - Ohayou Sayori!.mp3"

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

        # MCM
        def lcm(a, b):
            if a == 0 or b == 0:
                return 0
            return abs(a * b) // gcd(a, b)

        # Calcular MCM de una lista
        def synchronize_cycles(cycles):
            if not cycles:
                return 0
            result = cycles[0]
            for c in cycles[1:]:
                result = lcm(result, c)
            return result

        # Generar opciones incorrectas
        def generate_incorrect_option(correct, cycles):
            while True:
                choice = random.randint(0,2)
                option = correct
                if choice == 0:
                    # Pequeña variacion
                    mods = [-10,-5,5,10]
                    option = correct + random.choice([m for m in mods if correct + m > 0])
                elif choice == 1 and cycles:
                    # Factor o multiplo
                    c = random.choice(cycles)
                    if correct % c == 0 and correct // c > 1:
                        option = correct // c
                    else:
                        option = c * random.randint(2,4)
                else:
                    # Subconjunto de ciclos
                    if len(cycles) > 1:
                        subset = random.sample(cycles, random.randint(1,len(cycles)-1))
                        option = synchronize_cycles(subset)
                    else:
                        option = correct + random.randint(1,10)
                if option > 0 and option != correct:
                    return option

        # Generar pregunta por nivel
        def generate_question(level):
            min_val = 2 + (level-1)*2
            max_val = 15 + (level-1)*5
            max_cycles = min(5, 2 + level//3)
            num_cycles = random.randint(2, max_cycles)
            cycles = [random.randint(min_val, max_val) for _ in range(num_cycles)]
            correct = synchronize_cycles(cycles)
            opts = [correct]
            opts.append(generate_incorrect_option(correct, cycles))
            opts.append(generate_incorrect_option(correct, cycles))
            random.shuffle(opts)
            return cycles, opts, correct


    # -------------------------
    # VARIABLES DEL JUEGO
    # -------------------------
    default level_mcm = 1 # Nivel inicial
    default current_cycles_mcm = [] # Ciclos actuales de los dispositivos
    default current_options_mcm = [] # Opciones actuales para la pregunta
    default correct_answer_mcm = 0
    default last_message_mcm = ""

    # -------------------------
    # PANTALLA DE PREGUNTA
    # -------------------------
    screen question_screen_mcm():
        modal True
        tag question

        frame:
            xalign 0.5
            yalign 0.5
            has vbox

            text "Nivel [level_mcm]" size 40
            text "Ciclos de los dispositivos: [current_cycles_mcm]" size 35
            text "¿Después de cuántas unidades se sincronizan?" size 40

            for i, val in enumerate(current_options_mcm):
                textbutton "[val]":
                    action Function(handle_choice_mcm, i)
                    xminimum 300
                    yminimum 60

            textbutton "Salir al menu principal":
                action Return()


    # -------------------------
    # MANEJO DE OPCIONES
    # -------------------------
    init python:
        def handle_choice_mcm(index):
            global last_message_mcm, level_mcm

            selected = current_options_mcm[index]

            if selected == correct_answer_mcm:
                last_message_mcm = "¡Muy bien! Avanzaste al siguiente nivel."
                level_mcm += 1
                renpy.play("bien.wav")
                renpy.hide("akira-neutral")
                renpy.show("akira-bien", at_list=[Position(xalign=-0.2, yalign=1.0)])
            else:
                last_message_mcm = "Incorrecto, ¿Error de dedo?"
                renpy.play("mal.wav")
                renpy.hide("akira-neutral")
                renpy.show("akira-mal", at_list=[Position(xalign=-0.2, yalign=1.0)])

            renpy.jump("resultado_mcm")


    # -------------------------
    # LABEL PRINCIPAL
    # -------------------------
    label play_mcm:

        hide akira-bien
        show akira-neutral at Position(xalign=-0.2, yalign=1.0)
        $ current_cycles_mcm, current_options_mcm, correct_answer_mcm = generate_question(level_mcm)
        call screen question_screen_mcm
        return


    # -------------------------
    # RESULTADO
    # -------------------------
    label resultado_mcm:

        # Mostrar resultado
        if last_message_mcm == "¡Muy bien! Avanzaste al siguiente nivel.":
            akira "[last_message_mcm]"
            jump play_mcm
        else:
            akira "[last_message_mcm]"
            akira "La respuesta correcta era: [correct_answer_mcm]"
            menu:
                akira "¿Qué quieres hacer?"

                "Reintentar (volver a Nivel 1)":
                    $ level_mcm = 1
                    hide akira-mal
                    jump play_mcm

                "Salir al menu principal":
                    return
