import colorama as c
import random as r

import animaux.loups as loups
import animaux.moutons as moutons
import Main.prairie as prairie

c.init(autoreset=True)


class Simulation:
    """
    Classe qui représente la simulation.
    """

    def __init__(self, duree_repousse: int = 4, herbe_max: int = 9, taille: int = 5, nb_moutons: int = 5,
                 nb_loups: int = 2, faim_mouton: int = 3, energie_mouton: int = 10, faim_loup: int = 3,
                 energie_loup: int = 10):
        """
        Constructeur de la classe Simulation.
        :param nb_moutons: Nombre de moutons dans la simulation. (int)
        :param nb_loups: Nombre de loups dans la simulation. (int)
        """
        self.__prairie = prairie.Prairie(herbe_max, duree_repousse, taille)
        self.__troupeau = moutons.Troupeau(energie_mouton, faim_mouton)
        self.__meute = loups.Meute(energie_loup, faim_loup)
        self.__tour: int = 0

        for _ in range(nb_moutons):
            self.__troupeau.add_mouton(moutons.Mouton(r.randint(0, self.__prairie.get_taille() - 1),
                                                      r.randint(0, self.__prairie.get_taille() - 1),
                                                      self.__troupeau.get_faim_mouton(),
                                                      self.__troupeau.get_energie_mouton()))

        for _ in range(nb_loups):
            self.__meute.add_loup(loups.Loup(r.randint(0, self.__prairie.get_taille() - 1),
                                             r.randint(0, self.__prairie.get_taille() - 1),
                                             self.__meute.get_faim_loup(),self.__meute.get_energie_loup()))

    def get_prairie(self) -> prairie.Prairie:
        """
        Sortie : Retourne la prairie de la simulation.
        """
        return self.__prairie

    def get_troupeau(self) -> moutons.Troupeau:
        """
        Sortie : Retourne le troupeau de la simulation.
        """
        return self.__troupeau

    def get_meute(self) -> loups.Meute:
        """
        Sortie : Retourne la meute de la simulation.
        """
        return self.__meute

    def get_tour(self) -> int:
        """
        Sortie : Retourne le nombre de tours de la simulation.
        """
        return self.__tour

    def un_tour(self):
        self.__tour += 1

        self.__prairie.herbe_pousse()

        for mouton in self.__troupeau.get_moutons_lst():
            mouton.a_faim_mouton()
            mouton.deplacement(self.get_prairie())
            mouton.mange(self.get_prairie())
            print(mouton)

        self.__troupeau.equarrisseur()
        self.__troupeau.reproduction()

        for loup in self.__meute.get_loups():
            loup.a_faim_loup()
            loup.deplacement(self.get_prairie())
            loup.mange(self.__troupeau)

        self.__meute.equarrisseur()
        self.__meute.reproduction()

    def trouver_mouton(self, x: int, y: int) -> bool:
        """
        Sortie : Retourne le mouton à la position (x, y).
        :param x: La position x du mouton.
        :param y: La position y du mouton.
        """
        for mouton in self.__troupeau.get_moutons_lst():
            if mouton.get_x() == x and mouton.get_y() == y:
                return True
        return False

    def trouver_loup(self, x: int, y: int) -> bool:
        """
        Sortie : Retourne le loup à la position (x, y).
        :param x: La position x du loup.
        :param y: La position y du loup.
        """
        for loup in self.__meute.get_loups():
            if loup.get_x() == x and loup.get_y() == y:
                return True
        return False

    def affichage(self):
        """
        Affiche les informations de la simulation.
        """
        print(f"----------- Tour n°{self.__tour} -----------")
        print(
            f"Nombre de moutons : {len(self.__troupeau.get_moutons_lst())}          Nombre de naissances : {self.__troupeau.get_naissances()}          Nombre de morts : {self.__troupeau.get_morts()}")
        print(
            f"Nombre de loups : {len(self.__meute.get_loups())}            Nombre de naissances : {self.__meute.get_naissances()}          Nombre de morts : {self.__meute.get_morts()}")

        res = ""
        grille = self.__prairie.get_grille()
        for i in range(self.__prairie.get_taille()):
            for j in range(self.__prairie.get_taille()):
                if self.trouver_loup(i, j):
                    res += (c.Back.RED + "L " + c.Back.RESET)
                elif self.trouver_mouton(i, j):
                    res += (c.Back.WHITE + "M " + c.Back.RESET)
                elif grille[i][j] >= self.__prairie.get_duree_repousse():
                    res += (c.Back.GREEN + str(grille[i][j]) + " " + c.Back.RESET)
                else:
                    res += (c.Back.YELLOW + str(grille[i][j]) + " " + c.Back.RESET)
            res += "\n"
        print(res)

    def partie(self):
        """
        Lance la simulation.
        """
        while len(self.__troupeau.get_moutons_lst()) > 0:
            self.un_tour()
            self.affichage()
            print("\n")

    def __str__(self) -> str:
        """
        Sortie : Retourne l'état de la simulation.
        """
        return str(self.__prairie) + "\n" + str(self.__troupeau) + "\n" + str(self.__meute)


if __name__ == "__main__":
    sim = Simulation()
    sim.partie()
