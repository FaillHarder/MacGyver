from view import View
from macgyver import MacGyver
from guardian import Guardian
from path import Path
from objects import Objects
from objects import Needle, Ether, Tube
from random import choice


# gérer états du jeu : running (fléches de déplacment)
#                      win
#                      lose
# conditions victoire
# placement des items
# déplacements


class Controller:

    counter_object = 0

    @staticmethod
    def random_object(maze):
        """Méthode générant aléatoirement les objets needle, tube, ether
            dans le labyrinthe"""
        index_path = []
        object_list = [Needle(), Tube(), Ether()]
        for tile in maze:
            if isinstance(tile, Path):
                index = maze.index(tile)
                index_path.append(index)
        for objects in object_list:
            object_index = choice(index_path)
            maze[object_index] = objects
            index_path.remove(object_index)
        return maze

    @staticmethod
    def move(maze, index_macgyver, destination):
        """Méthode permétant de déplacer macgyver. Prend en paramètre
            le labyrinthe, la position de macgyver et sa destination
            via View.input_move()"""
        if isinstance(maze[index_macgyver+(destination)], Path):
            maze[index_macgyver+(destination)] = MacGyver()
            maze[index_macgyver] = Path()
        elif isinstance(maze[index_macgyver+(destination)], Objects):
            maze[index_macgyver+(destination)] = MacGyver()
            maze[index_macgyver] = Path()
            Controller.counter_object += 1
            print("Macgyver à ramassé {} object.".format(
                Controller.counter_object
            ))
        else:
            View.message("wall")

    @staticmethod
    def check_win(maze, index_macgyver, destination):
        """Méthode permétant de voir si macgyver gagne ou perd
            la partie"""
        if isinstance(maze[index_macgyver+(destination)], Guardian):
            if Controller.counter_object == 3:
                Controller.counter_object = 0
                return "win"
            else:
                Controller.counter_object = 0
                return "lose"
