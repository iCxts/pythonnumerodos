#Write a Python function to check whether a string is pangram or not.
def is_string_pangram(word: str) -> bool:
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters = set(char.lower() for char in word if char.isalpha())
    return alphabet <= letters  
