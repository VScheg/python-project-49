import random
import math


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    """Check if number is prime."""
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def generate_round() -> tuple[str, str]:
    """
    Return random number
    and return "yes" if the number is prime
    or return "no" if the number is not prime.
    """
    question = random.randint(1, 100)
    solution = "yes" if is_prime(question) else "no"
    return str(question), solution
