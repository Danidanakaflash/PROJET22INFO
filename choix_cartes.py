import json
import random

def charger_cartes(path="DATA/cartes.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["CARTES"]

def choisir_sans_doublon(pool, exclus):

    dispo = []
    for carte in pool:
        nom = carte["nom"]
        est_exclue = False

        # Vérifie si la carte doit être exclue
        for exclu in exclus:
            if nom == exclu:
                est_exclue = True

        # Ajoute si autorisé
        if not est_exclue:
            dispo.append(carte)

    # On suppose qu'au moins une carte est disponible
    return random.choice(dispo)

# Couleurs par rareté
COLORS = {
    "commune": "\033[94m",      # bleu
    "rare": "\033[38;5;208m",   # orange
    "epique": "\033[95m",       # violet
    "legendaire": "\033[91m"    # rouge
}
RESET = "\033[0m"

def proposer_3_cartes(path="DATA/cartes.json", seed=None):
    if seed is not None:
        random.seed(seed)

    cartes = charger_cartes(path)

    pool1 = cartes["commune"]
    pool2 = cartes["commune"] + cartes["rare"]
    pool3 = cartes["commune"] + cartes["rare"] + cartes["epique"] + cartes["legendaire"]

    exclus = set()

    choix1 = choisir_sans_doublon(pool1, exclus)
    exclus.add(choix1["nom"])

    choix2 = choisir_sans_doublon(pool2, exclus)
    exclus.add(choix2["nom"])

    choix3 = choisir_sans_doublon(pool3, exclus)

    # Trouver la rareté d'une carte
    def rarete_de(c):
        for r in cartes:
            if c in cartes[r]:
                return r

    r1 = rarete_de(choix1)
    r2 = rarete_de(choix2)
    r3 = rarete_de(choix3)

    # Affichage final : nom en couleur, rareté à la fin en couleur
    resultat = (
        f"1 = {COLORS[r1]}{choix1['nom']}{RESET}, vie : {choix1['vie']}, attaque : {choix1['attaque']}, rareté : {COLORS[r1]}{r1}{RESET}\n"
        f"2 = {COLORS[r2]}{choix2['nom']}{RESET}, vie : {choix2['vie']}, attaque : {choix2['attaque']}, rareté : {COLORS[r2]}{r2}{RESET}\n"
        f"3 = {COLORS[r3]}{choix3['nom']}{RESET}, vie : {choix3['vie']}, attaque : {choix3['attaque']},rareté : {COLORS[r3]}{r3}{RESET}"
    )

    return resultat, [choix1, choix2, choix3]
