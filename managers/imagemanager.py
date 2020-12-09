import pygame


class ImageManager:
    images = {}

    @classmethod
    def load(cls):
        cls.images["Wall"] = pygame.image.load(
            "ressources/images/wall.png").convert()
        cls.images["MacGyver"] = pygame.image.load(
            "ressources/images/Mac.png").convert()
        cls.images["Guardian"] = pygame.image.load(
            "ressources/images/Guardian.png").convert()
        cls.images["Path"] = pygame.image.load(
            "ressources/images/path.png").convert()
        cls.images["Tube"] = pygame.image.load(
            "ressources/images/tube.png").convert()
        cls.images["Ether"] = pygame.image.load(
            "ressources/images/ether.png").convert()
        cls.images["Needle"] = pygame.image.load(
            "ressources/images/needle.png").convert()
        cls.images["gr"] = pygame.image.load(
            "ressources/images/but_du_jeu.png").convert()

    @classmethod
    def get(cls, name):
        return cls.images[name]
