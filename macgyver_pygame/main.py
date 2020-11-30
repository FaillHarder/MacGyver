from model import Model
from view import View
from controller import Controller
from imagemanager import ImageManager
import pygame
from constants import (
    SCREEN, GAME_TITLE, START_TEXT, QUIT_TEXT, GAME_RULE,
    WIN_TEXT, LOSE_TEXT, COUNT_0, COUNT_1, COUNT_2, COUNT_3,
    WIN_SOUND, LOSE_SOUND
    )


def main():
    pygame.init()
    ImageManager.__init__()
    black = (0, 0, 0)
    rectangle = pygame.rect.Rect(0, 50, 300, 50)
    rectangle2 = pygame.rect.Rect(0, 85, 300, 14)

    # Creation of the tile list
    tiles = []
    Model.load_from_file(tiles)
    # Add needle tube ether in the list
    Controller.random_object(tiles)

    continuer = True
    start = True
    game = True
    while continuer:
        pygame.time.Clock().tick(30)
        # Display start/quit/game rule
        if start:
            View.blit_text(SCREEN, GAME_TITLE, 10, 10)
            View.blit_text(SCREEN, START_TEXT, 35, 50)
            View.blit_text(SCREEN, QUIT_TEXT, 32, 80)
            View.blit_image(SCREEN, GAME_RULE, 0, 150)
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
                        View.blit_text(SCREEN, COUNT_0, 5, 85)
                        # Index de macgyver recovery
                        index_mac = View.index_macgyver(tiles)
                        # Draw maze (pos x = 0, y = 100)
                        View.draw(tiles, 0, 100)
                        # Blit counter "objet ramassé 1/2/3"
                        if Controller.counter_object == 1:
                            pygame.draw.rect(SCREEN, black, rectangle2)
                            View.blit_text(SCREEN, COUNT_1, 5, 85)
                        elif Controller.counter_object == 2:
                            pygame.draw.rect(SCREEN, black, rectangle2)
                            View.blit_text(SCREEN, COUNT_2, 5, 85)
                        elif Controller.counter_object == 3:
                            pygame.draw.rect(SCREEN, black, rectangle2)
                            View.blit_text(SCREEN, COUNT_3, 5, 85)
                        # Event Quit and move
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                game = False
                                continuer = False
                            elif event.type == pygame.KEYDOWN:
                                # Dictionary of directional keys for move
                                list_move = {
                                    pygame.K_LEFT: -1,
                                    pygame.K_RIGHT: +1,
                                    pygame.K_DOWN: +15,
                                    pygame.K_UP: -15
                                    }
                                for key in list_move:
                                    if event.key == key:
                                        Controller.move(
                                            tiles, index_mac, list_move[key])
                                print(index_mac)
                            # Check win
                            win_state = Controller.check_win(tiles, index_mac)
                            if win_state == "win":
                                WIN_SOUND.play().set_volume(0.2)
                                View.blit_text(SCREEN, WIN_TEXT, 90, 50)
                                game = False
                                start = False
                            elif win_state == "lose":
                                LOSE_SOUND.play().set_volume(0.1)
                                View.blit_text(SCREEN, LOSE_TEXT, 75, 50)
                                game = False
                                start = False
                        pygame.display.flip()
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
