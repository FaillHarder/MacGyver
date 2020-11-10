from model import Model
from view import View
from controller import Controller


def main():

    game = True

    while game:
        # Création de la liste depuis model
        tiles = []
        Model.load_from_file(tiles)
        # Ajout aléatoire des objets
        Controller.random_object(tiles)
        # Choix entre quitter et commencer une partie
        game_choice = View.input_player()

        if game_choice == "L":
            View.message("quit")
            game = False
        elif game_choice == "C":
            party = True
            while party:
                # Labyrinthe dessiné dans la console
                View.draw(tiles)
                # Récupération des coordonnées de destination de macgyver
                destination = View.input_move()
                # Récupération de la position de macgyver
                macgyver = View.index_macgyver(tiles)
                Controller.move(tiles, macgyver, destination)
                if Controller.check_win(tiles, macgyver, destination) == "win":
                    View.message("win")
                    party = False
                    game_choice
                elif Controller.check_win(tiles, macgyver, destination) == "lose":
                    View.message("lose")
                    party = False
                    game_choice


if __name__ == "__main__":
    main()
