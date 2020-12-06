import pygame


class ImageManager:
    images = {}

    @staticmethod
    def load():
        ImageManager.images["Wall"] = pygame.image.load(
            "ressources/images/wall.png").convert()
        ImageManager.images["MacGyver"] = pygame.image.load(
            "ressources/images/Mac.png").convert()
        ImageManager.images["Guardian"] = pygame.image.load(
            "ressources/images/Guardian.png").convert()
        ImageManager.images["Path"] = pygame.image.load(
            "ressources/images/path.png").convert()
        ImageManager.images["Tube"] = pygame.image.load(
            "ressources/images/tube.png").convert()
        ImageManager.images["Ether"] = pygame.image.load(
            "ressources/images/ether.png").convert()
        ImageManager.images["Needle"] = pygame.image.load(
            "ressources/images/needle.png").convert()
        ImageManager.images["gr"] = pygame.image.load(
            "ressources/images/but_du_jeu.png").convert()

    @staticmethod
    def get(name):
        return ImageManager.images[name]
