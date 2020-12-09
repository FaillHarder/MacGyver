import pygame


class FontManager:
    font = {}

    @classmethod
    def load(cls):
        cls.font["title"] = pygame.font.Font(
            "ressources/font/heavycopper3d.ttf", 24)
        cls.font["sq"] = pygame.font.Font(
            "ressources/font/Rounded_Elegance.ttf", 30)
        cls.font["wl"] = pygame.font.Font(
            "ressources/font/Shiny_Signature.ttf", 30)
        cls.font["obj"] = pygame.font.Font(
            "ressources/font/Rounded_Elegance.ttf", 12)

    @classmethod
    def get(cls, name):
        return cls.font[name]
