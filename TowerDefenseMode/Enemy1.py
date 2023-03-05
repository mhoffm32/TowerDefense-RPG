import Enemy


class Enemy1(Enemy):
    def __init__(self, x, y):
        img_path = ''

        super().__init__(x, y, img_path)

        #print("initialize Enemy Type 1")
