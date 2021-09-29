import math

class Line:
    def __init__(self):
        self(0,0,0,0)
    
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def getLength(self):
        return math.sqrt((self.x2 - self.x1) * (self.x2 - self.x1) + (self.y2 - self.y1) * (self.y2 - self.y1))

    def get_x1(self):
        return self.__x1
    
    def set_x1(self, x1):
        self.__x1 = x1

    def get_y1(self):
        return self.__y1
    
    def set_y1(self, y1):
        self.__y1 = y1

    def get_x2(self):
        return self.__x2
    
    def set_x2(self, x2):
        self.__x2 = x2

    def get_y2(self):
        return self.__y2
    
    def set_y2(self, y2):
        self.__y2 = y2

    x1 = property(get_x1, set_x1)
    y1 = property(get_y1, set_y1)

    x2 = property(get_x2, set_x2)
    y2 = property(get_y2, set_y2)

line = Line(1,1,4,3)
print(str(line.getLength()))
