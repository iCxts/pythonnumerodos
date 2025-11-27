import sys

class ConsoleLogger:
    def __init__(self, filename):
        self.filename = filename
        self._original_stdout = None
        self._file = None
        self._lines_written = 0

    def __enter__(self):
        self._original_stdout = sys.stdout
        self._file = open(self.filename, "w", encoding="utf-8")

        logger = self

        class _StdoutWrapper:
            def write(self, text):
                logger._file.write(text)
                logger._file.flush()
                logger._lines_written += text.count("\n")

            def flush(self):
                logger._file.flush()

        sys.stdout = _StdoutWrapper()
        return self

    def __exit__(self, exc_type, exc, tb):
        sys.stdout = self._original_stdout

        if exc_type is not None:
            message_map = {
                ZeroDivisionError: "zero division error",
                ValueError: "value error",
            }
            msg = message_map.get(exc_type, f"{exc_type.__name__}: {exc}")
            self._file.write(msg + "\n")
            self._lines_written += 1

        self._file.close()
        print(f"{self._lines_written} lines were logged to {self.filename}")
        return True


# Example usage
if __name__ == "__main__":
    with ConsoleLogger("output.log"):
        print("This should go to the file")
        print("This too")
        x = 2 / 0
