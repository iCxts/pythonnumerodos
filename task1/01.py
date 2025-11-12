#Write a Python function to find the max of any numbers of arguments (don't use the build in function max())
def find_max(*args: float) -> float:
    if not args:
        raise ValueError("this function requires at least one argument")
    
    curr_max = args[0]
    for number in args:
        if  number > curr_max:
            curr_max = number
    return curr_max
