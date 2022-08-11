#!/usr/bin/env python3
# Jacob Ursenbach
# CPSC 386-01
# 2022-07-10
# jlursenbach@csu.fullerton.edu
# @jlursenbach
#
# Lab 02-00
#
# This file is a blackjack game
#

"""
This is the launchfile for the blackjack game
"""

from blackjackgame import game


def main():
    """Launches game file"""

    blackjack = game
    blackjack.main()


if __name__ == "__main__":
    # __init__.start_game()
    main()
