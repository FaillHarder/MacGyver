from model import Model
import pygame

SCREEN = pygame.display.set_mode((600, 600))
WALL = pygame.image.load("ressource/wall.png").convert_alpha()
PATH = pygame.image.load("ressource/path.png").convert_alpha()
MACGYVER = pygame.image.load("ressource/Mac20.png").convert_alpha()
GUARDIAN = pygame.image.load("ressource/Guardian20.png").convert_alpha()
NEEDLE = pygame.image.load("ressource/needle20.png").convert_alpha()
TUBE = pygame.image.load("ressource/tube20.png").convert_alpha()
ETHER = pygame.image.load("ressource/ether20.png").convert_alpha()


"""wall = Wall(WALL)
path = Path(PATH)
macgyver = MacGyver(MACGYVER)
guardian = Guardian(GUARDIAN)
tube = Tube(TUBE)
needle = Needle(NEEDLE)
ether = Ether(ETHER)"""


maze = []
Model.load_from_file(maze)


class ImageManager:
    images = {}

    @staticmethod
    def __init__():
        ImageManager.images["Wall"] = WALL
        ImageManager.images["MacGyver"] = MACGYVER
        ImageManager.images["Guardian"] = GUARDIAN
        ImageManager.images["Path"] = PATH
        ImageManager.images["Tube"] = TUBE
        ImageManager.images["Ether"] = ETHER
        ImageManager.images["Needle"] = NEEDLE

    @staticmethod
    def get(name):
        return ImageManager.images[name]


class Tile():

    def __init__(self, image):
        self.image = image

    def draw(self, screen, pos_x, pos_y):
        screen.blit(self.image, (pos_x, pos_y))


class Wall(Tile):
    def __init__(self,):
        super().__init__(ImageManager.get("Wall"))


class Path(Tile):
    def __init__(self):
        super().__init__(ImageManager.get("Path"))


class Guardian(Tile):
    def __init__(self):
        super().__init__(ImageManager.get("Guardian"))


class MacGyver(Tile):
    def __init__(self):
        super().__init__(ImageManager.get("MacGyver"))


class Objects(Tile):
    def __init__(self, image):
        self.image = image


class Needle(Objects):
    def __init__(self):
        super().__init__(ImageManager.get("Needle"))


class Tube(Objects):
    def __init__(self):
        super().__init__(ImageManager.get("Tube"))


class Ether(Objects):
    def __init__(self):
        super().__init__(ImageManager.get("Ether"))


ImageManager.__init__()
tile_list = []
tile_list.append(Wall())
tile_list.append(Path())
tile_list.append(MacGyver())
tile_list.append(Guardian())
tile_list.append(Tube())
tile_list.append(Needle())
tile_list.append(Ether())
continuer = True
pygame.init()

for tile in maze:
    tile.draw(SCREEN, 20, 20)

"""while continuer:

    
    tile.draw(SCREEN, 20, 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    pygame.display.flip()

pygame.quit()"""
