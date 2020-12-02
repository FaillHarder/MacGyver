import pygame


class ImageManager:
    images = {}

    @staticmethod
    def load():
        ImageManager.images["Wall"] = pygame.image.load(
            "ressources/images/wall.png").convert_alpha()
        ImageManager.images["MacGyver"] = pygame.image.load(
            "ressources/images/Mac20.png").convert_alpha()
        ImageManager.images["Guardian"] = pygame.image.load(
            "ressources/images/Guardian20.png").convert_alpha()
        ImageManager.images["Path"] = pygame.image.load(
            "ressources/images/path.png").convert_alpha()
        ImageManager.images["Tube"] = pygame.image.load(
            "ressources/images/tube20.png").convert_alpha()
        ImageManager.images["Ether"] = pygame.image.load(
            "ressources/images/ether20.png").convert_alpha()
        ImageManager.images["Needle"] = pygame.image.load(
            "ressources/images/needle20.png").convert_alpha()
        ImageManager.images["gr"] = pygame.image.load(
            "ressources/images/but_du_jeu.png").convert()

    @staticmethod
    def get(name):
        return ImageManager.images[name]
