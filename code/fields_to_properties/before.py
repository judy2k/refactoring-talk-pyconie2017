from functools import lru_cache


@lru_cache()
def fib(index):
    print('  ', index)
    if index < 2:
        return 1
    return fib(index-2) + fib(index-1)


class FibonacciResult(object):
    def __init__(self, index):
        self.value = fib(index)


five = FibonacciResult(5)
print(five.value)