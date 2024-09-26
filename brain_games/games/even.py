import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    """Check if number is even."""
    return number % 2 == 0


def generate_round() -> tuple[str, str]:
    """
    Return random number
    and return "yes" if the number is even
    or return "no" if the number is odd.
    """
    question = str(random.randint(1, 100))
    solution = "yes" if is_even(question) else "no"
    return question, solution
