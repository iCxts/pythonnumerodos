#Create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list. The function will have an input of a string, and output a list of integers.
def find_length(phrase: str) -> list:
    word_list = phrase.split(' ')
    value_list = []
    for word in word_list:
        value_list.append(len(word))
    return value_list
    
