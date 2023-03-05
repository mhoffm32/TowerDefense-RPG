
import GameObject

class Weapon(GameObject):
    def __init__(self,x,y,img_path):
        #initialize other weapon specific attributes
        super().__init__(x,y,img_path)

        #print("initialize Weapon")