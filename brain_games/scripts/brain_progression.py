#!/usr/bin/env python3

from brain_games.engine import start_game
from brain_games.games.progression import get_game, GAME_RULE


def brain_progression():
    start_game(GAME_RULE, get_game)


def main():
    brain_progression()


if __name__ == '__main__':
    main()
