'''
<<<<<<< HEAD
1. Pretend there is no way to get i-th element of the list. Also we don't know how to use `for` loop. Given that, print the 3rd element from `['a', 'b', 'c']` list
'''
sample = ['a', 'b', 'c']

it = iter(sample)
it.__next__()
it.__next__()
third_element = it.__next__()
print(third_element)
=======
Write a function cut_suffix which takes a string and a suffix. A function should return this string without the given suffix.

cut_suffix("foobar", "bar")
>>> "foo"

cut_suffix("foobar", "boo")
>>> "foobar"
'''
def cut_suffix(word: str, suffix: str) -> str:
    return word.removesuffix(suffix)

>>>>>>> bd86a8bab30c1319eb447da262f2835cd0021dfc
