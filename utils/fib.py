"""
fibonnaci generator
"""


def fib(n):
    if n == 1:
        return 0
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b
