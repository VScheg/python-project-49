def is_even(num):
    return "no" if num % 2 else "yes"


def calculate(num1, num2, operation):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case _:
            return num1 * num2


def gcd(num1, num2):
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    if max_num % min_num == 0:
        return min_num
    while min_num != 0:
        exchange = min_num
        min_num = max_num % min_num
        max_num = exchange
    return max_num


def is_prime(num):
    if num < 2:
        return "no"
    elif num < 4:
        return "yes"
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return "no"
    return "yes"
