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

# Image but du jeu
GAME_RULE = pygame.image.load("ressources/images/but_du_jeu.png").convert()

# Game title
title_font = pygame.font.Font("ressources/font/heavycopper3d.ttf", 24)
GAME_TITLE = title_font.render("MacGyver Maze", True, (3, 140, 252))
# Start/Quit text
text_font = pygame.font.Font(
    "ressources/font/Rounded_Elegance.ttf", 30)
START_TEXT = text_font.render("Press 'S' for Start", True, (2, 180, 255))
QUIT_TEXT = text_font.render("Press 'Q' for Quit", True, (0, 255, 255))
# Texte compteur d'objet
object_font = pygame.font.Font(
    "ressources/font/Rounded_Elegance.ttf", 12)
COUNT_0 = object_font.render("Objet ramassé : 0", True, (255, 255, 255))
COUNT_1 = object_font.render("Objet ramassé : 1", True, (255, 255, 255))
COUNT_2 = object_font.render("Objet ramassé : 2", True, (255, 255, 255))
COUNT_3 = object_font.render("Objet ramassé : 3", True, (255, 255, 255))
# Win/lose text
win_lose_font = pygame.font.Font("ressources/font/Shiny_Signature.ttf", 30)
WIN_TEXT = win_lose_font.render("YOU WIN", True, (0, 255, 255))
LOSE_TEXT = win_lose_font.render("YOU LOSE", True, (255, 0, 0))

# Win/lose sound
WIN_SOUND = pygame.mixer.Sound("ressources/audio/Victory.mp3")
LOSE_SOUND = pygame.mixer.Sound("ressources/audio/game_over.mp3")
