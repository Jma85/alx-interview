#!/usr/bin/env python3
def min_operations(n: int) -> int:
    """
    Returns the minimum number of operations required to reach a certain number.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

    num_operations = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        num_operations += 1

    return num_operations