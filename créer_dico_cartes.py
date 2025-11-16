import json

# Cartes par rareté avec stats homogènes
cartes_communes = [
    {"nom": "Gang de gobelins", "attaque": 6, "vie": 10},
    {"nom": "Archers", "attaque": 7, "vie": 9},
    {"nom": "Chevalier", "attaque": 8, "vie": 11},
    {"nom": "Horde de gargouilles", "attaque": 6, "vie": 10},
    {"nom": "Barbares", "attaque": 7, "vie": 11},
    {"nom": "Recrues royales", "attaque": 6, "vie": 12},
    {"nom": "Squelettes", "attaque": 5, "vie": 9},
    {"nom": "Esprit de glace", "attaque": 6, "vie": 10},
    {"nom": "Artificière", "attaque": 7, "vie": 11}
]

cartes_rares = [
    {"nom": "Sorcier de feu", "attaque": 7, "vie": 11},
    {"nom": "Mini Pekka", "attaque": 8, "vie": 12},
    {"nom": "Valkyrie", "attaque": 7, "vie": 13},
    {"nom": "Chevaucheur de cochon", "attaque": 8, "vie": 12},
    {"nom": "Mousquetaire", "attaque": 7, "vie": 11},
    {"nom": "Gobelin à sarbacane", "attaque": 6, "vie": 10}
]

cartes_epiques = [
    {"nom": "Prince", "attaque": 8, "vie": 13},
    {"nom": "Géant squelette", "attaque": 7, "vie": 14},
    {"nom": "Sorcière", "attaque": 7, "vie": 12},
    {"nom": "Dragon électrique", "attaque": 8, "vie": 13}
]

cartes_legendaires = [
    {"nom": "Phoenix", "attaque": 9, "vie": 14},
    {"nom": "Fantôme", "attaque": 8, "vie": 13},
    {"nom": "Méga-chevalier", "attaque": 9, "vie": 15}
]

cartes_champions = [
    {"nom": "Reine des archers", "attaque": 10, "vie": 15},
    {"nom": "Chevalier d’or", "attaque": 9, "vie": 14},
    {"nom": "Géant royal champion", "attaque": 10, "vie": 16}
]

coffres = {
    "coffre_or": [
        {"nom": "Cabane de gobelins", "type": "batiment", "rarete": "rare", "attaque": None, "capacite": None},
        {"nom": "Pierre tombale", "type": "batiment", "rarete": "rare", "attaque": None, "capacite": None},
        {"nom": "Heal potion", "type": "sort", "rarete": "rare", "attaque": None, "capacite": None},
        {"nom": "Poison", "type": "sort", "rarete": "epique", "attaque": None, "capacite": None}
    ],

    "coffre_argent": [
        {"nom": "Canon","type": "batiment", "rarete": "commune", "attaque": None, "capacite": None},
        {"nom": "Mortier", "type": "batiment", "rarete": "commune", "attaque": None, "capacite": None},
        {"nom": "Gel", "type": "sort", "rarete": "epique", "attaque": None, "capacite": None},
        {"nom": "Rage", "type": "sort", "rarete": "commune", "attaque": None, "capacite": None}
    ],

    "coffre_diamant": [
        {"nom": "Tesla", "type": "batiment", "rarete": "epique", "attaque": None, "capacite": None},
        {"nom": "Tour de l'Enfer", "type": "batiment", "rarete": "legendaire", "attaque": None, "capacite": None},
        {"nom": "Foudre", "type": "sort", "rarete": "epique", "attaque": None, "capacite": None},
        {"nom": "Roquette", "type": "sort", "rarete": "legendaire", "attaque": None, "capacite": None}
    ]
}

donnees = {
    "CARTES": {
        "commune": cartes_communes,
        "rare": cartes_rares,
        "epique": cartes_epiques,
        "legendaire": cartes_legendaires,
        "champions": cartes_champions
    },
    "COFFRES": coffres
}

with open("cartes.json", "w", encoding="utf-8") as f:
    json.dump(donnees, f, ensure_ascii=False, indent=4)

