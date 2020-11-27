from constants import MAPPING
from path import Path
from wall import Wall
from guardian import Guardian
from macgyver import MacGyver
from tile import Tile


class Model:

    @staticmethod
    def load_from_file(tiles):
        """Method allowing to instantiate the characters of the file txt"""
        with open("maze.txt", "r") as infile:
            data = infile.read().replace("\n", "")
            for char in data:
                tile_class_name = MAPPING[char]
                tile_class = globals()[tile_class_name]
                tiles.append(tile_class())
