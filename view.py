from models.macgyver import MacGyver
from managers.fontmanager import FontManager
from managers.imagemanager import ImageManager
from constants import SCREEN, TITLE, BLUE, START, BLUE2, CLOSE


class View:

    @staticmethod
    def draw(tile_list, pos_x, pos_y):
        """Method allowing to draw the labyrinth.
        It takes as parameter the list of tiles
        and the x, y positions of the first tile"""
        x_number = 0
        y_number = 20
        # Clé de mon dictionaire = Instance de classe
        # Valeur = Image associer à la classe
        for x, tile in enumerate(tile_list):
            tile.draw((pos_x + x_number), pos_y)
            x_number += 20
            if (x + 1) % 15 == 0:
                pos_y += y_number
                x_number = 0

    @staticmethod
    def blit_img(image, pos_x, pos_y):
        """Method to blit an image"""
        return SCREEN.blit(image, (pos_x, pos_y))

    @staticmethod
    def blit_text(font, text, color, pos_x, pos_y):
        """Method to blit an text"""
        text = font.render(text, True, (color))
        return SCREEN.blit(text, (pos_x, pos_y))

    @classmethod
    def draw_rules(cls):
        cls.blit_text(FontManager.get("title"), TITLE, BLUE, 10, 5)
        cls.blit_text(FontManager.get("sq"), START, BLUE2, 35, 50)
        cls.blit_text(FontManager.get("sq"), CLOSE, BLUE2, 32, 80)
        cls.blit_img(ImageManager.get("gr"), 0, 150)

    @staticmethod
    def index_macgyver(liste):
        """Method return the index of macgyver in the maze"""
        for pos, tile in enumerate(liste):
            if isinstance(tile, MacGyver):
                return pos
