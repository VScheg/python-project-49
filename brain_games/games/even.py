import random


def is_even(number: int) -> bool:
    """Check if number is even."""
    return False if number % 2 else True


def get_yes_or_no(statement: bool) -> str:
    """
    Return "yes" if argument is True.
    Return "no" if argument is False.
    """
    return "yes" if statement else "no"


def get_number_and_solution(function) -> str:
    """
    Return random number
    and return "yes" if result of function of the number returns True,
    or return "no" if result of function of the number returns False.
    """
    number = random.randint(1, 100)
    return number, get_yes_or_no(function(number))
