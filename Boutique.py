import random
import json
from utils import ask_choice

# Prix associés à chaque coffre
prix_coffres = {
    "coffre_argent": 2,
    "coffre_or": 4,
    "coffre_diamant": 6
}

# Charger les coffres depuis cartes.json
def charger_coffres(fichier):
    with open(fichier, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data["COFFRES"]

# Afficher les options
def afficher_boutique():

    print("\n🛒 Boutique")
    print("1. Coffre Argent : 2 couronnes")
    print("2. Coffre Or : 4 couronnes")
    print("3. Coffre Diamant : 6 couronnes")
    print("4. Quitter")

# Tirer une carte aléatoire
def tirer_carte(coffre):
    return random.choice(coffre)

# Boutique REELLE utilisée par le jeu
def boutique(couronnes):

    inventaire = []
    coffres = charger_coffres("DATA/cartes.json")

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

            print(f"\n Tu as obtenu : {carte['nom']} ({carte['type']}, {carte['rarete']})")
            print(f" Couronnes restantes : 👑 {couronnes} 👑")

        else:
            print("❌ Choix invalide.")

    return couronnes, inventaire


def charger_cartes():
    with open("DATA/cartes.json", "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder_cartes(data):
    with open("DATA/cartes.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def bonus(joueur):
    data = charger_cartes()
    toutes_les_cartes = data["CARTES"]   # commune, rare, epique, etc.

    print("Choisis ton bonus :")
    print("1. +1 couronne")
    print("2. +1 PV à toutes tes cartes")
    print("3. +1 ATK à toutes tes cartes")

    choix = ask_choice(["1", "2", "3"])

    if choix == "1":
        joueur["couronnes"] += 1
        print("Tu gagnes 1 couronne.")

    elif choix == "2":
        for categorie in toutes_les_cartes.values():
            for carte in categorie:
                carte["vie"] += 1
        print("+1 PV ajouté à toutes les cartes.")
        sauvegarder_cartes(data)

    elif choix == "3":
        for categorie in toutes_les_cartes.values():
            for carte in categorie:
                carte["attaque"] += 1
        print("+1 ATK ajouté à toutes les cartes.")
        sauvegarder_cartes(data)
