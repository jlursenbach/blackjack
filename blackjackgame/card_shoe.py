#!/usr/bin/env python3
# Jacob Ursenbach
# CPSC 386-01
# 2022-07-21
# jlursenbach@csu.fullerton.edu
# @jlursenbach
#
# Lab 02-00
#
# Blackjack game
#

"""
This class defines a card shoe, which holds a number of decks.
Functions are relevant to shoe size and multiple deck manipulation
"""

from random import randint
from blackjackgame import deck as ds


class Shoe(ds.Deck):
    """
    The shoe deck
    """

    def __init__(self, count=8):
        """
        :param count: The number of decks in the shoe
        """
        super().__init__(joker=False)

        # defines a single deck.
        self.deck_def = self._cards

        # keeps the current deck count (in case it changes)
        self.decks_in_shoe = 1
        self.shoe = []

        # adds all decks
        for _ in range(count - 1):
            self.add_deck()

    def __str__(self):
        """
        Defines the string representation of the Shoe
        Ex: Decks: 8 | Cards: 564
        :return: string representation of shoe
        """
        return f"Decks: {self.shoe_size()} | Cards: {len(self._cards)}"

    def shoe_size(self):
        """
        :return: an int representing num of decks
        """
        return self.decks_in_shoe

    def reset_shoe(self, new_shoe_size: int = None):
        """
        Resets the shoe with new decks
        :return: None
        """
        # deletes all contents of shoe
        self.clear_shoe()

        # allows user to define new shoe size
        if new_shoe_size:
            self.set_shoe_size(new_shoe_size)

        # adds the decks
        for _ in range(self.decks_in_shoe):
            self.add_deck()

    def add_deck(self):
        """
        Adds a single new deck to the shoe
        :return: None
        """
        self._cards = self._cards + self.deck_def
        self.decks_in_shoe += 1

    def clear_shoe(self):
        """
        Deletes everything in the shoe.
        :return: None
        """
        self._cards.clear()

    def set_shoe_size(self, size):
        """
        Allows user to redefine num of cards in shoe
        :param size: num of decks
        :return: None
        """
        # sets new size
        self.decks_in_shoe = size
        # resets shoe with new size
        self.reset_shoe()

    def rand_shoe_size(self, low, high) -> int:
        """
        Allows show with random num of decks
        User provides a range
        :param low: lowest num of decks
        :param high: Most decks
        :return:
        """
        self.set_shoe_size(randint(low, high))
        return self.shoe_size()


if __name__ == "__main__":
    pass
