import json
import random

def charger_cartes(path="DATA/cartes.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["CARTES"]

def choisir_sans_doublon(pool, exclus):
    dispo = [c for c in pool if c["nom"] not in exclus]
    return random.choice(dispo)

def proposer_3_cartes(path="DATA/cartes.json", seed=None):
    if seed is not None:
        random.seed(seed)

    cartes = charger_cartes(path)

    # Pools selon rareté
    pool1 = cartes["commune"]
    pool2 = cartes["commune"] + cartes["rare"]
    pool3 = cartes["commune"] + cartes["rare"] + cartes["epique"] + cartes["legendaire"]

    exclus = set()

    choix1 = choisir_sans_doublon(pool1, exclus)
    exclus.add(choix1["nom"])

    choix2 = choisir_sans_doublon(pool2, exclus)
    exclus.add(choix2["nom"])

    choix3 = choisir_sans_doublon(pool3, exclus)

# Déterminer rareté
    def rarete_de(carte):
        for r in cartes:
         if carte in cartes[r]:
            return r


    r1 = rarete_de(choix1)
    r2 = rarete_de(choix2)
    r3 = rarete_de(choix3)

# Construire la chaîne à afficher
    resultat = (
        f"1 = {{ '{choix1['nom']}', 'attaque' : {choix1['attaque']}, 'vie' : {choix1['vie']} }} {r1}\n"
        f"2 = {{ '{choix2['nom']}', 'attaque' : {choix2['attaque']}, 'vie' : {choix2['vie']} }} {r2}\n"
        f"3 = {{ '{choix3['nom']}', 'attaque' : {choix3['attaque']}, 'vie' : {choix3['vie']} }} {r3}"
)

# Renvoie le texte + la liste des cartes choisies
    return resultat, [choix1, choix2, choix3]