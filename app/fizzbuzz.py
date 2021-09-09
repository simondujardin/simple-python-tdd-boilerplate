import numpy as np


def fizzbuzz(n):
    value = np.arange(1, n+1, dtype=object)
    mask3 = value % 3 == 0
    mask5 = value % 5 == 0
    value[mask3] = "Fizz"
    value[mask5] = "Buzz"
    value[mask3 & mask5] = "FizzBuzz"
    return value.tolist()
