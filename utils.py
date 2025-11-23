def press_enter():
    input("\nAppuie sur Entrée pour continuer...")

def ask_choice(options):
    #Demande au joueur de saisir une option valide.
    #Ne montre pas les options. Si l'entrée est invalide, affiche 'Entrée invalide' et redemande.
    while True:
        choice = input().strip()
        if choice in options:
            return choice
        print("❌ Entrée invalide, choisis un nombre de la liste.")

def intro(nom):
    print(f"=== Bienvenue dans Clash Royale {nom} === \n")
    print("""Dans ce monde médiéval sans limites où la magie et les créatures fantastiques font partie du quotidien, de nombreux royaumes avides de richesses se sont engagés dans la bataille surnommée le "clash royal", une guerre éternelle qui se joue dans des arènes où deux rois se font face lors d'un duel spectaculaire. Entre ces quatre remparts, la loi du plus fort est absolue. Chaque camp envoie sa recrue la plus prometteuse pour le représenter lors de multiples faces-à-faces. Seul  le roi invaincu aura la chance de passer à la prochaine arène et de continuer sa quête. Le sort réservé au roi perdant n'est nul autre que sa destitution. Sa couronne sera livrée au vainqueur et il se verra renvoyé à la case départ. La légende raconte qu'un jour, un roi téméraire aurait atteint l'arène finale au bout de mille et une victoires à son compte. Cependant beaucoup disent qu'il ne s'agit que d'une histoire inventée pour invectiver les esprits et embraser les combats. Serais-tu prêt à porter le fardeau d'un peuple tout entier pour le mener à la victoire ? Le chemin sera long et tu feras surement face à des défaites. Si tu te sens capable d'accomplir cette tâche alors bonne chance à toi futur champion !\n""")

    print("Règles : Chaque tour, choisis une carte parmi 3 de ton deck pour combattre l'ennemi. Tu obtiendras des couronnes à chaque combat gagné qui te permettront d'acheter des bonus pour t'aider dans les combats \n")
    print("Si tu perds, tu recommences depuis zéro.\n ")