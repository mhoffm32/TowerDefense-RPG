import GameObject


class Character(GameObject):

    def __init__(self, x, y, img_path):
        # initialize other character specific attributes
        super().__init__(x, y, img_path)

    # def move(self)
