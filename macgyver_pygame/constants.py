import pygame
MAPPING = {
    " ": "Path",
    "#": "Wall",
    "m": "MacGyver",
    "g": "Guardian"
    }


screen = pygame.display.set_mode((300, 400))
image = pygame.image.load("ressource/floor-tiles-20x20.png").convert_alpha()
path = image.subsurface(pygame.Rect(60, 240, 20, 20))
wall = image.subsurface(pygame.Rect(140, 220, 20, 20))
macgyver = pygame.image.load("ressource/macgyver.png").convert()
macgyver = pygame.transform.scale(macgyver, (20, 20))
guardian = pygame.image.load("ressource/Gardien.png").convert()
guardian = pygame.transform.scale(guardian, (20, 20))
needle = pygame.image.load("ressource/seringue.png").convert()
needle = pygame.transform.scale(needle, (20, 20))
tube = pygame.image.load("ressource/tube_plastique.png").convert()
tube = pygame.transform.scale(tube, (20, 20))
ether = pygame.image.load("ressource/ether.png").convert()
ether = pygame.transform.scale(ether, (20, 20))