from operator import concat, sub, mul
import random


def calculate(number_1: int, number_2: int, operation: str) -> int:
    """Return result of calculation of two numbers."""
    operations = {
        "+": concat(number_1, number_2),
        "-": sub(number_1, number_2),
        "*": mul(number_1, number_2)}
    return operations[operation]


def get_expression_and_solution() -> tuple[str]:
    """Return expression and solution of expression"""
    a = random.randint(0, 99)
    b = random.randint(0, 99)
    operation = random.choice(["+", "-", "*"])
    return f"{a} {operation} {b}", str(calculate(a, b, operation))
