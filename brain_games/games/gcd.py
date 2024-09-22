import random


def gcd(number_1: int, number_2: int) -> int:
    """Return the greatest common divisor of two numbers."""
    max_number = max(number_1, number_2)
    min_number = min(number_1, number_2)
    if max_number % min_number == 0:
        return min_number
    while min_number != 0:
        remainder = max_number % min_number
        max_number, min_number = min_number, remainder
    return max_number


def get_numbers_and_gcd() -> tuple[int]:
    """Return two random numbers and the greatest common divisor of them."""
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    return f"{a} {b}", str(gcd(a, b))
