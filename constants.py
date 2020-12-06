import pygame

pygame.init()

MAPPING = {
    " ": "Path",
    "#": "Wall",
    "m": "MacGyver",
    "g": "Guardian"
    }

# Window
SCREEN = pygame.display.set_mode((300, 400))

TITLE = "MacGyver Maze"
START = "Press 'S' for Start"
CLOSE = "Press 'Q' for Start"
WIN = "YOU WIN"
LOSE = "YOU LOSE"
BLUE = (3, 140, 252)
BLUE2 = (0, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RECTANGLE = pygame.rect.Rect(0, 50, 300, 50)

# Win/lose sound
WIN_SOUND = pygame.mixer.Sound("ressources/audio/Victory.mp3")
LOSE_SOUND = pygame.mixer.Sound("ressources/audio/game_over.mp3")
