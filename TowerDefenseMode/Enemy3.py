from TowerDefenseMode.Enemy import Enemy

class Enemy3(Enemy):
   def __init__(self, x, y, img_path, tower):
        super().__init__(x, y, img_path, tower, 50, 50)
        self.health = 500
        self.damage = 100
        self.speed = .02
        self.attackSpeed = 3