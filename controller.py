from models.guardian import Guardian
from models.macgyver import MacGyver
from models.objects import Objects, Tube, Needle, Ether
from models.path import Path

from random import choice


class Controller:

    counter_object = 0

    @staticmethod
    def randomize_objects(maze):
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
            pass
        elif isinstance(maze[destination_tile], Path):
            maze[destination_tile] = MacGyver()
            maze[index_macgyver] = Path()
        elif isinstance(maze[destination_tile], Objects):
            maze[destination_tile] = MacGyver()
            maze[index_macgyver] = Path()
            Controller.counter_object += 1

    @staticmethod
    def check_win(maze, index_macgyver):
        """Method to check if macgyver wins or loses"""
        destination = {"up": +15, "down": -15, "left": -1, "right": +1}
        for key in destination:
            mac_position = index_macgyver+(destination[key])
            if index_macgyver + destination[key] <= 225:
                if isinstance(maze[mac_position], Guardian):
                    return "win" if Controller.counter_object == 3 else "lose"
        return "running"
