def press_enter():
    input("\nAppuie sur Entrée pour continuer...")

def ask_choice(options):
    #Demande au joueur de saisir une option valide.
    #Ne montre pas les options. Si l'entrée est invalide, affiche 'Entrée invalide' et redemande.
    while True:
        choice = input().strip()
        if choice in options:
            return choice
        print("❌ Entrée invalide, réessaie.")

def intro(nom):
    print(f"=== Bienvenue dans Clash Royale {nom} ===")
    print("Règles : Chaque tour, choisis une carte parmi 3 de ton deck pour combattre l'ennemi.")
    print("Si tu perds, tu recommences depuis zéro.\n")