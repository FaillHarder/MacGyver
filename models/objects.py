from .tile import Tile
from managers.imagemanager import ImageManager


class Objects(Tile):
    def __init__(self, image):
        self.image = image


class Needle(Objects):
    def __init__(self):
        super().__init__(ImageManager.get("Needle"))


class Tube(Objects):
    def __init__(self):
        super().__init__(ImageManager.get("Tube"))


class Ether(Objects):
    def __init__(self):
        super().__init__(ImageManager.get("Ether"))
