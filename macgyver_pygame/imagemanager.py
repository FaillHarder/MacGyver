from constant import WALL, MACGYVER, GUARDIAN, PATH, TUBE, ETHER, NEEDLE


class ImageManager:
    images = {}

    @staticmethod
    def __init__():
        ImageManager.images["Wall"] = WALL
        ImageManager.images["MacGyver"] = MACGYVER
        ImageManager.images["Guardian"] = GUARDIAN
        ImageManager.images["Path"] = PATH
        ImageManager.images["Tube"] = TUBE
        ImageManager.images["Ether"] = ETHER
        ImageManager.images["Needle"] = NEEDLE

    @staticmethod
    def get(name):
        return ImageManager.images[name]
