from models.macgyver import MacGyver
from models.guardian import Guardian
from models.path import Path
from models.objects import Objects
from models.objects import Needle, Ether, Tube
from random import choice


class Controller:

    counter_object = 0

    @staticmethod
    def random_object(maze):
        """Method that randomly generates needle, tube, ether
            in the labyrinth. Takes as parameter list_maze"""
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
        """Method allowing to move macgyver. Takes as parameter
            list_maze, macgyver position and destination"""
        destination_tile = (index_macgyver + destination)
        if (index_macgyver % 15 == 0 and destination == -1 or
            index_macgyver % 15 == 14 and destination == 1 or
            index_macgyver < 15 and destination == -15 or
                index_macgyver > 210 and destination == 15):
            print("Attention au vide!!")
        elif isinstance(maze[destination_tile], Path):
            maze[destination_tile] = MacGyver()
            maze[index_macgyver] = Path()
        elif isinstance(maze[destination_tile], Objects):
            maze[destination_tile] = MacGyver()
            maze[index_macgyver] = Path()
            Controller.counter_object += 1
        else:
            print("c'est un mur")

    @staticmethod
    def check_win(maze, index_macgyver):
        """Method to check if macgyver wins or loses"""
        destination = {"up": +15, "down": -15, "left": -1, "right": +1}
        for key in destination:
            mac_position = index_macgyver+(destination[key])
            if index_macgyver + destination[key] <= 225:
                if isinstance(maze[mac_position], Guardian):
                    if Controller.counter_object == 3:
                        return "win"
                    else:
                        return "lose"