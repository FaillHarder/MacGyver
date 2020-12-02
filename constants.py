import pygame

pygame.init()

MAPPING = {
    " ": "Path",
    "#": "Wall",
    "m": "MacGyver",
    "g": "Guardian"
    }

# Fenetre du jeu
SCREEN = pygame.display.set_mode((300, 400))

# Texte compteur d'objet
object_font = pygame.font.Font(
    "ressources/font/Rounded_Elegance.ttf", 12)

COUNT_1 = object_font.render("Objet ramassé : 1", True, (255, 255, 255))
COUNT_2 = object_font.render("Objet ramassé : 2", True, (255, 255, 255))
COUNT_3 = object_font.render("Objet ramassé : 3", True, (255, 255, 255))

# Win/lose sound
WIN_SOUND = pygame.mixer.Sound("ressources/audio/Victory.mp3")
LOSE_SOUND = pygame.mixer.Sound("ressources/audio/game_over.mp3")
