from gestion_joueur import load_save, save, reset_save, creer_joueur
from ENNEMI import get_random_enemy
from Combat import combat
from choix_cartes import proposer_3_cartes
from utils import ask_choice, press_enter
from capa_coffres import appliquer_capacite
import random

def game_loop():


    seed = input("Seed ? (laisser vide pour aléatoire)\n> ")
    if seed.strip() != "":
        random.seed(int(seed))

    nom = (input("Nom d'utilisateur :"))
    creer_joueur(nom)
    joueur = creer_joueur(nom)
    save("DATA/joueur.json")

    print(f"=== Bienvenue dans Clash Royale {nom} ===")
    print("Règles : Chaque tour, choisis une carte parmi 3 de ton deck pour combattre l'ennemi.")
    print("Si tu perds, tu recommences depuis zéro.\n")
    press_enter()

    # Inventaire des bonus acquis
    bonus_possedes = []

    # Boucle infinie d'arènes
    while True:

        print(f"\n=== Arène {joueur["arene"]} ===")
        print(f"Couronnes actuelles : {joueur["couronnes"]}")

        # Chaque arène contient 5 combats
        for combat_num in range(1, 6):

            print(f"\n--- Combat {combat_num} / 5 ---")

            # 1. Générer un ennemi
            ennemi = get_random_enemy((5*joueur["arene"])-5+combat_num)
            print(f"Un ennemi apparaît : {ennemi['name']} (HP={ennemi['hp']}, ATK={ennemi['atk']})")

            # 2. Proposer 3 cartes
            texte, cartes = proposer_3_cartes()
            print("\nChoisis une carte :")
            print(texte)

            # 3. Demander le choix du joueur
            choix = ask_choice(["1", "2", "3"])
            carte_choisie = cartes[int(choix) - 1]
            print(f"\nTu as choisi : {carte_choisie['nom']}")

            # 4. Combat avec possibilité d'utiliser un bonus
            vivant = combat(carte_choisie, ennemi, bonus_possedes)

            if not vivant:
                print("\n===== DÉFAITE =====")
                print(f"Tu as atteint l'arène {joueur["arene"]}.")
                print(f"Tu as gagné {joueur["combats_gagnes_total"]} combats au total.")

                # Reset la sauvegarde
                data = reset_save()
                joueur["couronnes"] = data["couronnes"]
                joueur["arene"] = data["arene"]
                joueur["combats_gagnes_total"] = 0
                bonus_possedes = []

                press_enter()
                break  # redémarre l'arène 1

            # 5. Victoire → +1 couronne
            joueur["couronnes"] += 1
            joueur["combats_gagnes_total"] += 1
            print(f"\nVictoire ! Tu gagnes 1 couronne. Total = {joueur["couronnes"]}")

            # 6. Aller à la boutique ?
            print("\nSouhaites-tu aller à la boutique ?")
            print("1. Oui")
            print("2. Non")

            rep = ask_choice(["1", "2"])

            if rep == "1":
                from Boutique import boutique
                couronnes, nouveaux_bonus = boutique(joueur["couronnes"])
                bonus_possedes.extend(nouveaux_bonus)
                save({"couronnes": couronnes, "arene": joueur["arene"]})

            # 7. Sauvegarde immédiate
            save({"couronnes":joueur["couronnes"], "arene": ["arene"]})

        # Fin de l'arène → passage à la suivante
        if joueur["couronnes"] > 0:
            print(f"\n=== Tu as terminé l'arène {["arene"]} ! ===")
            joueur["arene"] += 1
            save({"couronnes": ["couronnes"], "arene": ["arene"]})
            press_enter()


# Appel de la boucle principale
if __name__ == "__main__":
    game_loop()
