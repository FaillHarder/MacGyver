
# input

class View:

    # fonction permettant de print la liste en labyrinthe
    @staticmethod
    def print(tiles):
        """Return the labyrinthe in 15x15 """
        for x, tile in enumerate(tiles):
            print(tile, end="")
            if (x+1) % 15 == 0:
                print("")
