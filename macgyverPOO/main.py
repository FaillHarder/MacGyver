from model import Model
from view import View
from controller import Controller

# run win lose
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
                win_state = Controller.check_win(tiles, macgyver, destination)
                if win_state:
                    View.message(win_state)
                    party = False
                    View.input_player()
                


if __name__ == "__main__":
    main()
