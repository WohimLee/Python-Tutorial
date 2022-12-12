
import time

class BBox:
    def __init__(self, l, t, r, b):
        self.l = l
        self.t = t
        self.r = r
        self.b = b
    
    @property
    def width(self):
        return self.r - self.l + 1

    def func1(self):
        self.width
        pass

    def func2(self):
        pass

if __name__ == "__main__":
    bbox = BBox(0, 0, 15, 8)
    print(bbox.width)