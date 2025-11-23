import json
import random

def get_random_enemy(arene, path="DATA/cartes_base.json"):
    #Tire un ennemi aléatoire dans le JSON, détermine sa rareté,colore son nom et sa rareté, et augmente ses stats selon l'arène.

    COULEURS_RARETE = {
        "commune": "\033[94m",    # bleu
        "rare": "\033[38;5;208m",       # orange
        "epique": "\033[95m",     # violet
        "legendaire": "\033[91m"  # rouge
    }
    RESET = "\033[0m"

    # Charger les cartes depuis le JSON
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Pool de cartes ennemies
    cartes = []
    for rarete in ["commune", "rare", "epique", "legendaire"]:
        cartes += data["CARTES"][rarete]

    # Tirer un ennemi au hasard
    enemy = random.choice(cartes)

    # Déterminer la rareté
    rarete = None
    for r, liste in data["CARTES"].items():
        if enemy in liste:
            rarete = r
            break

    couleur = COULEURS_RARETE[rarete]

    # Créer le dictionnaire de l'ennemi avec stats ajustées selon l'arène, commence plus bas que nos cartes
    ennemi = {
        "name": f"{couleur}{enemy['nom']}{RESET}",
        "hp": enemy["vie"] -2 + (arene-1)*5,       # +5 PV par arène
        "atk": enemy["attaque"] -1 + (arene-1)*5,  # +5 ATK par arène
        "rarete": f"{couleur}{rarete}{RESET}"
    }

    return ennemi
