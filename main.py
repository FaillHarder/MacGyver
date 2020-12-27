from controller import Controller
from model import Model
from managers.imagemanager import ImageManager
from managers.fontmanager import FontManager
from managers.soundmanager import SoundManager
from view import View
from constants import SCREEN, BINDING_MOVE

import pygame


def main():
    pygame.init()
    # Ressources loading
    ImageManager.load()
    FontManager.load()
    SoundManager.load()
    # loading of the maze
    tiles = []
    Model.load_from_file(tiles)
    Controller.randomize_objects(tiles)
    # States of the game
    state = "rules"
    while True:
        pygame.time.Clock().tick(30)
        # Display
        SCREEN.fill((0, 0, 0))
        View.draw_title()
        if state == "rules":
            View.draw_rules()
        else:
            View.draw_maze(tiles)
            View.draw_picked_objects(Controller.counter_object)
            if state == "win":
                View.draw_win_message()
            elif state == "lose":
                View.draw_lose_message()
        pygame.display.flip()
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if state == "rules":
                    if event.key == pygame.K_q:
                        return
                    elif event.key == pygame.K_s:
                        state = "running"
                elif state == "running":
                    if event.key in BINDING_MOVE:
                        Controller.move(
                            tiles, View.index_macgyver(tiles),
                            BINDING_MOVE[event.key]
                            )
        # Logics
        if state == "running":
            state = Controller.check_win(tiles, View.index_macgyver(tiles))
        elif state in ("win", "lose"):
            SoundManager.get(state).play().set_volume(0.1)
            pygame.time.wait(4000)
            break


if __name__ == "__main__":
    main()
    pygame.quit()
