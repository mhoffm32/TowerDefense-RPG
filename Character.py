from GameObject import GameObject 


class Character(GameObject):

    def __init__(self, x, y, img):
        # initialize other character specific attributes
        super().__init__(x, y, img)

    # def move(self)
