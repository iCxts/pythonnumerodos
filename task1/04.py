#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def count_case(word: str) -> tuple:
    upper_count = 0
    lower_count = 0

    for char in word:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count
