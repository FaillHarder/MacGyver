class Tuile:
    def init(self, image):
        self.image = image
    def draw(self, window, x, y):
        window.blit(self.image, [x, y])


class McGyver(Tuile):
    def init(self):
        super().init(self, ImageManager.get("McGyver"))


class Wall(Tuile):
    def init(self):
        super().init(self, ImageManager.get("Wall"))


class ImageManager:
    images = {}
    @staticmethod
    def init():
        images["McGyver"] = pygame.image.load("/img/mac_gyver.png")
        images["Wall"] = pygame.image.load("/img/wall.png")
    @staticmethod
    def get(name):
        return images[name]


ImageManager.init()
tuiles = []
tuiles.append(McGyver())
tuiles.append(Wall())

for tuile in tuiles:
    tuile.draw()

if isinstance(tuile, Objet):
    pass