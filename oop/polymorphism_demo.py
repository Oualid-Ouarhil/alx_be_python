class shape:
    def area(self):
        raise NotImplementedError

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        import math
        return math.pi * self.radius **2 

