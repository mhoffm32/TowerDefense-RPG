from TowerDefenseMode.Enemy import Enemy



class Enemy1(Enemy):
    def __init__(self, x, y, img_path, tower):
        super().__init__(x, y, img_path, tower, 20, 20)
        self.health = 100
        self.damage = 5
        self.speed = .2
        self.attackSpeed = .5

        #print("initialize Enemy Type 1")
