import prompt
import random


def is_even(num):
    if num % 2:
        return False
    else:
        return True


def is_correct(answer, num, name):
    if is_even(num):
        correct = "yes"
    else:
        correct = "no"
    if answer == correct:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
        print(f"Let's try again, {name}!")
        return False


def game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    tries = 3
    while tries != 0:
        number = random.randint(0, 99)
        print(f"Question: {number}")
        user = prompt.string("Your answer: ")
        if is_correct(user, number, name):
            tries -= 1
        else:
            break
    else:
        print(f"Congratulations, {name}!")
