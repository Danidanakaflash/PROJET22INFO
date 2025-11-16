def combat(carte, ennemi):
    carte_hp = carte["vie"]
    carte_atk = carte["attaque"]

    print("\n--- Combat ---")

    while carte_hp > 0 and ennemi["hp"] > 0:
        print(f"\nTa carte : {carte['nom']} (HP {carte_hp})")
        print(f"Ennemi : {ennemi['name']} (HP {ennemi['hp']})")

        print("\n1. Attaquer")
        print("2. Passer (objet si tu veux plus tard)")
        action = input("> ")

        if action == "1":
            ennemi["hp"] -= carte_atk
            print(f"Tu infliges {carte_atk} dégâts.")

        if ennemi["hp"] > 0:
            carte_hp -= ennemi["atk"]
            print(f"L'ennemi riposte et inflige {ennemi['atk']} dégâts.")

    return carte_hp > 0