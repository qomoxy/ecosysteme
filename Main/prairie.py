import colorama as c
# module colorama pour les couleurs dans le terminal

c.init(autoreset=True) # Permet de réinitialiser les couleurs après chaque print.

class Prairie:
    """
    Classe qui représent une Prairie.
    """

    def __init__(self, herbe_max: int, duree_repousse: int, taille: int):
        """
        Initialise une Prairie.
        :param herbe_max: La hauteur max de l'herbe. (int)
        :param duree_repousse: La hauteur minimun de l'herbe pour qu'elle puisse être mangée. (int)
        :param taille: taille de la prairie. (int)
        """
        self.__herbe_max: int = herbe_max
        self.__duree_repousse: int = duree_repousse
        self.__taille: int = taille
        self.__grille = [[duree_repousse for _ in range(self.__taille)] for _ in range(self.__taille)]

    def get_herbe_max(self) -> int:
        """
        Sortie : Retourne la hauteur maximale de l'herbe.
        """
        return self.__herbe_max

    def get_duree_repousse(self) -> int:
        """
        Sortie : Retourne la durée de repousse de l'herbe.
        """
        return self.__duree_repousse

    def get_taille(self) -> int:
        """
        Sortie : Retourne la taille de la prairie.
        """
        return self.__taille

    def get_grille(self) -> list:
        """
        Sortie : Retourne la grille de la prairie.
        """
        return self.__grille

    def herbe_pousse(self) -> None:
        """
        Fait pousser l'herbe de la prairie.
        """
        for i in range(self.__taille):
            for j in range(self.__taille):
                if self.__grille[i][j] < self.__herbe_max:
                    self.__grille[i][j] += 1

    def assez_herbe(self, x: int, y: int) -> bool:
        """
        Sortie : Retourne True si il y a assez d'herbe sur la case (x,y), False sinon.
        :param x: La position x de la case.
        :param y: La position y de la case.
        """
        return self.__grille[x][y] >= self.__duree_repousse

    def manger_herbe(self, x: int, y: int) -> int:
        """
        Sortie : Retourne la hauteur de l'herbe mangée.
        :param x: La position x de la case.
        :param y: La position y de la case.
        """
        tmp = self.__grille[x][y]
        if self.assez_herbe(x, y):
            self.__grille[x][y] = 0
            print(tmp)
            return tmp
        return 0

    def __str__(self) -> str:
        """
        Sortie : Retourne une représentation de la prairie avec des couleurs.
        """
        res = ""
        for i in range(self.__taille):
            for j in range(self.__taille):
                if self.__grille[i][j] >= self.__duree_repousse:
                    res += (c.Back.GREEN + str(self.__grille[i][j]) + " " + c.Style.RESET_ALL)
                else:
                    res += (c.Back.YELLOW + str(self.__grille[i][j]) + " " + c.Style.RESET_ALL)
            res += "\n"
        return res


