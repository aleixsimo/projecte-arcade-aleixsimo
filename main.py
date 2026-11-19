import jocs

def main():
    # Bucle principal que manté el programa en marxa
    while True:
        # 1. Mostrem el menú a l'usuari
        print("\n--- BENVINGUT/DA AL MINI ARCADE ---")
        print("1. Jugar a Pedra, Paper, Tisora")
        print("2. Jugar a Endevinar el Número")
        print("S. Sortir")
        
        # 2. Demanem quina opció vol triar
        opcio = input("Tria una opció: ").strip().upper()
        
        # 3. Gestionem l'opció triada
        if opcio == "1":
            print("\nIniciant Pedra, Paper, Tisora...")
            jocs.janken()
            
        elif opcio == "2":
            print("\nIniciant Endevinar el Número...")
            jocs.nana()
            
        elif opcio == "S":
            # Missatge de comiat i trencament del bucle
            print("\nGràcies per jugar al Mini Arcade! Fins aviat!")
            break
            
        else:
            # Si l'usuari escriu qualsevol altra cosa
            print("\n[ERROR] Opció no vàlida. Si us plau, tria 1, 2 o S.")

# Aquesta línia assegura que la funció main() s'executi només
# quan obrim aquest fitxer directament
if __name__ == "__main__":
    main()