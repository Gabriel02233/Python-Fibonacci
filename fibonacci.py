# Fibonacci
# Author @jakobgraetz
# (c) Jakob Graetz | 2023 - 2024
# MIT license
# Last Update 02/12/2024 (MM/DD/YYYY)

# Imports, optional,
import time
import sys

# Optional, but increases the maximum integer size this
# script can compute, therefore highly recommended.
sys.set_int_max_str_digits(100000)


# Definition of main() function.
def main():
    # Initializes the first to numbers. Should stay at
    # a = 1; b = 0
    a: int = 1
    b: int = 0
    while True:
        # Computes the next number of the sequence.
        c: int = a + b
        # Optional, but you can set the sleep function
        # so you can more easily read the number in your
        # terminal before the next one gets printed.
        time.sleep(0.08)
        # Prints the computed next number of the Fibonacci
        # sequence.
        print(c)
        # Updates the initial numbers to their new values.
        b = a
        a = c


main()