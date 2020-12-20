import math

class CordinatesStruct:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def display_cord(self):
        vector = [self.x, self.y]
        return vector

    def calucate_dist(self, obj):
        return math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)


