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
Defines a card
"""

from collections import namedtuple

Card = namedtuple("Card", ["rank", "suit"])


def stringify_card(self: Card):
    """
    Returns string representation for card object
    :return: ex: |8  ♠|
    """
    spaces = " "
    if self.rank != "10":
        spaces += " "
    return f"|{self.rank}{spaces}{self.suit}|"


def big_card_str(self: Card):
    """
    String definition fo
    :param self:
    :return: List of Strings
             Print in loop
    """
    # 10 card is larger. Special case
    spaces = " "
    if self.rank != "10":
        spaces += " "

    # the string representation
    card_list = [
        " ___ ",
        f"|{self.rank}{spaces}{self.suit}|",
        f"|{self.suit}{spaces}{self.rank}|",
    ]

    return card_list


def card_left(self: Card):
    """
    parses the left side of a card
    :param self:
    :return: list[str] of left side of card
    """
    spaces = ""
    if self.rank == "10":
        spaces += " "
    left_side = [" _", f"|{self.rank}", f"|{self.suit}"]
    return left_side


def card_right(self: Card):
    """
    parses right side of a card
    :param self:
    :return: list[str] of right side of card
    """
    spaces = " "
    underscore = ''
    if self.rank == "10":
        underscore += "_"
    right_side = [
        f"{underscore}__",
        f"{spaces}{self.suit}|",
        f"{spaces}{self.rank}|",
    ]
    return right_side

    # spaces = " "
    # spacing2 = ' '
    # if self.rank != "10":
    #     return f"|{self.suit}{spaces}{self.rank}{spacing2}{self.suit}|"
    #
    # return f"|{self.suit}{1}{spaces}{0}{self.suit}|"


Card.__str__ = stringify_card

if __name__ == '__main__':
    pass
    # rank_ace = 'a'
    # rank_10 = '10'
    # suit_ace = '♠'
    # suit_heart = '♥'
    #
    # ranks = ['a', '10']
    # suits = ['♠', '♥']
    #
    # ace_spades = Card(rank_ace, suit_ace)
    # ten_hearts = Card(rank_10, suit_heart)
    # king_clubs = Card('k', '♣')
    #
    # print(ace_spades)
    # print(ten_hearts)
    #
    # left = card_left(ace_spades)
    # right = card_right(ace_spades)
    # for num in range(0, 3):
    #     print(f"{left[num]}{right[num]}")
    #
    # left = card_left(ten_hearts)
    # right = card_right(ten_hearts)
    # for num in range(0, 3):
    #     print(f"{left[num]}{right[num]}")
    #
    # cards_list = [ace_spades, ace_spades]
    #
    # frame = []
    #
    # line = ''
    # spacing = ''
    #
    #
    # def num_tens(card_list) -> int:
    #     tens = 0
    #     for item in card_list:
    #         if item.rank == '10':
    #             tens += 1
    #     return tens
    #
    #
    # last_card_ten = False
    # if cards_list[len(cards_list) - 1].rank == '10':
    #     last_card_ten = True
    #
    # # card tops
    # top = f" {'__' * (len(cards_list))}{'_' * (num_tens(cards_list) + 1)}"
    # if last_card_ten:
    #     top += "_ "
    # else:
    #     top += " "
    #
    # frame.append(top)
    # # card bodies
    # for num in range(1, 3):
    #     for index, card in enumerate(cards_list):
    #
    #         # check for 10 <- special formatting case
    #         if card.rank == '10':
    #             if index != len(cards_list) - 1:
    #                 if num == 2:
    #                     spacing = ' '
    #
    #         # add left sides
    #         line += f"{card_left(card)[num]}{spacing}"
    #         spacing = ''
    #     # add right side of last card
    #     if num == 3:
    #         if last_card_ten:
    #             line += '10|'
    #         else:
    #             line += f"{card_right(cards_list[len(cards_list) - 1])[num]}"
    #     if num != 3:
    #         line += f"{card_right(cards_list[len(cards_list) - 1])[num]}"
    #     # add line to frame
    #     frame.append(line)
    #     # reset line
    #     line = ''
    #
    # for line in frame:
    #     print(line)
