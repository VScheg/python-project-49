from operator import add, sub, mul
import random


TASK = "What is the result of the expression?"
OPERATIONS = {
    "+": add,
    "-": sub,
    "*": mul
}


def calculate(number_1: int, number_2: int, operation: str) -> int:
    """Return result of calculation of two numbers."""
    return OPERATIONS[operation](number_1, number_2)


def generate_round() -> tuple[str, str]:
    """Return expression and solution of expression"""
    number_1 = random.randint(0, 99)
    number_2 = random.randint(0, 99)
    operation = random.choice(list(OPERATIONS.keys()))
    question = f"{number_1} {operation} {number_2}"
    solution = str(calculate(number_1, number_2, operation))
    return question, solution
