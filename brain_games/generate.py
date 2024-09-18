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
        case "progression":
            progression = generate_progression()
            key = random.choice(progression)
            progression[progression.index(key)] = ".."
            progression = [str(i) for i in progression]
            return ' '.join(progression), str(key)


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(6, 11)
    count = length
    number = start
    result = []
    while count != 0:
        result.append(number)
        number += step
        count -= 1
    return result
