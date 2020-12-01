
class Tile():

    def __init__(self, image):
        self.image = image

    def draw(self, screen, pos_x, pos_y):
        screen.blit(self.image, (pos_x, pos_y))
