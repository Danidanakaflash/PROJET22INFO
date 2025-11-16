
from capa_coffres import appliquer_capacite
from utils import ask_choice

def combat(carte, ennemi, inventaire=None, batiments_actifs=None):
    """
    Combat entre une carte et un ennemi.
    - carte: dictionnaire avec 'nom', 'vie', 'attaque'
    - ennemi: dictionnaire avec 'name', 'hp', 'atk'
    - inventaire: liste des sorts/bâtiments obtenus en boutique (sorts = usage unique)
    - batiments_actifs: liste des bâtiments déjà posés (bonus permanent)
    """
    if inventaire is None:
        inventaire = []
    if batiments_actifs is None:
        batiments_actifs = []

    carte_hp = carte["vie"]
    carte_atk = carte["attaque"]

    print("\n--- Combat ---")

    while carte_hp > 0 and ennemi["hp"] > 0:
        print(f"\nTa carte : {carte['nom']} (HP {carte_hp})")
        print(f"Ennemi : {ennemi['name']} (HP {ennemi['hp']})")

        # Calculer bonus attaque des bâtiments actifs
        bonus_atk = sum([2 for b in batiments_actifs if b['nom'] in ["Canon", "Cabane de gobelins"]])

        # Afficher les actions
        print("\n1. Attaquer")
        if inventaire or batiments_actifs:
            print("2. Utiliser un sort/bâtiment")
            choix_actions = ["1", "2"]
        else:
            choix_actions = ["1"]

        action = ask_choice(choix_actions)

        if action == "1":
            # attaque normale avec bonus des bâtiments
            total_atk = carte_atk + bonus_atk
            ennemi["hp"] -= total_atk
            print(f"Tu infliges {total_atk} dégâts à l'ennemi.")

        elif action == "2":
            # choisir un sort ou bâtiment à utiliser
            objets_disponibles = inventaire + batiments_actifs
            for i, obj in enumerate(objets_disponibles, 1):
                print(f"{i}. {obj['nom']} ({obj['type']})")
            choix_obj = int(ask_choice([str(i) for i in range(1, len(objets_disponibles)+1)])) - 1
            objet_utilise = objets_disponibles[choix_obj]

            # appliquer la capacité
            retour = appliquer_capacite(objet_utilise, ennemi, batiments_actifs)

            # retirer les sorts à usage unique
            if objet_utilise in inventaire and objet_utilise['type'] == "sort":
                inventaire.remove(objet_utilise)

            # les bâtiments restent dans batiments_actifs

        # riposte ennemie si vivant et pas gelé
        if ennemi["hp"] > 0:
            if "gel" in ennemi and ennemi["gel"]:
                print("L'ennemi est gelé et ne peut pas attaquer ce tour !")
                ennemi["gel"] = False  # effet gel dure 1 tour
            else:
                carte_hp -= ennemi["atk"]
                print(f"L'ennemi riposte et inflige {ennemi['atk']} dégâts.")

        # effets poison
        if "poison" in ennemi and ennemi["poison"] > 0:
            carte_hp -= 5
            ennemi["poison"] -= 1
            print("L'effet Poison te fait perdre 5 HP !")

    # combat terminé
    if carte_hp > 0:
        print(f"\n✅ Tu as vaincu {ennemi['name']} !")
    else:
        print(f"\n💀 Ta carte a été détruite par {ennemi['name']} !")

    return carte_hp > 0
