from constants import SCREEN


class Tile():
    """"""
    def __init__(self, image):
        self.image = image

    def draw(self, pos_x, pos_y):
        SCREEN.blit(self.image, (pos_x, pos_y))
