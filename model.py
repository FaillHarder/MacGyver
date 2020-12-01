from constants import MAPPING
from models.path import Path
from models.wall import Wall
from models.guardian import Guardian
from models.macgyver import MacGyver
from models.tile import Tile


class Model:

    @staticmethod
    def load_from_file(tiles):
        """Method allowing to instantiate the characters of the file txt"""
        with open("ressources/maze.txt", "r") as infile:
            data = infile.read().replace("\n", "")
            for char in data:
                tile_class_name = MAPPING[char]
                tile_class = globals()[tile_class_name]
                tiles.append(tile_class())
