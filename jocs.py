import robot
import random

# Joc de pedra, paper, tisora
def janken():
    # 1. Creem una instància del robot per poder jugar contra ell
    bot = robot.robot()
    
    # 2. Variables locals per guardar el marcador
    punts_jugador = 0
    punts_robot = 0
    ronda_actual = 1
    
    print("\n--- PEDRA, PAPER, TISORA ---")
    print("Tria la modalitat de joc:")
    print("1. El primer que arribi a 3 victòries")
    print("2. Jugar un total de 5 rondes")
    
    # Validem que l'usuari triï una opció vàlida (1 o 2)
    mode = ""
    while mode not in ["1", "2"]:
        mode = input("Selecciona modalitat (1 o 2): ").strip()
        if mode not in ["1", "2"]:
            print("Opció incorrecta. Introdueix 1 o 2.")

    # 3. Bucle de la partida
    partida_en_curs = True
    while partida_en_curs:
        print(f"\n--- Ronda {ronda_actual} ---")
        print(f"Marcador actual -> Tu: {punts_jugador} | Robot: {punts_robot}")
        
        # Demanem la jugada a l'usuari i la validem
        jugada_usuari = input("Tria (pedra, paper, tisora): ").strip().lower()
        while jugada_usuari not in ["pedra", "paper", "tisora"]:
            print("Jugada invàlida! Has d'escriure: pedra, paper o tisora.")
            jugada_usuari = input("Tria (pedra, paper, tisora): ").strip().lower()
            
        # Obtenim la jugada del robot
        jugada_bot = bot.playing()
        print(f"El robot ha tret: {jugada_bot}")
        
        # 4. Comparem les jugades de la ronda
        if jugada_usuari == jugada_bot:
            print("-> Empat en aquesta ronda!")
            
        elif (jugada_usuari == "pedra" and jugada_bot == "tisora") or \
             (jugada_usuari == "paper" and jugada_bot == "pedra") or \
             (jugada_usuari == "tisora" and jugada_bot == "paper"):
            print("-> Has guanyat aquesta ronda!")
            punts_jugador += 1
            
        else:
            print("-> El robot guanya aquesta ronda!")
            punts_robot += 1
            
        ronda_actual += 1

        # 5. Comprovem si la partida s'ha d'acabar segons el mode triat
        if mode == "1":
            # El primer a 3 victòries
            if punts_jugador == 3 or punts_robot == 3:
                partida_en_curs = False
                
        elif mode == "2":
            # 5 rondes fixes (la ronda_actual ja val 6 quan n'hem jugat 5)
            if ronda_actual > 5:
                partida_en_curs = False

    # 6. Resultat final de la partida
    print("\n===============================")
    print(f"RESULTAT FINAL: Tu {punts_jugador} - {punts_robot} Robot")
    if punts_jugador > punts_robot:
        print("Felicitats! Has guanyat la partida!")
    elif punts_robot > punts_jugador:
        print("El robot guanya la partida...")
    else:
        print("La partida ha acabat en empat!")
    print("===============================\n")

# Joc de endevinar el número

def nana():
    # 1. Generem el número secret entre 1 i 100
    numero_secret = random.randint(1, 100)
    intents = 0
    endevinat = False
    
    print("\n--- ENDEVINA EL NÚMERO ---")
    print("He pensat un número entre 1 i 100. Pots endevinar quin és?")
    
    # 2. Bucle fins que l'usuari encerti
    while not endevinat:
        entrada = input("\nIntrodueix el teu número: ").strip()
        
        # 3. Validem que realment hagi escrit un número enter
        try:
            intent_usuari = int(entrada)
        except ValueError:
            print("[AVÍS] Has d'introduir un número enter vàlid!")
            continue  # Torna a l'inici del while sense comptar com a intent
            
        intents += 1
        
        # 4. Comparem el número i donem pistes
        if intent_usuari < numero_secret:
            print("Massa baix! El número secret és més gran.")
        elif intent_usuari > numero_secret:
            print("Massa alt! El número secret és més petit.")
        else:
            # L'ha encertat!
            endevinat = True
            print("\nFelicitats! Has endevinat el número!")
            print(f"Número secret: {numero_secret}")
            print(f"Has necessitat un total de {intents} intents.")

    print("------------------------------------------\n")