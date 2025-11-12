#Write a Python function that takes a list and returns a new list with unique elements of the first list. Please use list comprehension as well
def unique_list(items: list) -> list:
    unique = []
    for element in items:
        if element not in unique:
            unique.append(element)
    return unique

