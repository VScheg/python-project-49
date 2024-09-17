import random
from .calculations import is_even, calculate


def generate_expression(game_name):
    match game_name:
        case "even":
            print('Answer "yes" if the number is even, otherwise answer "no".')
            num = random.randint(0, 99)
            return num, is_even(num)
        case "calc":
            print('What is the result of the expression?')
            a = random.randint(0, 99)
            b = random.randint(0, 99)
            operation = random.choice(["+", "-", "*"])
            return f"{a} {operation} {b}", str(calculate(a, b, operation))
