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
A seat in the table
contains player and hand
controls interaction with player
"""

from random import randrange
from blackjackgame import hand
from blackjackgame import player


class Seat:
    """
    A seat at a blackjack table
    """

    def __init__(self, new_player: player.Player = None):
        """
        add the player and hand
        :param new_player:
        """
        self.actor = new_player
        self.hand = hand.Hand()
        self.bet = float(0)
        self.did_double = False

    def __str__(self):
        """
        str representation of seat state
        :return:
        """
        if self.actor.type == 'Dealer':
            return f"{self.actor.name} - (hand: {self.hand})"

        return f"{self.actor.name} - ({self.hand} - (bet: ${self.bet})"

    def add_player(self, new_player):
        """
        replace the player int eh seat
        :param new_player:
        :return:
        """
        self.actor = new_player

    def remove_player(self):
        """
        emptys the seat
        :return:
        """
        self.actor = None

    def deal_to(self, *kwarg):
        """
        gives Card object to the Hand
        :param kwarg:
        :return:
        """
        for card in kwarg:
            self.hand.add_cards(card)

    def clear_bet(self):
        """
        zeros out bet value
        :return:
        """
        self.bet = float(0)

    def clear_hand(self):
        """
        clears hand
        :return:
        """
        self.hand.clear_hand()

    def clear_double(self):
        """
        sets did double to false
        :return:
        """
        self.did_double = False

    def is_empty(self) -> bool:
        """
        is the hand empty?
        :return:
        """
        return not bool(self.actor)
        #
        # if self.actor is None:
        #     return True
        # else:
        #     return False

    @staticmethod
    def empty() -> int:
        """
        returns -1 for an empty seat (no player)
        :return:
        """
        return -1

    def status(self) -> str:
        """
        parses the player status into a string
        :return:
        """
        if self.hand.get_value() > 21:
            return "bust"
        if self.hand.get_value() == 21:
            return "win"

        return "alive"

    def score(self) -> int:
        """
        returns player's current score
        :return:
        """
        return self.hand.get_value()

    def get_bet(self):
        """
        provides a number of automated queries
        asks for a bet in a realistic voice.
        calls the player get_float
        parses response
        :return:
        """
        player_bet = -1

        queries = [
            f"How much do you bet {self.actor.name}?",
            f"What's the bet {self.actor.name}",
            f"{self.actor.name} betting how much?",
            f"What are you putting down {self.actor.name}",
            f"How much are we putting on the line {self.actor.name}",
            f"You've got ${self.actor.bank}, how much do you bet",
            f"${self.actor.bank} available. What's the bet?",
            f"Bet how much of your ${self.actor.bank}",
        ]

        # loop requires valid response
        while player_bet < 0:
            # get player query
            player_bet = self.actor.query_float(
                queries[randrange(len(queries))] + '\n'
            )

            # valid number
            if player_bet > 0:
                # checks player bank to validate bet
                if self.actor.bank >= player_bet:
                    self.actor.edit_bank(-player_bet)
                    self.bet += player_bet
                else:
                    player_bet = -1
                    self.actor.message("You don't have that much money")
            # player doesn't want to play
            elif player_bet == 0:
                pass
            # invalid bet (was a negative number).
            # will replay loop
            else:
                self.actor.message("You cannot bet a negative number")

    def doubles_down(self) -> bool:
        """
        calls the player query_bool
        provides a number of querys to ask in different ways
        :return:
        """
        does_double = False
        queries = [
            f"Ok {self.actor.name}, do you want to double down?",
            f"Are you going to double down {self.actor.name}?",
            f"{self.actor.name} Double Down?",
            f"We doubling down, or what {self.actor.name}",
            f"Double Down {self.actor.name}?",
        ]

        if self.actor.bank >= self.bet:
            does_double = self.actor.query_bool(
                queries[randrange(len(queries))] + '\n'
            )
        else:
            self.actor.message(
                f"{self.actor.name} can not double down. Insufficient funds.\n"
            )

        if does_double:
            self.actor.edit_bank(-self.bet)
            self.bet += self.bet
            self.did_double = True
            return True

        return False

    def player_hits(self):
        """
        Queries the player if they want to hit
        provides a number of unique interaction/questions.
        calls player.query_bool
        :return: bool hit or no hit
        """
        queries = [
            f"{self.actor.name} Hit?",
            f"Want another card {self.actor.name}?",
            f"{self.actor.name} do you hit or stand?",
            f"Deal another {self.actor.name}?",
            f"Risk a hit {self.actor.name}?",
            f"That's {self.hand.get_value()} points. Hit?",
            f"You're at {self.hand.get_value()} {self.actor.name}. Hit?",
            f"{self.hand.get_value()} points. Hit?",
            f"${self.bet} on the line. Deal another?",
            f"${self.bet} bet, {self.hand.get_value()} points. Hit again?",
            "Want another card?",
            "Push your luck?",
        ]

        return self.actor.query_bool(queries[randrange(len(queries))] + '\n')

    def pay_out(self):
        """
        pays the bet into the bank at a 2 to 1 odd
        used for a win
        :return:
        """
        self.actor.edit_bank(self.bet * 2)

    def return_funds(self):
        """
        provides the bet money back to the user
        used in case of a tie with dealer
        :return:
        """
        self.actor.edit_bank(self.bet)


if __name__ == '__main__':

    dude = player.Player('Jacob')
    chair = Seat(dude)

    print(chair)
