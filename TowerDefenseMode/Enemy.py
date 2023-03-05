import Character


class Enemy(Character):
    def __init__(self, x, y, img_path):
        # initialize other enemy specific attributes
        super().__init__(x, y, img_path)

        #print("initialize Enemy")
