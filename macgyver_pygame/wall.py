from tile import Tile
from imagemanager import ImageManager


class Wall(Tile):
    def __init__(self,):
        super().__init__(ImageManager.get("Wall"))
