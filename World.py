import ExplorationMode.Level as Level
import TowerDefenseMode.Exterior as Exterior

class World:
    def __init__(self):
        print("World Created")
        self.level = Level()
        self.exterior = Exterior()
        self.progressBar = 0
        self.combatTimer = 0

    def update(self):
        print("Updating World")
        #update everything here

