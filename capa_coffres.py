# Toutes les capacités des sorts et bâtiments
# Bonus selon l'arène ( pour suivre croissance jeu )
def bonus_par_arene(arene):
    return arene

# Les sorts
def Soin(carte, ennemi, combat_state, arene=0):
    soin = 20 + 2*bonus_par_arene(arene)
    carte['vie'] += soin  # ⬅ soin immédiat
    print(f"Tu récupères {soin} PV immédiatement !")

def Foudre(carte, ennemi, combat_state, arene=0):
    dmg = 16 + 2*bonus_par_arene(arene)
    ennemi['hp'] -= dmg
    print(f'Foudre : {dmg} dégâts instantanés !')

def Rage(carte, ennemi, combat_state, arene=0):
    combat_state['rage'] = 1.75
    print('Rage : tes attaques sont augmentées de 75% pour ce combat !')

def Roquette(carte, ennemi, combat_state, arene=0):
    ennemi['hp'] = 0
    print('Roquette : ennemi instantanément éliminé !')

# Les batiments
def Canon(carte, ennemi, combat_state, arene=0):
    bonus = 6 + 2*bonus_par_arene(arene)
    combat_state['bonus_atk'] += bonus
    print(f'Canon : +{bonus} ATK chaque tour.')

def Mortier(carte, ennemi, combat_state, arene=0):
    bonus = 5 + 2*bonus_par_arene(arene)
    combat_state['bonus_atk'] += bonus
    print(f'Mortier : +{bonus} ATK chaque tour.')

def Tesla(carte, ennemi, combat_state, arene=0):
    bonus = 4 + bonus_par_arene(arene)
    combat_state['bonus_atk'] += bonus
    ennemi['atk'] = max(0, ennemi['atk']//2)
    print(f' Tesla : +{bonus} ATK et l\'ennemi perd 50% d\'attaque.')

def Tour_de_l_Enfer(carte, ennemi, combat_state, arene=0):
    bonus =  8 + 2 * bonus_par_arene(arene)
    combat_state['bonus_atk'] += bonus
    print(f' Tour de l\'enfer : +{bonus} ATK chaque tour.')

def Cabane_de_gobelins(carte, ennemi, combat_state, arene=0):
    bonus = 7 + bonus_par_arene(arene)
    combat_state['bonus_atk'] += bonus
    print(f'Cabane : +{bonus} ATK, 3 gobelins t\'aident.')

# Crée un état de combat initial
def creer_etat_combat():
    return {
        'bonus_atk':0,
        'rage':1.0,
        'heal':0,
    }
# faire le dictionnaire
CAPACITES = {
    'Soin': Soin,
    'Foudre': Foudre,
    'Rage': Rage,
    'Roquette': Roquette,
    'Canon': Canon,
    'Mortier': Mortier,
    'Tesla': Tesla,
    "Tour de l'Enfer": Tour_de_l_Enfer,
    'Cabane de gobelins': Cabane_de_gobelins,
}

