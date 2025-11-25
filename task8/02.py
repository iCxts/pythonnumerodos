'''
<<<<<<< HEAD
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
=======
Write a function boxed which takes a string and two arguments: a symbol fill and a number pad. A result of the boxed function execution should be a string surrounded by fill symbols as it’s shown in the example.

print(boxed("Hello world", fill="*", pad=2))
print(boxed("Fishy", fill="#", pad=1))
result:

*****************
** Hello world **
*****************

#########
# Fishy #
#########
'''
def boxed(text: str, fill: str = "*", pad: int = 1) -> str:
    inner = f" {text} "
    side = fill * pad
    middle = f"{side}{inner}{side}"
    border = fill * len(middle)
    return "\n".join([border, middle, border])


>>>>>>> bd86a8bab30c1319eb447da262f2835cd0021dfc
