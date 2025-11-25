'''
She-bang – a sequence #! which is used in Unix-like systems to run executable scripts. She-bang is always written on the first line in the script. After she-bang there is path to an interpreter program written, for example:

#! /bin/sh

#!/usr/bin/env python -v

Look at more example of she-bang here: http://en.wikipedia.org/wiki/Shebang_(Unix)

Write a function parse_shebang which takes a path to an executable script and return a path to an interpreter program, if a script contains she-bang and None otherwise. For the scripts in the example above:

parse_shebang("./example1.txt")
>>> "/bin/sh"

parse_shebang("./example2.txt")
>>> "/usr/bin/env python -v"
'''
def parse_shebang(path: str) -> str | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()
    except FileNotFoundError:
        return None

    if not first_line.startswith("#!"):
        return None

    interpreter = first_line[2:].strip()

    return interpreter if interpreter else None