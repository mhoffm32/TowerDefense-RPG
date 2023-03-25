from TowerDefenseMode.Enemy import Enemy


class Enemy2(Enemy):
    def __init__(self, x, y, img_path, tower):
        super().__init__(x, y, img_path, tower, 40, 40)
        self.health = 50
        self.damage = 100
        self.speed = .15
        self.attackSpeed = 3
