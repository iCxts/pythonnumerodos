#Write a Python class named Rectangle constructed by a length and width and methods which will compute the area of a rectangle, and another method that calculate the perimeter.
class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        if length <= 0 or width <= 0:
            raise ValueError("length and width must be positive")
        self.length = length
        self.width = width
    
    def get_area(self) -> float:
        return self.length * self.width
    
    def get_perimeter(self) -> float:
        return 2 * (self.length + self.width)