'''
    Create class Person with attributes: name and age
    Create a display() method that displays the name and age
    Create a child class Student which inherits from the Person class and which also has a course attribute.
    Override method display() that displays the name, age and course of an object created via the Student class.
    Create a Student instance and test its display() method.
'''

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = str(name)
        if age <= 0:
            raise ValueError('Invalid age')
        self.age = age
    
    def display(self) -> None:
        print(f'Name: {self.name}, Age: {self.age}')
    
class Student(Person):
    def __init__(self, name: str, age: int, course: str) -> None:
        super().__init__(name, age)
        self.course = str(course)

    def display(self) -> None:
        print(f'Name: {self.name}, Age: {self.age}, Course: {self.course}')
