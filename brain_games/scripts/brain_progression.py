#!/usr/bin/env python3

from .engine import engine_games
from brain_games.games.progression import get_game, promo_question


def brain_progression():
    engine_games(promo_question, get_game)


def main():
    brain_progression()


if __name__ == '__main__':
    main()
