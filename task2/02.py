#The function below can raise different exceptions, depending on the argument. Handle all possible exceptions (and base class Exception). For each exception type print corresponding message. You cannot change the do_meaningless_things function.
def do_meaningless_things(argument):
    answer = 0
    array = [[1, 2, 3], [4.4, 5, "6"], ['list("78")', 9.0, 10/(argument-5)], [None]]
    for i in range(4):
        for j in range(argument):
            answer += array[i][j]
    return answer

try:
    do_meaningless_things() # argument can be anything
except ZeroDivisionError as error:
    print("ZeroDivisionError:", error)
except TypeError as error:
    print("TypeError:", error)
except IndexError as error:
    print("IndexError:", error)
except Exception as error:
    print("Except:", error)
else:
    print("everything went fine")

