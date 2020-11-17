from wall import Wall
from path import Path
from macgyver import MacGyver
from guardian import Guardian
from objects import Tube, Needle, Ether
from constants import screen, macgyver, tube, needle, ether, guardian, wall, path



"""screen = pygame.display.set_mode((300, 400))
image = pygame.image.load("ressource/floor-tiles-20x20.png").convert_alpha()
path = image.subsurface(pygame.Rect(60, 240, 20, 20))
wall = image.subsurface(pygame.Rect(140, 220, 20, 20))
macgyver = pygame.image.load("ressource/macgyver.png").convert()
macgyver = pygame.transform.scale(macgyver, (20, 20))
guardian = pygame.image.load("ressource/Gardien.png").convert()
guardian = pygame.transform.scale(guardian, (20, 20))
needle = pygame.image.load("ressource/seringue.png").convert()
needle = pygame.transform.scale(needle, (20, 20))
tube = pygame.image.load("ressource/tube_plastique.png").convert()
tube = pygame.transform.scale(tube, (20, 20))
ether = pygame.image.load("ressource/ether.png").convert()
ether = pygame.transform.scale(ether, (20, 20))"""


class View:
    @staticmethod
    def draw(tile_list, pos_x, pos_y):
        """Méthode permétant de dessiner le labyrinthe.
        Elle prend en paramètre la liste des tuiles
        et les position x, y de départ du dessin"""
        x_number = 0
        y_number = 20
        for x, tile in enumerate(tile_list):
            if isinstance(tile, MacGyver):
                screen.blit(macgyver, (pos_x + x_number, pos_y))
            elif isinstance(tile, Wall):
                screen.blit(wall, (pos_x + x_number, pos_y))
            elif isinstance(tile, Path):
                screen.blit(path, (pos_x + x_number, pos_y))
            elif isinstance(tile, Guardian):
                screen.blit(guardian, (pos_x + x_number, pos_y))
            elif isinstance(tile, Needle):
                screen.blit(needle, (pos_x + x_number, pos_y))
            elif isinstance(tile, Tube):
                screen.blit(tube, (pos_x + x_number, pos_y))
            elif isinstance(tile, Ether):
                screen.blit(ether, (pos_x + x_number, pos_y))
            x_number += 20
            if (x + 1) % 15 == 0:
                pos_y += y_number
                x_number = 0

    @staticmethod
    def index_macgyver(liste):
        """Méthode permettant de récuprérer l'index de macgyver dans la liste"""
        for tile in liste:
            if isinstance(tile, MacGyver):
                return liste.index(tile)
