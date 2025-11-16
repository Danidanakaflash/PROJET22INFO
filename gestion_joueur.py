import json
import os

SAVE_PATH = "../Cartes/save.json"

def load_save():
    os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)  # Crée le dossier si inexistant
    try:
        with open(SAVE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"couronnes": 0, "arene": 1}
        save(data)
    return data

def save(data):
    os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)  # Crée le dossier si inexistant
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def reset_save():
    data = {"couronnes": 0, "arene": 1}
    save(data)
    return data