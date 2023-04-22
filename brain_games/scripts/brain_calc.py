#!/usr/bin/env python3

from .engine import engine_games
from brain_games.games.calc import get_game, promo_question


def brain_calc():
    engine_games(promo_question, get_game)


def main():
    brain_calc()


if __name__ == '__main__':
    main()
