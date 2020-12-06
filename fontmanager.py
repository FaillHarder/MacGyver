import pygame


class FontManager:
    Font = {}

    @staticmethod
    def load():
        FontManager.Font["title"] = pygame.font.Font(
            "ressources/font/heavycopper3d.ttf", 24)
        FontManager.Font["sq"] = pygame.font.Font(
            "ressources/font/Rounded_Elegance.ttf", 30)
        FontManager.Font["wl"] = pygame.font.Font(
            "ressources/font/Shiny_Signature.ttf", 30)
        FontManager.Font["obj"] = pygame.font.Font(
            "ressources/font/Rounded_Elegance.ttf", 12)

    @staticmethod
    def get(name):
        return FontManager.Font[name]
