#!/usr/bin/env python3
from ..welcome import welcome_user 
from ..game import game


def main():
    user_name = welcome_user()
    print('What is the result of the expression?')
    game(user_name, 'calc')


if __name__ == "__main__":
    main()
