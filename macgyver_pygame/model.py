from constants import MAPPING
from path import Path
from wall import Wall
from guardian import Guardian
from macgyver import MacGyver
from tile import Tile

# vérif si il y a 225 char


class Model:

    @staticmethod
    def load_from_file(tiles):
        """Méthode permettant d'instancier les caractères du fichiertxt"""
        with open("maze.txt", "r") as infile:
            data = infile.read().replace("\n", "")
            for char in data:
                tile_class_name = MAPPING[char]
                tile_class = globals()[tile_class_name]
                tiles.append(tile_class())
