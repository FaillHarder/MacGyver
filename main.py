from model import Model
from view import View
from controller import Controller
from imagemanager import ImageManager
from fontmanager import FontManager as ft
import pygame
from constants import (
    SCREEN, WIN_SOUND, LOSE_SOUND, TITLE, START, CLOSE,
    WIN, LOSE, BLUE, BLUE2, RED, BLACK, WHITE, RECTANGLE
    )


def main():
    pygame.init()
    ImageManager.load()
    ft.load()
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
    state = "rules"
    while continuer:
        pygame.time.Clock().tick(30)
        # Display start/quit/game rule
        if state == "rules":
            View.blit_text(SCREEN, ft.get("title"), TITLE, BLUE, 10, 5)
            View.blit_text(SCREEN, ft.get("sq"), START, BLUE2, 35, 50)
            View.blit_text(SCREEN, ft.get("sq"), CLOSE, BLUE2, 32, 80)
            View.blit_img(SCREEN, ImageManager.get("gr"), 0, 150)
            # Event pygame Quit or Start
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        continuer = False
                    elif event.key == pygame.K_s:
                        state = "running"
        if state == "running":
            # Black rectangle over a Start/Quit
            pygame.draw.rect(SCREEN, BLACK, RECTANGLE)
            # Draw maze (pos x = 0, y = 100)
            View.draw(tiles, 0, 100)
            # Blit counter "objet ramassé"
            ojb_pick = (f"Objet ramassé : {Controller.counter_object}")
            View.blit_text(SCREEN, ft.get("obj"), ojb_pick, WHITE, 5, 85)
            index_mac = View.index_macgyver(tiles)
            # Event Quit and move
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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
                View.blit_text(SCREEN, ft.get("wl"), WIN, BLUE2, 90, 50)
                state = "win"
            elif win_state == "lose":
                LOSE_SOUND.play().set_volume(0.1)
                View.blit_text(SCREEN, ft.get("wl"), LOSE, RED, 75, 50)
                state = "lose"
        if state == "win" or state == "lose":
            pygame.display.flip()
            continuer = False
            pygame.time.wait(4000)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
