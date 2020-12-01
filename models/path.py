from .tile import Tile
from imagemanager import ImageManager


class Path(Tile):
    def __init__(self):
        super().__init__(ImageManager.get("Path"))
