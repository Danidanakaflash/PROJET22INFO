from utils import ask_choice
from capa_coffres import appliquer_capacite

def combat(carte, ennemi, bonus_possedes):
    carte_hp = carte["vie"]
    carte_atk = carte["attaque"]

    print("\n--- Combat ---")

    # Séparer les sorts et les bâtiments
    sorts = [b for b in bonus_possedes if b["type"] == "sort"]
    batiments = [b for b in bonus_possedes if b["type"] == "batiment"]

    batiments_actifs = []   # bâtiments posés pendant ce combat

    while carte_hp > 0 and ennemi["hp"] > 0:

        print(f"\nTa carte : {carte['nom']} (HP {carte_hp}, ATK {carte_atk})")
        print(f"Ennemi : {ennemi['name']} (HP {ennemi['hp']}, ATK {ennemi['atk']})")

        # Appliquer les effets des bâtiments actifs à chaque tour
        for i in batiments_actifs:
            carte_hp, carte_atk, ennemi = appliquer_capacite( carte_hp, carte_atk, ennemi)

        print("\nChoisis ton action :")
        print("1. Attaquer")
        print("2. Utiliser un sort")
        print("3. Poser un bâtiment")

        choix = ask_choice(["1", "2", "3"])

        # --- 1 : Attaquer ---
        if choix == "1":
            # Appliquer bonus des bâtiments actifs
            total_bonus = sum(b.get("bonus_atk", 0) for b in batiments_actifs)
            degats = carte_atk + total_bonus
            ennemi["hp"] -= degats
            print(f"\n Tu infliges {degats} dégâts !")

        # --- 2 : Sort ---
        elif choix == "2":
            if not sorts:
                print("❌ Aucun sort disponible.")
                continue

            print("\n Sorts disponibles :")
            for i, s in enumerate(sorts):
                print(f"{i+1}. {s['nom']}")

            indice = ask_choice([str(i+1) for i in range(len(sorts))])
            sort = sorts[int(indice) - 1]

            print(f"\n Tu utilises : {sort['nom']}")
            carte_hp, carte_atk, ennemi = appliquer_capacite(carte_hp, carte_atk, ennemi)

            # Sort utilisé → supprimé
            bonus_possedes.remove(sort)
            sorts.remove(sort)

        # --- 3 : Bâtiment ---
        elif choix == "3":
            if not batiments:
                print("❌ Aucun bâtiment disponible.")
                continue

            print("\n Bâtiments disponibles :")
            for i, b in enumerate(batiments):
                print(f"{i+1}. {b['nom']}")

            indice = ask_choice([str(i+1) for i in range(len(batiments))])
            bat = batiments[int(indice) - 1]

            print(f"\n Tu poses le bâtiment : {bat['nom']} (effet actif dès ce tour)")
            batiments_actifs.append(bat)
            batiments.remove(bat)

        # Ennemi attaque si vivant
        if ennemi["hp"] > 0:
            carte_hp -= ennemi["atk"]
            print(f" L’ennemi inflige {ennemi['atk']} dégâts.")

    # Tous les bâtiments sont supprimés automatiquement après le combat
    return carte_hp > 0
