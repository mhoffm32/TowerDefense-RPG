
import GameObject

class Troop(GameObject):
    def __init__(self,x,y,img_path):
        #initialize other troop specific attributes
        super().__init__(x,y,img_path)