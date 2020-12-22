from managers.imagemanager import ImageManager
from .tile import Tile


class MacGyver(Tile):
    def __init__(self):
        super().__init__(ImageManager.get("MacGyver"))
