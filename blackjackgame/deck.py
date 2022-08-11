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
Defines a deck (group of standard playing cards)
"""

from random import shuffle, randint
from blackjackgame import cards as card_template


class Deck:
    """
    52 cards Joker optional.
    Cut and Cut card included
    Suits use universal unicode symbols
    """

    ranks = "a 2 3 4 5 6 7 8 9 10 j q k".split()
    # suits = 'c h s d'.split()
    suits = "♣ ♥ ♠ ♦".split()
    joker_card = "🃏"

    # These should probably be in the game file. Card values depend on the game
    values = list(range(1, 10)) + [10, 10, 10, 10]
    rank_val = dict(zip(ranks, values))

    def __init__(self, *, joker: bool = False):
        """
        Creates deck
        """
        # card is a NamedTuple
        self._cards = [
            card_template.Card(rank, suit)
            for suit in Deck.suits
            for rank in Deck.ranks
        ]

        # Default Joker isn't needed
        if joker:
            self._cards = self._cards + [
                card_template.Card(Deck.joker_card, Deck.joker_card)
            ]

        self._cut_card_pos = -1

    def __str__(self) -> str:
        """
        Prints every card in card str representation
        ex: |8  ♠| \n <- 1 of 52 lines
        allows user to see order of cards in deck
        :return: str -
        """
        print_statement = ""
        for card in self._cards:
            print_statement += card.__str__() + "\n"
        return print_statement

    def shuffle_deck(self, shuffle_count=1) -> None:
        """
        Shuffles the deck object
        pseudorandom
        Multiple shuffles not "needed" due to random
        But it replicates reality
        :param shuffle_count: Allows mor than one shuffle
        :return: None
        """
        for _ in range(shuffle_count):
            shuffle(self._cards)

    def cut_card_pos(self) -> int:
        """

        :return:
        """
        return self._cut_card_pos

    def cut_deck(
        self, low_range=None, high_range=None, *, cut_pos=None
    ) -> None:
        """
        Cuts the deck.
        User can either provide low/high limits for random
        OR they can define a cut position
        defined cut pos overrules rand
        :param low_range: lowest cut point
        :param high_range: highest cut point
        :param cut_pos: overrule any random cut.
        :return: None
        """
        deck_size = len(self._cards)

        if high_range:
            if high_range > deck_size:
                raise "High_range can not be above deck size"

        tenth = deck_size // 10

        low = low_range if low_range else tenth
        high = high_range if high_range else (3 * tenth)

        cut_point = cut_pos if cut_pos else randint(low, high)

        upper_half = self._cards[:cut_point]
        lower_half = self._cards[cut_point:]

        self._cards = lower_half + upper_half

    def set_cut_card_pos(self, cut_pos: int = None) -> int:
        """
        Allows setting a specific position
        Defaults to between 80 and 80%
        Default positions based on 8 deck shoe
        :param cut_pos: User defined cut card pos
        :return: (int) new cut card pos
        """
        if cut_pos:
            self._cut_card_pos = cut_pos
        else:
            self.set_random_cut_card_pos(
                int(len(self._cards) // (10 / 8)),
                int(len(self._cards) // (10 / 8.5)),
            )

        return self.cut_card_pos()

    def set_random_cut_card_pos(self, lower_bound=0, upper=None) -> None:
        """
        Sets a cut card position
        Defaults to any location in deck
        lower and upper bounds can be set
        :param lower_bound: lowes position for cut card
        :param upper: highest position for cut card
        :return: None
        """
        if upper:
            upper_bound = upper
        else:
            upper_bound = len(self._cards)

        # print(f"cut_card limits: {upper_bound}, {lower_bound}")

        self._cut_card_pos = randint(lower_bound, upper_bound)

    def has_past_cut_card_pos(self) -> bool:
        """
        Cut Card Pos is defined as int in __init__
        Signifies the time to reshuffle deck
        :return: bool: deck size smaller than cut card num
        """
        return len(self._cards) < self._cut_card_pos

    def deal(self) -> card_template.Card:
        """
        pops card from deck list, and returns it as argument
        :return: top Card object from deck
        """
        return self._cards.pop()

    def num_cards(self) -> int:
        """
        returns remaining number of cards
        :return: int of card number
        """
        return len(self._cards)


if __name__ == "__main__":
    pass
