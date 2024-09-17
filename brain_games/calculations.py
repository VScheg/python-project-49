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
