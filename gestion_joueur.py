import json
import os

SAVE_PATH = "../Cartes/save.json"

def creer_joueur(nom):
    return {'nom':nom, 'couronnes': 0, "arene": 1, "combats_gagnes_total": 0}

def save(data):
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def reset_save():
    data = {"couronnes": 0, "arene": 1}
    save(data)
    return data

def reset_cartes():
    with open("DATA/cartes_base.json", "r", encoding="utf-8") as f:
        base = json.load(f)

    with open("DATA/cartes.json", "w", encoding="utf-8") as f:
        json.dump(base, f, indent=4, ensure_ascii=False)


