import pygame

pygame.init()

# Dictionary to associate characters with class names
MAPPING = {
    " ": "Path",
    "#": "Wall",
    "m": "MacGyver",
    "g": "Guardian"
    }

# Window
SCREEN = pygame.display.set_mode((300, 400))

# Dictionary of directional keys for move
BINDING_MOVE = {
    pygame.K_LEFT: -1,
    pygame.K_RIGHT: +1,
    pygame.K_DOWN: +15,
    pygame.K_UP: -15
    }


class Message:
    """Message use of the game"""
    TITLE = "MacGyver Maze"
    START = "Press 'S' for Start"
    CLOSE = "Press 'Q' for Start"
    WIN = "YOU WIN"
    LOSE = "YOU LOSE"


class Color:
    """Color use of the game"""
    BLUE = (3, 140, 252)
    CYAN = (0, 255, 255)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
