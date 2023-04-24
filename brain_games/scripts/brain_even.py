#!/usr/bin/env python3

from brain_games.engine import start_game
from brain_games.games.even import get_game, GAME_RULE


def brain_even():
    start_game(GAME_RULE, get_game)


def main():
    brain_even()


if __name__ == '__main__':
    main()
