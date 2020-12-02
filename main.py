from model import Model
from view import View
from controller import Controller
from imagemanager import ImageManager
from textmanager import TextManager
import pygame
from constants import (
    SCREEN, COUNT_1,
    COUNT_2, COUNT_3, WIN_SOUND, LOSE_SOUND
    )


def main():
    pygame.init()
    ImageManager.load()
    TextManager.load()
    black = (0, 0, 0)
    rectangle = pygame.rect.Rect(0, 50, 300, 50)
    rectangle2 = pygame.rect.Rect(0, 85, 300, 14)

    # Creation of the tile list
    tiles = []
    Model.load_from_file(tiles)
    # Add needle tube ether in the list
    Controller.random_object(tiles)
    # Dictionary of directional keys for move
    list_move = {
        pygame.K_LEFT: -1,
        pygame.K_RIGHT: +1,
        pygame.K_DOWN: +15,
        pygame.K_UP: -15
        }
    continuer = True
    start = True
    game = True
    while continuer:
        pygame.time.Clock().tick(30)
        # Display start/quit/game rule
        if start:
            View.blit(SCREEN, TextManager.get("gt"), 10, 10)
            View.blit(SCREEN, TextManager.get("st"), 35, 50)
            View.blit(SCREEN, TextManager.get("qt"), 32, 80)
            View.blit(SCREEN, ImageManager.get("gr"), 0, 150)
        # Event pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    continuer = False
                elif event.key == pygame.K_s:
                    while game:
                        # Black rectangle over a Start/Quit
                        pygame.draw.rect(SCREEN, black, rectangle)
                        # Blit counter "objet ramassé"
                        View.blit(SCREEN, TextManager.get("c0"), 5, 85)
                        # Index de macgyver recovery
                        index_mac = View.index_macgyver(tiles)
                        # Draw maze (pos x = 0, y = 100)
                        View.draw(tiles, 0, 100)
                        # Blit counter "objet ramassé 1/2/3"
                        if Controller.counter_object == 1:
                            pygame.draw.rect(SCREEN, black, rectangle2)
                            View.blit(SCREEN, COUNT_1, 5, 85)
                        elif Controller.counter_object == 2:
                            pygame.draw.rect(SCREEN, black, rectangle2)
                            View.blit(SCREEN, COUNT_2, 5, 85)
                        elif Controller.counter_object == 3:
                            pygame.draw.rect(SCREEN, black, rectangle2)
                            View.blit(SCREEN, COUNT_3, 5, 85)
                        # Event Quit and move
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                game = False
                                continuer = False
                            elif event.type == pygame.KEYDOWN:
                                for key in list_move:
                                    if event.key == key:
                                        Controller.move(
                                            tiles, index_mac, list_move[key])
                            # Check win
                            win_state = Controller.check_win(tiles, index_mac)
                            if win_state == "win":
                                WIN_SOUND.play().set_volume(0.2)
                                View.blit(SCREEN, TextManager.get("wt"), 90, 50)
                                game = False
                                start = False
                            elif win_state == "lose":
                                LOSE_SOUND.play().set_volume(0.1)
                                View.blit(SCREEN, TextManager.get("lt"), 75, 50)
                                game = False
                                start = False
                        pygame.display.flip()
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
