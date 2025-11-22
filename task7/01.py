'''
1. Pretend there is no way to get i-th element of the list. Also we don't know how to use `for` loop. Given that, print the 3rd element from `['a', 'b', 'c']` list
'''
sample = ['a', 'b', 'c']

it = iter(sample)
it.__next__()
it.__next__()
third_element = it.__next__()
print(third_element)