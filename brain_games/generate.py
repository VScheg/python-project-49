import random
from .calculations import is_even, calculate, gcd


def generate_expression(game_name):
    match game_name:
        case "even":
            num = random.randint(0, 99)
            return num, is_even(num)
        case "calc":
            a = random.randint(0, 99)
            b = random.randint(0, 99)
            operation = random.choice(["+", "-", "*"])
            return f"{a} {operation} {b}", str(calculate(a, b, operation))
        case "gcd":
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            return f"{a} {b}", str(gcd(a, b))
