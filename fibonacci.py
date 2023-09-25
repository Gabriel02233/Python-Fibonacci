# Fibonacci

import time
import sys

sys.set_int_max_str_digits(100000)


def main():
    a = 1
    b = 1
    while True:
        c = a + b
        time.sleep(0.08)
        print(c)
        b = a
        a = c


main()