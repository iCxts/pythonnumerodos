#Create a Cricle class and intialize it with radius. Make two methods get_area and get_circumference inside this class. Try thinking about what properties should be of class and which should be of instances, which should be public and which should be private.
import math
class Circle:
    def __init__(self, radius: float) -> None:
        if radius <= 0:
             raise ValueError("radius must be positive")
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * (self.radius ** 2)
    
    def get_circumference(self) -> float:
        return 2 * math.pi * self.radius
    