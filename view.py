from models.macgyver import MacGyver
from managers.fontmanager import FontManager
from managers.imagemanager import ImageManager
from constants import SCREEN, Color, Message


class View:

    @staticmethod
    def draw_maze(tile_list):
        """Method allowing to draw the labyrinth.
        It takes as parameter the list of tiles
        and the x, y positions of the first tile"""
        pos_x = 0
        pos_y = 100
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
    def index_macgyver(liste):
        """Method return the index of macgyver in the maze"""
        for pos, tile in enumerate(liste):
            if isinstance(tile, MacGyver):
                return pos

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
    def draw_title(cls):
        """Method to blit game title"""
        cls.blit_text(FontManager.get(
            "title"), Message.TITLE, Color.BLUE, 10, 5)

    @classmethod
    def draw_rules(cls):
        """Method to blit start/quit/rules"""
        cls.blit_text(FontManager.get("sq"), Message.START, Color.CYAN, 35, 50)
        cls.blit_text(FontManager.get("sq"), Message.CLOSE, Color.CYAN, 32, 80)
        cls.blit_img(ImageManager.get("gr"), 0, 150)

    @classmethod
    def draw_picked_objects(cls, objects_count):
        """Method to blit the collected objects (Needle, Tube, Ether)"""
        cls.blit_text(FontManager.get(
            "obj"), f"Objet ramassé : {objects_count}", Color.WHITE, 5, 85)

    @classmethod
    def draw_win_message(cls):
        """Method to blit win message"""
        cls.blit_text(FontManager.get("wl"), Message.WIN, Color.CYAN, 90, 50)

    @classmethod
    def draw_lose_message(cls):
        """Method to blit lose message"""
        cls.blit_text(FontManager.get("wl"), Message.LOSE, Color.RED, 75, 50)
