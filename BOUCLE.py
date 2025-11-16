from gestion_joueur import load_save, save, reset_save
from ENNEMI import get_random_enemy
from Combat import combat
from choix_cartes import proposer_3_cartes
from utils import ask_choice, press_enter
import random

def game_loop():

    # Charger la sauvegarde
    data = load_save()
    couronnes = data["couronnes"]
    arene = data["arene"]

    # Compteur total de combats gagnés (depuis le début de la partie)
    combats_gagnes_total = 0

    seed = input("Seed ? (laisser vide pour aléatoire)\n> ")
    if seed.strip() != "":
        random.seed(int(seed))

    print("=== Bienvenue dans Clash Royale ===")
    print("Règles : Chaque tour, choisis une carte parmis 3 de ton deck pour combattre l'ennemi. \nSi tu perds, tu recommences depuis zéro.\n")
    press_enter()

    # Boucle infinie d'arènes
    while True:

        print(f"\n=== Arène {arene} ===")
        print(f"Couronnes actuelles : {couronnes}")

        # Chaque arène contient 5 combats
        for combat_num in range(1, 6):

            print(f"\n--- Combat {combat_num} / 5 ---")

            # 1. Générer un ennemi
            ennemi = get_random_enemy(level=arene)
            print(f"Un ennemi apparaît : {ennemi['name']} (HP={ennemi['hp']}, ATK={ennemi['atk']})")

            # 2. Proposer 3 cartes
            texte, cartes = proposer_3_cartes()
            print("\nChoisis une carte :")
            print(texte)

            # 3. Demander le choix du joueur
            choix = ask_choice("> ", ["1", "2", "3"])
            carte_choisie = cartes[int(choix) - 1]
            print(f"\nTu as choisi : {carte_choisie['nom']}")

            # 4. Combat
            vivant = combat(carte_choisie, ennemi)

            if not vivant:
                print("\n===== DÉFAITE =====")
                print(f"Tu as atteint l'arène {arene}.")
                print(f"Tu as gagné {combats_gagnes_total} combats au total.")

                # Reset la sauvegarde
                data = reset_save()
                couronnes = data["couronnes"]
                arene = data["arene"]
                combats_gagnes_total = 0

                press_enter()
                break  # redémarre l'arène 1

            # 5. Victoire → +1 couronne
            couronnes += 1
            combats_gagnes_total += 1
            print(f"\nVictoire ! Tu gagnes 1 couronne. Tu en a en tout {couronnes}")

            # 6. Aller à la boutique ?
            print("\nSouhaites-tu aller à la boutique ?")
            print("1. Oui")
            print("2. Non")

            rep = ask_choice("> ", ["1", "2"])

            if rep == "1":
                from Boutique import boutique
                couronnes, _ = boutique(couronnes)
                save({"couronnes": couronnes, "arene": arene})

            # 7. Sauvegarde immédiate
            save({"couronnes": couronnes, "arene": arene})

        # Si le joueur vient de perdre, on recommence depuis l'arène 1
        if couronnes == 0 and arene == 1:
            continue

        # 8. Fin de l'arène → passage à la suivante
        print(f"\n=== Tu as terminé l'arène {arene} ! ===")
        arene += 1

        # 8. Sauvegarde
        save({"couronnes": couronnes, "arene": arene})

        press_enter()


# Appel de la boucle principale
if __name__ == "__main__":
    game_loop()