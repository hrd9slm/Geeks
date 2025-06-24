import math

class Circle:
    def __init__(self, *, radius=None, diameter=None):
        if radius is not None:
            self._radius = radius
        elif diameter is not None:
            self._radius = diameter / 2
        else:
            raise ValueError("You must specify either radius or diameter")

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return math.pi * self._radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __le__(self, other):
        return self == other or self < other
if __name__=="__main__":
    c1 = Circle(radius=3)
    c2 = Circle(diameter=10)

    print(c1)  
    print(c2)  

    c3 = c1 + c2
    print(c3)  

    print(c1 == c2)   
    print(c1 < c2)    

    circles = [c2, c3, c1]
    circles.sort()
    for c in circles:
        print(c)
