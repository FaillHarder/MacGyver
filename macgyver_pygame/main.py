from model import Model
from view import View
from controller import Controller
from constants import screen
import pygame

pygame.init()

police_title = pygame.font.Font("ressource/heavy_copper/heavycopper3d.ttf", 24)
game_title = police_title.render("MacGyver Maze", True, (19, 77, 85))
police_text = pygame.font.Font(
    "ressource/heavy_copper/PoetsenOne-Regular.ttf", 30)

start_text = police_text.render("Press 'F' for start", True, (255, 255, 255))
black = (0, 0, 0)
rectangle = pygame.rect.Rect(0, 50, 300, 50)


tiles = []
Model.load_from_file(tiles)
Controller.random_object(tiles)

continuer = True
game = True
while continuer:
    View.draw(tiles, 0, 100)
    screen.blit(game_title, (10, 10))
    screen.blit(start_text, (35, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                while game:
                    pygame.draw.rect(screen, black, rectangle)
                    View.draw(tiles, 0, 100)
                    index_mac = View.index_macgyver(tiles)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game = False
                            continuer = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                Controller.move(tiles, index_mac, -1)
                            elif event.key == pygame.K_RIGHT:
                                Controller.move(tiles, index_mac, +1)
                            elif event.key == pygame.K_DOWN:
                                Controller.move(tiles, index_mac, +15)
                            elif event.key == pygame.K_UP:
                                Controller.move(tiles, index_mac, -15)
                        win_state = Controller.check_win(tiles, index_mac, +1)
                        if win_state:
                            game = False
                    pygame.display.flip()
    pygame.display.flip()
pygame.quit()
