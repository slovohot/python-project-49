#!/usr/bin/env python3

from brain_games.engine import engine_games
from brain_games.games.gcd import get_game, promo_question


def brain_gcd():
    engine_games(promo_question, get_game)


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
