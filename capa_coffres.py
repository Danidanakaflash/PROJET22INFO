# Toutes les capacités des sorts et bâtiments
# Bonus selon l'arène ( pour suivre croissance jeu )
def bonus_par_arene(arene):
    return arene

# Les sorts
def Gel(carte, ennemi, combat_state, arene=0):
    ennemi['gel'] = 1
    print("L'ennemi est gelé pour un tour !")

def Poison(carte, ennemi, combat_state, arene=0):
    dmg = 3 + bonus_par_arene(arene)
    ennemi['poison'] = 3
    ennemi['poison_dmg'] = dmg
    print(f'Poison : {dmg} dégâts par tour pendant 3 tours !')

def Heal_potion(carte, ennemi, combat_state, arene=0):
    heal = 10 + 2*bonus_par_arene(arene)
    combat_state['heal'] = heal
    print(f'Heal Potion : tu récupères {heal} PV !')

def Foudre(carte, ennemi, combat_state, arene=0):
    dmg = 5 + bonus_par_arene(arene)
    ennemi['hp'] -= dmg
    print(f'Foudre : {dmg} dégâts instantanés !')

def Rage(carte, ennemi, combat_state, arene=0):
    combat_state['rage'] = 1.5
    print('Rage : tes attaques sont augmentées de 50% pour ce combat !')

def Roquette(carte, ennemi, combat_state, arene=0):
    ennemi['hp'] = 0
    print('Roquette : ennemi instantanément éliminé !')

# Les batiments
def Canon(carte, ennemi, combat_state, arene=0):
    bonus = 2 + bonus_par_arene(arene)
    combat_state['bonus_atk'] += bonus
    print(f'Canon : +{bonus} ATK chaque tour.')

def Mortier(carte, ennemi, combat_state, arene=0):
    bonus = 1 + bonus_par_arene(arene)
    combat_state['bonus_atk'] += bonus
    print(f'Mortier : +{bonus} ATK chaque tour.')

def Tesla(carte, ennemi, combat_state, arene=0):
    bonus = 3 + bonus_par_arene(arene)
    combat_state['bonus_atk'] += bonus
    ennemi['atk'] = max(0, ennemi['atk']//2)
    print(f'⚡ Tesla : +{bonus} ATK et l\'ennemi perd 50% d\'attaque.')

def Tour_de_l_Enfer(carte, ennemi, combat_state, arene=0):
    if 'tour_enfer_bonus' not in combat_state:
        combat_state['tour_enfer_bonus'] = 5 + bonus_par_arene(arene)
    else:
        combat_state['tour_enfer_bonus'] *= 1.5
    combat_state['bonus_atk'] += combat_state['tour_enfer_bonus']
    print(f'Tour de l\'Enfer : +{combat_state["tour_enfer_bonus"]:.1f} ATK ce tour (x1,5 chaque tour)')

def Cabane_de_gobelins(carte, ennemi, combat_state, arene=0):
    bonus = 2 + bonus_par_arene(arene)
    combat_state['bonus_atk'] += bonus
    print(f'Cabane : +{bonus} ATK, 3 gobelins t\'aident.')

def Pierre_tombale(carte, ennemi, combat_state, arene=0):
    dmg = 5 + bonus_par_arene(arene)
    combat_state['tombstone'] = dmg
    print(f'Pierre tombale : si tu meurs, un squelette inflige {dmg} dégâts.')

# Crée un état de combat initial
def creer_etat_combat():
    return {
        'bonus_atk':0,
        'rage':1.0,
        'inferno':1.0,
        'poison':0,
        'poison_dmg':0,
        'gel':0,
        'heal':0,
        'tombstone':0,
        'tour_enfer_bonus': None
    }

# faire le dictionnaire
CAPACITES = {
    'Gel': Gel,
    'Poison': Poison,
    'Heal potion': Heal_potion,
    'Foudre': Foudre,
    'Rage': Rage,
    'Roquette': Roquette,
    'Canon': Canon,
    'Mortier': Mortier,
    'Tesla': Tesla,
    "Tour de l'Enfer": Tour_de_l_Enfer,
    'Cabane de gobelins': Cabane_de_gobelins,
    'Pierre tombale': Pierre_tombale,
}

