import Main.prairie as prairie
import animaux.moutons as moutons
import random as r

class Loup:
    """
    Classe qui représent un Loup.
    """
    def __init__(self, x: int, y: int, energie: int, faim: int):
        """
        Constructeur de la classe Loup.
        :param x: coordonnée x du loup. (int)
        :param y: coordonnée y du loup. (int)
        :param faim: points de faim du loup. (int)
        :param energie: points d'énergie du loup. (int)
        """
        self.__x: int = x
        self.__y: int = y
        self.__faim: int = faim
        self.__energie: int = energie

    def get_x(self) -> int:
        """
        Sortie : Retourne la position x du loup.
        """
        return self.__x

    def get_y(self) -> int:
        """
        Sortie : Retourne la position y du loup.
        """
        return self.__y

    def get_faim(self) -> int:
        """
        Sortie : Retourne les points de faim du loup.
        """
        return self.__faim

    def get_energie(self) -> int:
        """
        Sortie : Retourne les points d'énergie du loup.
        """
        return self.__energie

    def update_energie(self, energie: int) -> None:
        """
        Met à jour les points d'énergie du loup.
        :param energie: Les points dénergie à ajouter ou à retirer au loup.
        """
        self.__energie += energie

    def est_mort(self) -> bool:
        """
        Sortie : Retourne True si le loup est mort, False sinon.
        """
        return self.__energie <= 0

    def a_faim_loup(self) -> None:
        """
        Fait perdre des points d'énergie au loup parraport à ça faim.
        """
        self.update_energie(-self.__faim)

    def mange(self, troupeau: moutons.Troupeau) -> bool:
        """
        Sortie : Retourne True si le loup a mangé un mouton, False sinon.
        :param troupeau: Le troupeau de mouton.
        """
        for mouton in troupeau.get_moutons_lst():
            if self.__x == mouton.get_x() and self.__y == mouton.get_y():
                tmp = mouton.get_energie()
                self.update_energie(tmp)
                troupeau.remove_mouton(mouton)

    def deplacement(self, p: prairie.Prairie) -> None:
        """
        Fait se déplacer le loup.
        :param p: instance de Prairie.
        """
        newx = self.__x + r.randint(-1, 1)
        newy = self.__y + r.randint(-1, 1)

        # Vérifie si la nouvelle position est dans les limites de la prairie
        if 0 <= newx < len(p.get_grille()) and 0 <= newy < len(p.get_grille()[0]):
            # Mets à jour les coordonnées du loup
            self.__x = newx
            self.__y = newy

    def __str__(self) -> str:
        """
        Sortie : Retourne l'état du loup.
        """
        return f"Le loup est en ({self.__x}, {self.__y}) avec {self.__energie} points d'énergie et {self.__faim} points de faim."

class Meute:
    """
    Classe représentant une meute de loup.
    """
    def __init__(self, energie_loup: int, faim_loup: int):
        """
        Constructeur de la classe Meute.
        """
        self.__loups_lst: list = []
        self.__naissances: int = 0
        self.__morts: int = 0
        self.__energie_loup: int = energie_loup
        self.__faim_loup: int = faim_loup

    def get_loups(self) -> list:
        """
        Sortie : Retourne la liste des loups.
        """
        return self.__loups_lst

    def get_naissances(self) -> int:
        """
        Sortie : Retourne le nombre de naissances.
        """
        return self.__naissances

    def get_morts(self) -> int:
        """
        Sortie : Retourne le nombre de morts.
        """
        return self.__morts

    def get_energie_loup(self) -> int:
        """
        Sortie : Retourne les points d'énergie des loups.
        """
        return self.__energie_loup

    def get_faim_loup(self) -> int:
        """
        Sortie : Retourne les points de faim des loups.
        """
        return self.__faim_loup

    def add_loup(self, loup: Loup) -> None:
        """
        Ajoute un loup à la meute.
        :param loup: instance de Loup.
        """
        self.__loups_lst.append(loup)

    def remove_loup(self, loup: Loup) -> None:
        """
        Supprime un loup de la meute.
        :param loup: instance de Loup.
        """
        self.__loups_lst.remove(loup)

    def equarrisseur(self) -> None:
        """
        Supprime les loups morts de la meute.
        """
        for loup in self.__loups_lst:
            if loup.est_mort():
                self.remove_loup(loup)
                self.__morts += 1

    def reproduction(self) -> None:
        """
        Fait se reproduire les loups.
        """
        for i in range(len(self.__loups_lst) - 1):
            for i2 in range(i + 1, len(self.__loups_lst)):
                if r.random() < 0.4 and self.__loups_lst[i].get_x() == self.__loups_lst[i2].get_x() and self.__loups_lst[i].get_y() == self.__loups_lst[i2].get_y():
                    if self.__loups_lst[i].get_energie() > 5 and self.__loups_lst[i2].get_energie() > 5:
                        self.add_loup(Loup(self.__loups_lst[i].get_x(), self.__loups_lst[i].get_y(), self.__faim_loup, self.__energie_loup))
                        self.__naissances += 1
                        self.__loups_lst[i].update_energie(-5)
                        self.__loups_lst[i2].update_energie(-5)

    def __str__(self) -> str:
        """
        Sortie : Retourne l'état de la meute.
        """
        res = ""
        for loup in self.__loups_lst:
            res += str(loup) + "\n"
        return res


