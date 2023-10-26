import Main.prairie as prairie
# module prairie pour la classe Prairie
import random as r


# module random pour les déplacements aléatoires

class Mouton:
    """
    Classe représentant un mouton.
    """

    def __init__(self, x: int, y: int, energie: int, faim: int):
        """
        Constructeur de la classe Mouton.
        :param x: coordonnée x du mouton. (int)
        :param y: coordonnée y du mouton. (int)
        :param energie: points d'énergie du mouton. (int)
        :param faim: points de faim du mouton. (int)
        """
        self.__x: int = x
        self.__y: int = y
        self.__energie: int = energie
        self.__faim: int = faim

    def get_x(self) -> int:
        """
        Sortie : Retourne la position x du mouton.
        """
        return self.__x

    def get_y(self) -> int:
        """
        Sortie : Retourne la position y du mouton.
        """
        return self.__y

    def get_energie(self) -> int:
        """
        Sortie : Retourne les points d'énergie du mouton.
        """
        return self.__energie

    def update_energie(self, points: int) -> None:
        """
        Met à jour les points d'énergie du mouton.
        :param points: Les points dénergie à ajouter ou à retirer au mouton.
        """
        print(points)
        self.__energie += points
        print(self.__energie)

    def get_faim(self) -> int:
        """
        Sortie : Retourne les points de faim du mouton.
        """
        return self.__faim

    def est_mort(self) -> bool:
        """
        Sortie : Retourne True si le mouton est mort, False sinon.
        """
        return self.__energie <= 0

    def a_faim_mouton(self) -> None:
        """
        Fait perdre des points d'énergie au mouton parraport à ça faim.
        """
        self.update_energie(-self.__faim)

    def mange(self, p: prairie.Prairie) -> None:
        """
        Fait manger le mouton l'herbe de la case où il est.
        :param p: instance de Prairie.
        """
        tmp = p.manger_herbe(self.__x, self.__y) # J'ai fait ça car quand je le met dans le update_energie ça ne marche pas (ça ajoute 0)
        self.update_energie(tmp)

        if self.__energie > 20:
            self.__energie = 20

    def deplacement(self, p: prairie.Prairie) -> None:
        """
        Déplace le mouton à la position (x, y).
        :param p: instance de Prairie
        """
        newx = self.__x + r.randint(-1, 1)
        newy = self.__y + r.randint(-1, 1)

        # Vérifie si la nouvelle position est dans les limites de la prairie
        if 0 <= newx < len(p.get_grille()) and 0 <= newy < len(p.get_grille()[0]):
            # Mets à jour les coordonnées du mouton
            self.__x = newx
            self.__y = newy

    def __str__(self) -> str:
        """
        Sortie : Retourne une chaine de caractère représentant le mouton.
        """
        return f"Le mouton est en ({self.__x}, {self.__y}) avec {self.__energie} points d'énergie et {self.__faim} points de faim."


class Troupeau:
    """
    Classe représentant un troupeau de moutons.
    """

    def __init__(self, faim_mouton: int, energie_mouton: int):
        """
        Constructeur de la classe Troupeau.
        """
        self.__moutons_lst: list = []
        self.__naissances: int = 0
        self.__morts: int = 0
        self.__faim_mouton: int = faim_mouton
        self.__energie_mouton: int = energie_mouton

    def get_moutons_lst(self) -> list:
        """
        Sortie : Retourne la liste des moutons du troupeau.
        """
        return self.__moutons_lst

    def get_naissances(self) -> int:
        """
        Sortie : Retourne le nombre de naissances du troupeau.
        """
        return self.__naissances

    def get_morts(self) -> int:
        """
        Sortie : Retourne le nombre de morts du troupeau.
        """
        return self.__morts

    def get_faim_mouton(self) -> int:
        """
        Sortie : Retourne les points de faim des moutons.
        """
        return self.__faim_mouton

    def get_energie_mouton(self) -> int:
        """
        Sortie : Retourne les points d'énergie des moutons.
        """
        return self.__energie_mouton

    def add_mouton(self, mouton) -> None:
        """
        Ajoute un mouton au troupeau.
        :param mouton: instance de Mouton.
        """
        self.__moutons_lst.append(mouton)

    def remove_mouton(self, mouton) -> None:
        """
        Supprime un mouton du troupeau.
        :param mouton: instance de Mouton.
        """
        self.__moutons_lst.remove(mouton)

    def equarrisseur(self) -> None:
        """
        Supprime les moutons morts du troupeau.
        """
        for mouton in self.__moutons_lst:
            if mouton.est_mort():
                self.remove_mouton(mouton)
                self.__morts += 1

    def reproduction(self) -> None:
        """
        Fait se reproduire les moutons du troupeau.
        """
        for i in range(len(self.__moutons_lst) - 1):
            for i2 in range(i + 1, len(self.__moutons_lst)):
                if r.random() <= 0.4 and self.__moutons_lst[i].get_x() == self.__moutons_lst[i2].get_x() and self.__moutons_lst[i].get_y() == self.__moutons_lst[i2].get_y():
                    if self.__moutons_lst[i].get_energie() > 5 and self.__moutons_lst[i2].get_energie() > 5:
                        self.add_mouton(Mouton(self.__moutons_lst[i].get_x(), self.__moutons_lst[i].get_y(), self.__energie_mouton, self.__faim_mouton))
                        self.__naissances += 1
                        self.__moutons_lst[i].update_energie(-5)
                        self.__moutons_lst[i2].update_energie(-5)

    def __str__(self) -> str:
        """
        Sortie : Retourne une chaine de caractère représentant le troupeau.
        """
        res = ""
        for mouton in self.__moutons_lst:
            res += str(mouton) + "\n"
        return res
