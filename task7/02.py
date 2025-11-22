'''
2. Below is a "random" iterator. It'll provide you with random numbers within `for` or `while` loop. You can stop by clicking `stop` button (which would call `KeyboardInterrupt` exception)
'''
import random

class RandomIterator:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def __next__(self) -> int:
        return random.randint(self.start, self.end)
    
    def __iter__(self) -> 'RandomIterator':
        return self