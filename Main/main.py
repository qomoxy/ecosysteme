import simulation as sim

def main():
    """
    Fonction principale du programme.
    """
    answer = input(str(" \n Bienvenue sur le simulateur de prairie !\n Voulez-vous lancer une simulation ? (Oui/Non) : "))
    if answer.lower() == "oui":
        choice1 = input(str(" \n Voulez-vous modifié les paramètres de la simulation ? (Oui/Non) : "))
        if choice1.lower() == "oui":
            duree_repousse = int(input(" \n 1/8 | Entrez la durée de repousse de l'herbe dans la prairie (et aussi la longueur minimum d'herbe pour qu'elle puisse être mangé) : "))
            herbe_max = int(input(" 2/8 | Entrez la hauteur maximale de l'herbe : "))
            taille = int(input(" 3/8 | Entrez la taille de la prairie : "))
            nb_moutons = int(input(" 4/8 | Entrez le nombre de moutons : "))
            nb_loups = int(input(" 5/8 | Entrez le nombre de loups : "))
            faim_mouton = int(input(" 6/8 | Entrez le nombre de points de faim pour chaque mouton (l'énergie qu'il vont perdre chaque tour) : "))
            energie_mouton = int(input(" 7/8 | Entrez le nombre de points d'énergie qu'a chaque moutons : "))
            faim_loup = int(input(" 7/8 | Entrez le nombre de points de faim pour chaque mouton (l'énergie qu'il vont perdre chaque tour) : "))
            energie_loup = int(input(" 8/8 | Entrez le nombre de points d'énergie qu'a chaque loups : "))
            print("\n"*10)
            simulation = sim.Simulation(duree_repousse, herbe_max, taille, nb_moutons, nb_loups, faim_mouton, energie_mouton, faim_loup, energie_loup)
            simulation.partie()
        else:
            simulation = sim.Simulation()
            simulation.partie()
    else:
        print("Merci d'avoir lancé le programme de simulation. Au revoir !")
        exit()

if __name__ == "__main__":
    main()
