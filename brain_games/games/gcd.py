import random


TASK = "Find the greatest common divisor of given numbers."


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


def generate_round() -> tuple[str, str]:
    """Return two random numbers and the greatest common divisor of them."""
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f"{number_1} {number_2}"
    solution = str(gcd(number_1, number_2))
    return question, solution
