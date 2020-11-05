from tile import Tile


class Objects(Tile):
    def __repr__(self):
        return ""


class Needle(Objects):
    def __repr__(self):
        return "1"


class Tube(Objects):
    def __repr__(self):
        return "2"


class Ether(Objects):
    def __repr__(self):
        return "3"
