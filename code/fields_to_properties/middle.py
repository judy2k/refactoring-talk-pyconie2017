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

    def value(self):
        print("Generate a value on demand!")
        if self._value is None:
            self._value = fib(self._index)
        return self._value

five = FibonacciResult(5)
print(five.value)
# <bound method FibonacciResult.value of
#     <__main__.FibonacciResult object at 0x1056374a8>>