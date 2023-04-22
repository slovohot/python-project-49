#!/usr/bin/env python3

from .engine import engine_games
from brain_games.games.even import get_game, promo_question


def brain_even():
    engine_games(promo_question, get_game)


def main():
    brain_even()


if __name__ == '__main__':
    main()
