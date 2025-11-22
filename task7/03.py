'''
Provide `RandomIterator`'s with `iterations_limit` argument. When loop hits `iterations_limit + 1`-th iteration – raise `StopIteration` exception within `__next__` method
'''
import random

class RandomIterator:
    def __init__(self, start: int, end: int, limit: int) -> None:
        self.start = start
        self.end = end
        self.limit = limit
        self.counter = 0

    def __next__(self) -> int:
        if self.counter >= self.limit:
            raise StopIteration
        self.counter += 1
        return random.randint(self.start, self.end)
    
    def __iter__(self) -> 'RandomIterator':
        self.counter = 0
        return self