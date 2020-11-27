from wall import Wall
from path import Path
from macgyver import MacGyver
from guardian import Guardian
from objects import Tube, Needle, Ether
from constants import (
    SCREEN, MACGYVER, TUBE, NEEDLE, ETHER, GUARDIAN, WALL, PATH)


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
        liste_instance = {
            Wall: WALL, Path: PATH, MacGyver: MACGYVER,
            Guardian: GUARDIAN, Tube: TUBE, Needle: NEEDLE, Ether: ETHER
            }
        for x, tile in enumerate(tile_list):
            for key in liste_instance:
                if isinstance(tile, key):
                    SCREEN.blit(liste_instance[key], (pos_x + x_number, pos_y))
                    x_number += 20
                    if (x + 1) % 15 == 0:
                        pos_y += y_number
                        x_number = 0

    @staticmethod
    def blit_text(screen, text, pos_x, pos_y):
        return SCREEN.blit(text, (pos_x, pos_y))

    @staticmethod
    def index_macgyver(liste):
        """Method return the index of macgyver in the maze"""
        for pos, tile in enumerate(liste):
            if isinstance(tile, MacGyver):
                return pos
