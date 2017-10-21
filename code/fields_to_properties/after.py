from functools import lru_cache


@lru_cache()
def fib(index):
    if index < 2:
        return 1
    return fib(index-2) + fib(index-1)


class FibonacciResult(object):
    def __init__(self, index):
        self._index = index
        self._value = None

    @property
    def value(self):
        print("Generate a value on demand!")
        if self._value is None:
            self._value = fib(self._index)
        return self._value


print("Constructing... ", end="", flush=True)
five = FibonacciResult(5)
print("done")
print(five.value)
# Constructing... done
# Generate a value on demand!
# 8