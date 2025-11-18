'''
    Write a decorator n_times which given a number n makes a function to execute n times.

@n_times(3)
def print_my_name():
    print('Due')

print_my_name()

terminal
Due
Due
Due

'''
import functools

def n_times(n: int):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
            
        return inner
    return decorator



