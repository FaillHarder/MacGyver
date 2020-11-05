from model import Model
from view import View


def main():
    tiles = []
    Model.load_from_file(tiles)
    while choice == 1:
        View.print(tiles)
        choice = View.input() #si 0 quitter, si autre chose, move.


if __name__ == "__main__":
    main()

