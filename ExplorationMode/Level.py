from ExplorationMode.SubArea.SubArea import SubArea

class Level:
    def __init__(self, screen, progressBar):
        print("Initialize Level")
        self.screen = screen
        self.room = SubArea(0, self.screen, progressBar, 0)

    def update(self):
        self.room.update()


