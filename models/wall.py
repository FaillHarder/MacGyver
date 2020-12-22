from managers.imagemanager import ImageManager
from .tile import Tile


class Wall(Tile):
    def __init__(self,):
        super().__init__(ImageManager.get("Wall"))
