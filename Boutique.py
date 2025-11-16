import json
import random

# Prix associés à chaque coffre
prix_coffres = {
    "coffre_argent": 2,
    "coffre_or": 5,
    "coffre_diamant": 8
}

# Charger les coffres depuis cartes.json
def charger_coffres(fichier):
    with open(fichier, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data["COFFRES"]

# Afficher les options
def afficher_boutique():
    print("\n🛒 Boutique")
    print("1. Coffre Argent : 3 couronnes")
    print("2. Coffre Or : 5 couronnes")
    print("3. Coffre Diamant : 8 couronnes")
    print("4. Quitter")

# Tirer une carte aléatoire
def tirer_carte(coffre):
    return random.choice(coffre)

# Boutique REELLE utilisée par le jeu
def boutique(couronnes):

    inventaire = []
    coffres = charger_coffres("cartes.json")

    while True:
        print(f"\n Couronnes disponibles : 👑 {couronnes} 👑")
        afficher_boutique()

        choix = input("\n👉 Que veux-tu faire ? (1-4) : ")

        if choix == "4":
            print("\n👋 Tu quittes la boutique.")
            break

        elif choix in ["1", "2", "3"]:
            nom_coffre = list(prix_coffres.keys())[int(choix) - 1]
            prix = prix_coffres[nom_coffre]

            if couronnes < prix:
                print("❌ Tu n'as pas assez de couronnes.")
                continue

            carte = tirer_carte(coffres[nom_coffre])
            inventaire.append(carte)
            couronnes -= prix

            print(f"\n 🌪️ Tu as obtenu : {carte['nom']} ({carte['type']}, {carte['rarete']})")
            print(f" Couronnes restantes : 👑 {couronnes} 👑")

        else:
            print("❌ Choix invalide.")

    return couronnes, inventaire
