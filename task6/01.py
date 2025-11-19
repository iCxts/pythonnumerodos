'''
Write an “abstract” class, Box, and use it to define some methods which any box object should have:

    add, for adding any number of items to the box
    empty, for taking all the items out of the box and returning them as a list
    count, for counting the items which are currently in the box.

Write a simple Item class which has a name attribute and a value attribute – you can assume that all the items you will use will be Item objects. Now write two subclasses of Box which use different underlying collections to store items: ListBox should use a list, and DictBox should use a dict.

Write a function, repack_boxes, which takes any number of boxes as parameters, gathers up all the items they contain, and redistributes them as evenly as possible over all the boxes. Order is unimportant. There are multiple ways of doing this. Test your code with a ListBox with 20 items, a ListBox with 9 items and a DictBox with 5 items. You should end up with two boxes with 11 items each, and one box with 12 items.
'''

from abc import ABC, abstractmethod
from typing import List, Dict

class Item:
    def __init__(self, name: str, value: float) -> None:
        self.name = name
        self.value = value

class Box(ABC):
    @abstractmethod
    def add(self, *items: Item) -> None:
        pass
    
    @abstractmethod
    def empty(self) -> List[Item]:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

class ListBox(Box):
    def __init__(self) -> None:
        self._items: List[Item] = []
    
    def add(self, *items: Item) -> None:
        self._items.extend(items)
    
    def empty(self) -> List[Item]:
        items: List[Item] = self._items
        self._items = []
        return items
    
    def count(self) -> int:
        return len(self._items)

class DictBox(Box):
    def __init__(self) -> None:
        self._items: Dict[int, Item] = {}
        self._index = 0
    
    def add(self, *items: Item) -> None:
        for item in items:
            self._items[self._index] = item
            self._index += 1
    
    def empty(self) -> List[Item]:
        items = list(self._items.values())
        self._items = {}
        self._index = 0
        return items
    
    def count(self) -> int:
        return len(self._items)

def repack_boxes(*boxes: Box) -> None:
    if len(boxes) == 0:
        return
    
    all_items: List[Item] = []
    for box in boxes:
        all_items.extend(box.empty())
    
    base = len(all_items) // len(boxes)
    extra = len(all_items) % len(boxes)

    item_index = 0
    for index, box in enumerate(boxes):
        amount = base + (1 if index < extra else 0)
        batch = all_items[item_index: item_index + amount]
        item_index += amount
        box.add(*batch)

if __name__ == "__main__":
    items_20 = [Item(f"item_{i}", i) for i in range(20)]
    items_9 = [Item(f"item_{i+20}", i + 20) for i in range(9)]
    items_5 = [Item(f"item_{i+29}", i + 29) for i in range(5)]

    box1 = ListBox()
    box2 = ListBox()
    box3 = DictBox()

    box1.add(*items_20)
    box2.add(*items_9)    
    box3.add(*items_5)   

    print("Before repack:")
    print(box1.count(), box2.count(), box3.count())  

    repack_boxes(box1, box2, box3)

    print("After repack:")
    print(box1.count(), box2.count(), box3.count()) 



     
    

    
