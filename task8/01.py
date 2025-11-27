'''
Write a function cut_suffix which takes a string and a suffix. A function should return this string without the given suffix.

cut_suffix("foobar", "bar")
>>> "foo"

cut_suffix("foobar", "boo")
>>> "foobar"
'''
def cut_suffix(word: str, suffix: str) -> str:
    return word.removesuffix(suffix)
