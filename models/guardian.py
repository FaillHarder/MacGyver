from .tile import Tile
from managers.imagemanager import ImageManager


class Guardian(Tile):
    def __init__(self):
        super().__init__(ImageManager.get("Guardian"))
