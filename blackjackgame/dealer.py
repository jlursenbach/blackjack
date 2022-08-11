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
Defines Dealer AI
Subset of Player
"""

from blackjackgame import player


class Dealer(player.Player):
    """
    Dealer defines actions for Dealer special Player obejct
    """

    def __init__(self, table_pointer):
        """
        Initializes Dealer
        table_pointer allows access to other player hands
        """
        super().__init__(name="Dealer", player_type="Dealer")
        # define name and player type

        # info used for decision-making
        self.seats = table_pointer.seats
        self.player_states = []

    def __str__(self):
        """
        Redefines string representation
        Player prints bank balance
        Dealers don't need a bank
        :return: "Dealer"
        """
        return f"{self.name}"

    def get_player_states(self):
        """
        Pulls the current status from every player
        :return: None
        """
        for chair in self.seats:
            if chair.actor.type != 'Dealer':
                self.player_states.append(chair.status())

    def query_bool(self, query: str) -> bool:
        """
        The only decision is hit or not
        Simple dealer hits until 17
        :return:
        """
        # need a parameter to overwrite Player call
        # Parameter not needed
        # pylint complains that it isn't used
        # this is the work around
        placeholder = query
        placeholder += '1'

        self.get_player_states()

        all_busted = True
        for state in self.player_states:
            if state != 'bust':
                all_busted = False

        if all_busted:
            return False

        # hits if score is less than 17
        if self.seats[len(self.seats) - 1].score() >= 17:
            return False

        return True
