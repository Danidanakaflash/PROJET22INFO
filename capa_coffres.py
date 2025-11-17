
def appliquer_capacite(objet, ennemi, batiments_actifs):
    """
    Applique l'effet d'un sort ou d'un batiment sur l'ennemi ou sur le joueur.
    - objet: dictionnaire {nom, type, rarete, capacite}
    - ennemi: dictionnaire {name, hp, atk}
    - batiments_actifs: liste de batiments posés
    """
    nom = objet['nom']
    typ = objet['type']

    if typ == "sort":
        if nom == "Gel":
            # Gèle l'ennemi pendant 1 tour (pas d'attaque ce tour)
            ennemi['gel'] = True
            print("L'ennemi est gelé pour ce tour !")
        elif nom == "Poison":
            # Inflige 5 dégâts par tour pendant 3 tours
            ennemi['poison'] = 3
            print("️ L'ennemi est empoisonné pendant 3 tours !")
        elif nom == "Heal potion":
            # Rend 10 PV à la carte jouée (gérer dans combat)
            print(" Tu récupères 10 PV sur ta carte !")
            # retourner un signal pour combat.py
            return {"heal":10}
        elif nom == "Roquette":
            # Tue l'ennemi instantanément
            ennemi['hp'] = 0
            print("💥 ROQUETTE ! L'ennemi est détruit instantanément !")

    elif typ == "batiment":
        if nom == "Canon":
            # Augmente l'attaque +2 chaque tour
            batiments_actifs.append(objet)
            print(" Canon posé ! +2 ATK à chaque attaque.")
        elif nom == "Pierre tombale":
            # Effet spécial géré dans combat (spawn squelette si mort)
            batiments_actifs.append(objet)
            print("️ Pierre tombale posée ! Si tu meurs, un squelette inflige 5 dégâts.")
        elif nom == "Cabane de gobelins":
            batiments_actifs.append(objet)
            print(" Cabane de gobelins posée ! +2 ATK chaque attaque.")
        elif nom == "Mortier":
            batiments_actifs.append(objet)
            print(" Mortier posé ! +1 ATK chaque attaque.")
        elif nom == "Tesla":
            batiments_actifs.append(objet)
            print("⚡ Tesla posée ! +3 ATK chaque attaque.")
        elif nom == "Tour de l'Enfer":
            batiments_actifs.append(objet)
            print(" Tour de l'Enfer posée ! +5 ATK chaque attaque.")
