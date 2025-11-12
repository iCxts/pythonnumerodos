#Write an try except block covering the line that executes the sum_two_words() function. Handle at least 2 possible errors that might happen. It should print the returning value when an error is not presented. At last, it should always print Ve and Due are the cutest regardless the scenario.
def sum_two_words(w1: str, w2: str) -> str:
    return (w1 + w2)[0]

w1 = 'Vetit' # This can be changed
w2 = 'Rujipas' # This can be changed

try:
    print(sum_two_words(w1, w2))
except TypeError:
    print('both input must be string')
except IndexError:
    print('string is empty')
finally:
    print('Ve and Due are the cutest')
