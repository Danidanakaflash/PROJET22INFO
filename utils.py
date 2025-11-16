def press_enter():
    input("\nAppuie sur Entrée pour continuer...")


def ask_choice(prompt, choices):
    """
    prompt : texte à afficher
    choices : liste de valeurs autorisées (["1","2","3"])
    """
    print(prompt)
    choix = input("> ")

    while choix not in choices:
        print("Choix invalide. Réessaie.")
        choix = input("> ")

    return choix