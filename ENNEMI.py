import json
import random

def get_random_enemy(arene, path="DATA/cartes.json"):
    """
    Tire un ennemi aléatoire dans le JSON, détermine sa rareté,
    colore son nom et sa rareté, et augmente ses stats selon l'arène.
    """
    # Codes ANSI pour couleurs selon rareté
    COULEURS_RARETE = {
        "commune": "\033[34m",    # bleu
        "rare": "\033[33m",       # orange
        "epique": "\033[35m",     # violet
        "legendaire": "\033[31m"  # rouge
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

    # Créer le dictionnaire de l'ennemi avec stats ajustées selon l'arène
    ennemi = {
        "name": f"{couleur}{enemy['nom']}{RESET}",
        "hp": enemy["vie"] + (arene-1)*3,       # +3 PV par arène
        "atk": enemy["attaque"] + (arene-1)*3,  # +3 ATK par arène
        "rarete": f"{couleur}{rarete}{RESET}"
    }

    return ennemi
