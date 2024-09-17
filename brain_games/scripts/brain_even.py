#!/usr/bin/env python3
import prompt
from ..game import game


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    game(user_name)


if __name__ == "__main__":
    main()
