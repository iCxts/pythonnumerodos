#Write a Python function to calculate the fibonacci number of index i (starts with 1). The function accepts the number as an argument and return a single number. The fibonacci sequence starts with 1,1,2,3,5,8,13,21,.... Therefore, fibonacci of index 6 is number 8.
def fibonacci(n: int) -> int:
    if n <= 0:
        raise ValueError("index >= 1")
    
    if n == 1 or n == 2:
        return 1
    prev, curr = 1, 1
    for _ in range(n - 2):  
        prev, curr = curr, prev + curr
    return curr
