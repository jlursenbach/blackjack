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
A visualization tool
prints a blackjack table state using text manipulation
"""

import os
from blackjackgame import cards as c
from blackjackgame import player as pl


class TableVisualizer:
    """
    Visualiza Blackjack table state in text!
    """

    def __init__(self):
        """
        These are the frames that will be printed
        """
        self.separator = '-' * 60
        self.header_frame = []
        self.table_frame = []
        self.interface_frame = {
            "name": "",
            "results": "",
            "card_frame": "",
            "query_frame": "",
        }

    def set_header_frame(self, header):
        """
        sets the header frame to input
        :param header:
        :return:
        """
        self.header_frame = header

    @staticmethod
    def print_header_frame():
        """
        prints header_frame
        not made yet
        :return:
        """
        print("pass")

    # def parse_table_state(self, bj_table: tbl.Table.seats):
    #
    #     for chair in bj_table:
    #         if chair.actor.unique_id == "Dealer":
    #             continue
    #         player_column.update(
    #             {chair.actor.unique_id:
    #                 {
    #                     f"cash": f'{chair.actor.balance()}',
    #                     f"bet": f'{chair.bet}',
    #                     f"score": f'{chair.hand.get_value()}',
    #                     f"name": f'{chair.actor.name}',
    #                     f"hand": chair.hand.cards_str_list()
    #                 }}
    #         )
    #
    #     turn_subframe = []
    #     cash_subframe = [f"Cash:"]
    #     score_subframe = [f"Score:"]
    #     chair_subframe = [f""]
    #     pass

    def set_table_frame(self, parsed_table: list):
        """
        sets the frame that will print entire table
        :param parsed_table:
        :return:
        """
        self.table_frame = parsed_table

    @staticmethod
    def print_table_frame():
        """
        prints entire table
        :return:
        """
        print("pass")

    @staticmethod
    def set_interface_frame(frame):
        """
        creates the interface frame
        :param frame:
        :return:
        """
        print(frame)

    @staticmethod
    def print_interface_frame():
        """
        prints entire interface frame
        :return:
        """
        print("pass")

    @staticmethod
    def name_subframe(player: pl.Player):
        """
        sets up the name in the name frame
        :param player:
        :return:
        """
        name_frame = [f"{player.name.upper()}'s TURN:"]

        return name_frame

    @staticmethod
    def results_subframe(hand):
        """
        sets up the card and value in the results subframe
        :param hand:
        :return:
        """
        chair_frame = [f"-> {hand.get_value()} points <-"]
        return chair_frame

    @staticmethod
    def card_subframe(player_hand) -> list:
        """
        creates card subframe to visualize cards
        :param player_hand:
        :return:
        """
        frame = []

        frame_line = ''
        spacing = ''

        num_tens = 0
        hand_length = len(player_hand) - 1

        for item in player_hand:
            if item.rank == '10':
                num_tens += 1

        last_card_ten = False
        if player_hand[hand_length].rank == '10':
            last_card_ten = True

        # card tops
        top = f" {'__' * (len(player_hand))}{'_' * (num_tens + 1)}"
        if last_card_ten:
            top += "_ "
        else:
            top += " "

        frame.append(top)
        # card lines
        for num in range(1, 3):
            # for each card
            for index, card in enumerate(player_hand):

                # check for 10 <- special formatting case
                if card.rank == '10' and index != hand_length and num == 2:
                    spacing = ' '
                    # if index != hand_length:
                    #     if num == 2:
                    #         spacing = ' '

                # add left sides to string
                frame_line += f"{c.card_left(card)[num]}{spacing}"
                spacing = ''

            # left sides have been added
            # add right side of last card
            if num == 3:
                if last_card_ten:
                    frame_line += '10|'
                else:
                    frame_line += (
                        f"{c.card_right(player_hand[hand_length])[num]}"
                    )
            if num != 3:
                frame_line += f"{c.card_right(player_hand[hand_length])[num]}"

            # add line to frame
            frame.append(frame_line)
            # reset line
            frame_line = ''

        return frame

    def print_table(self):
        """
        prints all frames
        :return:
        """

        print(self.separator)
        self.print_header_frame()
        print(self.separator)
        self.print_table_frame()
        print(self.separator)
        self.print_interface_frame()

    @staticmethod
    def print_frame(frame):
        """
        generic frame printing function
        :param frame:
        :return:
        """
        for item in frame:
            print(item)

    # will need to test if this works on linux
    @staticmethod
    def clear_screen():
        """
        clears terminal screen
        use this to make table changes look animated
        :return:
        """
        os.system('cls||clear')


if __name__ == "__main__":
    pass
