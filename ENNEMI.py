import json
import random

def get_random_enemy(level=1, path="DATA/cartes.json"):
    # Charger les cartes depuis le JSON
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Ici on suppose que les ennemis sont dans "CARTES" > "commune" + "rare" + "epique" + "legendaire"
    cartes = []
    for rarete in ["commune", "rare", "epique", "legendaire"]:
        cartes += data["CARTES"][rarete]

    # Choisir un ennemi au hasard
    enemy = random.choice(cartes)

    # Augmenter les stats selon l'arène
    ennemi = {
        "name": enemy["nom"],
        "hp": enemy["vie"] + (level-1) * 2,    # exemple : +2 HP par arène
        "atk": enemy["attaque"] + (level-1)     # exemple : +1 ATK par arène
    }

    return ennemi