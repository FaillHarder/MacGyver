from models.macgyver import MacGyver
from constants import SCREEN


class View:

    @staticmethod
    def draw(tile_list, pos_x, pos_y):
        """Méthode permétant de dessiner le labyrinthe.
        Elle prend en paramètre la liste des tuiles
        et les position x, y de la première tuile"""
        x_number = 0
        y_number = 20
        # Clé de mon dictionaire = Instance de classe
        # Valeur = Image associer à la classe
        for x, tile in enumerate(tile_list):
            tile.draw(SCREEN, (pos_x + x_number), pos_y)
            x_number += 20
            if (x + 1) % 15 == 0:
                pos_y += y_number
                x_number = 0

    @staticmethod
    def blit_img(screen, image, pos_x, pos_y):
        return SCREEN.blit(image, (pos_x, pos_y))

    @staticmethod
    def blit_text(screen, font, text, color, pos_x, pos_y):
        text = font.render(text, True, (color))
        return SCREEN.blit(text, (pos_x, pos_y))

    @staticmethod
    def index_macgyver(liste):
        """Method return the index of macgyver in the maze"""
        for pos, tile in enumerate(liste):
            if isinstance(tile, MacGyver):
                return pos