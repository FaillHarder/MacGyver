from macgyver import MacGyver


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
        for tile in liste:
            if isinstance(tile, MacGyver):
                x = liste.index(tile)
                return x

    @staticmethod
    def input_player():
        joueur = input("Taper 'L' pour quitter :\nTaper 'C' pour commencer : ")
        return joueur

    @staticmethod
    def input_move():
        destination = {"z": -15, "q": -1, "s": +15, "d": +1}
        joueur = input("Que voulez vous faire : ? ('z' pour up, 'q' pour left, 's' pour down, 'd' pour right : ")
        return destination[joueur]

    @staticmethod
    def message(key):
        messages = {"win": "Vous avez gagné",
                    "lose": "Game over, le Gardien vous a tué!!!",
                    "quit": "Au revoir",
                    "wall": "C'est un mur",
                    }
        print(messages[key])
