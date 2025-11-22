from capa_coffres import CAPACITES
from utils import ask_choice

def creer_etat_combat():
    return {
        'bonus_atk':0,
        'rage':1.0,
        'inferno':1.0,
        'poison':0,
        'poison_dmg':0,
        'gel':0,
        'heal':0,
        'tombstone':0,
        'tour_enfer_bonus': None
    }

def appliquer_effets(carte_hp, ennemi, combat_state):
    if ennemi.get('poison',0) > 0:
        ennemi['poison'] -= 1
        degats = combat_state.get('poison_dmg',0)
        ennemi['hp'] -= degats
        print(f"Poison : {degats} dégâts infligés à l'ennemi !")
    gele = False
    if ennemi.get('gel',0) > 0:
        ennemi['gel'] -= 1
        gele = True
        print("L'ennemi est gele et ne peut pas attaquer ce tour !")

    return carte_hp, ennemi, gele

def calculer_degats_joueur(base_atk, combat_state):
    degats = base_atk + combat_state.get('bonus_atk',0)
    degats *= combat_state.get('rage',1.0)
    degats *= combat_state.get('inferno',1.0)
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

    # États de l'ennemi (poison, gel, etc.)
    ennemi.setdefault('poison', 0)
    ennemi.setdefault('poison_dmg', 0)
    ennemi.setdefault('gel', 0)

    # === BOUCLE PRINCIPALE DU COMBAT ===
    while carte_hp > 0 and ennemi['hp'] > 0:

        print(f"\nTa carte : {carte['nom']} (HP {carte_hp}, ATK {carte_atk})")
        print(f"Ennemi : {ennemi['name']} (HP {ennemi['hp']}, ATK {ennemi['atk']})")

        # Effets début de tour
        carte_hp, ennemi, ennemi_gele = appliquer_effets(carte_hp, ennemi, combat_state)

        # Effets des bâtiments actifs
        for b in batiments_actifs:
            nom = b['nom']
            if nom in CAPACITES:
                CAPACITES[nom](carte, ennemi, combat_state, arene)

        # === CHOIX DU JOUEUR ===
        action_faite = False
        while not action_faite:

            print("\nChoisis ton action :")
            print("1. Attaquer")
            print("2. Utiliser un sort")
            print("3. Poser un bâtiment")

            choix = ask_choice(['1', '2', '3'])

            # 1 ATTAQUER
            if choix == '1':
                dmg = calculer_degats_joueur(carte_atk, combat_state)
                ennemi['hp'] -= dmg
                print(f"Tu infliges {dmg} dégâts !")
                action_faite = True

            # 2 SORT
            elif choix == '2':
                if not sorts:
                    print("Aucun sort disponible. Choisis une autre action.")
                    continue  # empêche la perte de tour

                sort = sorts[0]  # tu utilises le premier automatiquement
                nom = sort['nom']
                print(f"Tu utilises : {nom}")

                if nom in CAPACITES:
                    CAPACITES[nom](carte, ennemi, combat_state, arene)

                sorts.remove(sort)
                bonus_possedes.remove(sort)

                action_faite = True

            # 3 BÂTIMENT
            elif choix == '3':
                if not batiments:
                    print("Aucun bâtiment disponible. Choisis une autre action.")
                    continue  # empêche la perte de tour

                bat = batiments[0]  # tu poses le premier automatiquement
                print(f"Tu poses : {bat['nom']}")

                batiments_actifs.append(bat)
                batiments.remove(bat)
                action_faite = True

        # === ATTAQUE DE L'ENNEMI ===
        if ennemi['hp'] > 0:

            if ennemi_gele:
                print("L'ennemi est gelé et t'inflige 0 dégâts.")
            else:
                carte_hp -= ennemi['atk']
                print(f"L'ennemi t'inflige {ennemi['atk']} dégâts.")

        # === SOIN ===
        heal = combat_state.get('heal', 0)
        if heal > 0:
            print(f"Tu récupères {heal} PV !")
            carte_hp += heal
            combat_state['heal'] = 0

    # === PIERRE TOMBAL ===
    if carte_hp <= 0 and combat_state.get('tombstone', 0) > 0:
        dmg = combat_state['tombstone']
        print(f"Pierre tombale : un squelette frappe l'ennemi pour {dmg} dégâts !")
        ennemi['hp'] -= dmg

    return carte_hp > 0
