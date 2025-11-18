'''
Write a decorator once which makes a function to execute only once and other times it just returns the result calculated on the first call.

@once
def random_number():
    return random.randint(1, 10)

print(random_number())
print(random_number())
print(random_number())

terminal
4
4
4

'''
import functools

def once(func):
    ran = False
    output = 0
    
    @functools.wraps(func)
    def inner(*args, **kwargs):
        nonlocal ran, output
        if not ran:
            output = func(*args, **kwargs)
            ran = True
        return output
    return inner


