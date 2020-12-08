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

# Dictionary of directional keys for move
BINDING_MOVE = {
    pygame.K_LEFT: -1,
    pygame.K_RIGHT: +1,
    pygame.K_DOWN: +15,
    pygame.K_UP: -15
    }
