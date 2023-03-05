import Weapon


class Cannon(Weapon):
    def __init__(self, x, y):
        img_path = ''

        super().__init__(x, y, img_path)
