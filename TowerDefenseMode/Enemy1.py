from TowerDefenseMode.Enemy import Enemy



class Enemy1(Enemy):
    def __init__(self, x, y, img_path, tower):
        super().__init__(x, y, img_path, tower)
        self.health = 100

        #print("initialize Enemy Type 1")
