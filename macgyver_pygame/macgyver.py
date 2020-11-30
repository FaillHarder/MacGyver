from tile import Tile
from imagemanager import ImageManager


class MacGyver(Tile):
    def __init__(self):
        super().__init__(ImageManager.get("MacGyver"))
