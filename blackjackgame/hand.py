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
Defines a user hand
A seat holds a hand and a player
"""

from blackjackgame import cards
from blackjackgame import deck


class Hand(list):
    """
    A list that holds cards
    parses card value and provides str for hand
    """

    _ranks = deck.Deck.ranks
    _values = list(range(1, 11)) + [10, 10, 10]
    _rank_to_value_dict = dict(zip(_ranks, _values))

    @staticmethod
    def int_card_value(card: cards.Card):
        """
        gets the value of a single card
        :param card: a Card Named Tuple
        :return: int value defined by Blackjack rules
        """
        return Hand._rank_to_value_dict.get(card.rank)

    # calls card value and assigns an int to a Card object
    cards.Card.__int__ = int_card_value

    def __init__(self, *argv):
        """
        Initialize class, super of list[]
        :param argv: argv allows adding multiple cards
        """
        super().__init__()
        # self.score = 0
        if argv:
            self.add_cards(argv)

    def __str__(self):
        """
        card str is |8  ♠|
        prints all cards and the combined score
        :return: ex: |8  ♠||8  ♠| - points: <16>
        """
        self_str = 'cards:'
        for card in self:
            self_str += card.__str__()
        self_str += f" - points: <{self.get_value()}>"
        return self_str

    @staticmethod
    def is_ace(check_card: cards.Card) -> bool:
        """
        checks if a card is an ace
        :param check_card: the card to check
        :return: bool
        """
        return check_card.rank == 'a'

    def get_value(self) -> int:
        """
        parses string into numeric card value
        :return: in card value
        """
        if len(self) == 0:
            return 0

        num_aces = sum(map(self.is_ace, self))
        hand_value = sum(map(cards.Card.__int__, self))

        if hand_value <= 21:
            for _ in range(num_aces):
                if hand_value + 10 <= 21:
                    hand_value += 10

        return hand_value

    def clear_hand(self):
        """
        removes all cards from hand
        :return: None
        """

        self.clear()

    def peek_cards(self):
        """
        returns a list with the cards currently held in the hand
        self is a list
        :return:
        """
        return self

    def print_hand(self):
        """
        prints cards:
        ex:
        |8  ♠|
        |8  ♠|
        :return:
        """
        for item in self:
            print(item)

    def cards_str_list(self):
        """
        returns a list of card strings
        :return:
        """
        hand_list = []
        for item in self:
            hand_list.append(cards.stringify_card(item))
        return hand_list

    def add_cards(self, *new_cards):
        """
        takes cards to be added
        adds them to list
        :param new_cards:
        :return:
        """
        if new_cards:
            for card in new_cards:
                self.append(card)


if __name__ == "__main__":
    pass
