'''
Write a function boxed which takes a string and two arguments: a symbol fill and a number pad. A result of the boxed function execution should be a string surrounded by fill symbols as it’s shown in the example.

print(boxed("Hello world", fill="*", pad=2))
print(boxed("Fishy", fill="#", pad=1))
result:

*****************
** Hello world **
*****************

#########
# Fishy #
#########
'''
def boxed(text: str, fill: str = "*", pad: int = 1) -> str:
    inner = f" {text} "
    side = fill * pad
    middle = f"{side}{inner}{side}"
    border = fill * len(middle)
    return "\n".join([border, middle, border])


