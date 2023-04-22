#!/usr/bin/env python3

from brain_games.engine import engine_games
from brain_games.games.prime import get_game, promo_question


def brain_prime():
    engine_games(promo_question, get_game)


def main():
    brain_prime()


if __name__ == '__main__':
    main()
