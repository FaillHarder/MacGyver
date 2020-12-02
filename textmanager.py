import pygame


class TextManager:
    text = {}
    title_font = pygame.font.Font("ressources/font/heavycopper3d.ttf", 24)
    text_font = pygame.font.Font("ressources/font/Rounded_Elegance.ttf", 30)
    win_lose_font = pygame.font.Font("ressources/font/Shiny_Signature.ttf", 30)
    object_font = pygame.font.Font("ressources/font/Rounded_Elegance.ttf", 12)
    

    @staticmethod
    def load():
        TextManager.text["gt"] = TextManager.title_font.render(
            "MacGyver Maze", True, (3, 140, 252))
        TextManager.text["st"] = TextManager.text_font.render(
            "Press 'S' for Start", True, (2, 180, 255))
        TextManager.text["qt"] = TextManager.text_font.render(
            "Press 'Q' for Quit", True, (0, 255, 255))
        TextManager.text["wt"] = TextManager.win_lose_font.render(
            "YOU WIN", True, (0, 255, 255))
        TextManager.text["lt"] = TextManager.win_lose_font.render(
            "YOU LOSE", True, (255, 0, 0))
        TextManager.text["c0"] = TextManager.object_font.render(
            "Objet ramassé : 0", True, (255, 255, 255))

    @staticmethod
    def get(name):
        return TextManager.text[name]
