from capa_coffres import CAPACITES
from utils import ask_choice

def creer_etat_combat(): #État temporaire du combat pour bonus et effets de sorts/bâtiments
    return {
        'bonus_atk': 0,
        'rage': 1.0,
        'inferno': 1.0,
        'heal': 0,
        'tour_enfer_bonus': None
    }

def calculer_degats_joueur(base_atk, combat_state): #Calcule les dégâts infligés par la carte du joueur
    degats = base_atk + combat_state.get('bonus_atk', 0)
    degats *= combat_state.get('rage', 1.0)
    degats *= combat_state.get('inferno', 1.0)
    return int(degats)

def combat(carte, ennemi, bonus_possedes, arene=0):

    carte_hp = carte['vie']
    carte_atk = carte['attaque']

    print("\n--- Combat ---")

    # Séparation sorts / bâtiments
    sorts = []
    batiments = []
    for b in bonus_possedes:
        if b['type'] == 'sort':
            sorts.append(b)
        elif b['type'] == 'batiment':
            batiments.append(b)

    combat_state = creer_etat_combat()
    batiments_actifs = []

    # Boucle principale
    while carte_hp > 0 and ennemi['hp'] > 0:

        print(f"\nTa carte : {carte['nom']} (HP {carte_hp}, ATK {carte_atk})")
        print(f"Ennemi : {ennemi['name']} (HP {ennemi['hp']}, ATK {ennemi['atk']})")

        # Effets des bâtiments actifs
        for b in batiments_actifs:
            nom = b['nom']
            if nom in CAPACITES:
                CAPACITES[nom](carte, ennemi, combat_state, arene)

        # Choix du joueur
        action_faite = False
        while not action_faite:
            print("\nChoisis ton action :")
            print("1. Attaquer")
            print("2. Utiliser un sort")
            print("3. Poser un bâtiment")

            choix = ask_choice(['1', '2', '3'])

            # Attaquer
            if choix == '1':
                dmg = calculer_degats_joueur(carte_atk, combat_state)
                ennemi['hp'] -= dmg
                print(f"Tu infliges {dmg} dégâts !")
                action_faite = True

            # Utiliser un sort
            elif choix == '2':
                if not sorts:
                    print("Aucun sort disponible. Choisis une autre action.")
                    continue
                sort = sorts[0]
                nom = sort['nom']
                print(f"Tu utilises : {nom}")
                if nom in CAPACITES:
                    CAPACITES[nom](carte, ennemi, combat_state, arene)
                sorts.remove(sort)
                bonus_possedes.remove(sort)
                action_faite = True

            # Poser un bâtiment
            elif choix == '3':
                if not batiments:
                    print("Aucun bâtiment disponible. Choisis une autre action.")
                    continue
                bat = batiments[0]
                print(f"Tu poses : {bat['nom']}")
                batiments_actifs.append(bat)
                batiments.remove(bat)
                action_faite = True

        # Attaque de l'ennemi
        if ennemi['hp'] > 0:
            carte_hp -= ennemi['atk']
            print(f"L'ennemi t'inflige {ennemi['atk']} dégâts.")

        # Soin éventuel
        heal = combat_state.get('heal', 0)
        if heal > 0:
            print(f"Tu récupères {heal} PV !")
            carte_hp += heal
            combat_state['heal'] = 0

    # Retourne True si le joueur survit, False sinon
    return carte_hp > 0
