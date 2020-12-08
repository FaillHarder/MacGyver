from model import Model
from view import View
from controller import Controller
from managers.imagemanager import ImageManager
from managers.fontmanager import FontManager
from managers.soundmanager import SoundManager
import pygame
from constants import SCREEN, WIN, LOSE, BLUE2, RED, BLACK, WHITE, RECTANGLE, BINDING_MOVE


def main():
    pygame.init()
    ImageManager.load()
    FontManager.load()
    SoundManager.load()
    # Creation of the tile list
    tiles = []
    Model.load_from_file(tiles)
    # Add needle tube ether in the list
    Controller.random_object(tiles)
    continuer = True
    state = "rules"
    while continuer:
        pygame.time.Clock().tick(30)
        # Display start/quit/game rule
        if state == "rules":
            View.draw_rules()
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
            View.blit_text(FontManager.get("obj"), ojb_pick, WHITE, 5, 85)
            index_mac = View.index_macgyver(tiles)
            # Event Quit and move
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continuer = False
                elif event.type == pygame.KEYDOWN:
                    for key in BINDING_MOVE:
                        if event.key == key:
                            Controller.move(
                                tiles, index_mac, BINDING_MOVE[key])
            # Check win
            win_state = Controller.check_win(tiles, index_mac)
            if win_state == "win":
                SoundManager.get("win").play().set_volume(0.2)
                View.blit_text(FontManager.get("wl"), WIN, BLUE2, 90, 50)
                state = "win"
            elif win_state == "lose":
                SoundManager.get("lose").play().set_volume(0.1)
                View.blit_text(FontManager.get("wl"), LOSE, RED, 75, 50)
                state = "lose"
        if state == "win" or state == "lose":
            pygame.display.flip()
            continuer = False
            pygame.time.wait(4000)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
