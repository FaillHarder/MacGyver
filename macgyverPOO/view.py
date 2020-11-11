from macgyver import MacGyver
# draw interface
# image se charge une seul fois


class View:

    # méthode permettant de print la liste en labyrinthe
    @staticmethod
    def draw(tiles):
        """Return the labyrinthe in 15x15 """
        for x, tile in enumerate(tiles):
            print(tile, end="")
            if (x+1) % 15 == 0:
                print("")

    @staticmethod
    def index_macgyver(liste):
        """Méthode permettant de récuprérer l'index de macgyver dans la liste"""
        for pos, tile in enumerate(liste):
            if isinstance(tile, MacGyver):
                return pos

    # a supprimer
    @staticmethod
    def input_player():
        return input("Taper 'L' pour quitter :\nTaper 'C' pour commencer : ")

    @staticmethod
    def input_move(key):
        destination = {"z": -15, "q": -1, "s": +15, "d": +1}
        return destination[key]

    @staticmethod
    def message(key):
        messages = {"win": "Vous avez gagné",
                    "lose": "Game over, le Gardien vous a tué!!!",
                    "quit": "Au revoir",
                    "wall": "C'est un mur",
                    }
        print(messages[key])
