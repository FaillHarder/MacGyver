from tile import Tile
from imagemanager import ImageManager


class Guardian(Tile):
    def __init__(self):
        super().__init__(ImageManager.get("Guardian"))
