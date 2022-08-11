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
The table object controls the game flow
controls queries and turns
enter and exit rounds
"""

from random import randint
from blackjackgame import card_shoe
from blackjackgame import seat
from blackjackgame.player import Player
from blackjackgame.dealer import Dealer
from blackjackgame.table_visualization import TableVisualizer as Tv
from blackjackgame.player_box import PlayerBox as Bx


class Table:
    """
    a Blackjack table
    """

    def __init__(self, players, *, box=Bx()):
        """
        sets up the table
        contains:
            shoe
            seats
                players
                hands
        :param players: a list of players
        :param box: a pointer to the box that holds all players
        """
        self.shoe = card_shoe.Shoe()
        self._new_shoe()
        print(f"decks: {self.shoe.shoe_size()}")
        self.seats = []

        # pointer to player file used to save
        self.box = box
        # self.header = 'BLACKJACK!!!'

        # seat players
        for actor in players:
            self.seats.append(seat.Seat(actor))

        # seat Dealer: update this when you create the AI
        self.seats.append(seat.Seat(Dealer(self)))

        # self.seat_table(players)

        # for actor in self.seats:
        #     # print(self.seats[actor])
        #     print(actor)

        self._round_loop()

    def manual_cut_card(self) -> int:
        """
        sets cut card location to project standards
        :return:
        """
        shoe_len = self.shoe.num_cards()
        return randint(shoe_len - 80, shoe_len - 60)

    def _new_shoe(self):
        """
        creates a new shoe
        called if deck passes cut card
        :return:
        """
        self.shoe.reset_shoe()
        self.shoe.shuffle_deck()
        self.shoe.cut_deck()
        self.shoe.set_cut_card_pos(self.manual_cut_card())

    # def add_player(self):
    #     """
    #
    #     :return:
    #     """
    #     pass

    # def get_table(self):
    #     """
    #
    #     :return:
    #     """
    #     return {"seats": self.seats,
    #             "header": self.header}

    def _round_loop(self):
        """
        The game loop
        controls flow of game
        calls all queries and players
        :return:
        """
        playing = True

        game_loop = [
            self._reset_chair,
            self._query_buy_in,
            self._deal_round,
            self._query_double_down,
            self._query_hits,
            self._check_winner,
            self._mysterious_benefactor,
        ]

        welcome = [
            "     _______________________",
            "     WELCOME TO BLACKJACK!!!",
            "     _______________________",
        ]

        top_of_round = [
            ">>> ITS THE TOP OF THE ROUND!!! <<<",
            "-----------------------------------\n",
        ]

        for line in welcome:
            print(line)

        while playing:

            for line in top_of_round:
                print(line)

            if self.shoe.has_past_cut_card_pos():
                self._new_shoe()
            for func in game_loop:
                for chair in self.seats:
                    self._query_wrapper(func, chair)
            if self.seats[0].actor.type == "Dealer":
                playing = False
            else:
                playing = self.keep_playing(self.seats[0])

            if not playing:
                self.box.save_player_file()
                print("Player Quit. Exiting GameState")

    @staticmethod
    def keep_playing(chair) -> bool:
        """
        query if player keeps playing
        default calls player 1
        if there's only a Dealer game loop quits instead
        :param chair:
        :return:
        """
        return chair.actor.query_bool("Do you want to keep playing?\n")

    @staticmethod
    def _mysterious_benefactor(chair):
        """
        Class requirement
        adds $10,000 to an empty bank at end of turn
        :param chair:
        :return:
        """
        if chair.actor.type != "Dealer":
            if chair.actor.bank == 0:
                chair.actor.edit_bank(10000)
                print(
                    f"{chair.actor.name} IS BROKE!!!\n"
                    f"A mysterious benefactor SWOOPS IN!\n"
                    f"--you check our bank... $10,000?!?!\n"
                )

    @staticmethod
    def _reset_chair(chair):
        """
        sets the chair to an empty state
        :param chair:
        :return:
        """
        chair.clear_hand()
        chair.clear_bet()
        chair.clear_double()

    @staticmethod
    def _query_wrapper(func, arg):
        """
        allows functions to be called from a list of functions
        :param func: a function
        :param arg: the parameters
        :return: None
        """
        func(arg)

    @staticmethod
    def _query_buy_in(chair):
        """
        Asks plyer in selected chair for their buy in
        :param chair: chair holding 1 player
        :return:float - 0 means no buy in
        """
        if chair.actor.type != "Dealer":
            print(chair.actor)
            chair.get_bet()

    def _deal_round(self, chair):
        """
        deals to everyone
        dealer only gets 1 card
        :param chair: the chair being dealt to
        :return: None
        """
        if chair.actor.type != "Dealer":
            chair.deal_to(self.shoe.deal(), self.shoe.deal())
        else:
            chair.deal_to(self.shoe.deal())
        print(chair.actor.name)
        self.print_cards(chair.hand)
        print(f"Points: {chair.hand.get_value()}")
        print("---------------------")

    def _query_double_down(self, chair):
        """
        asks player if they want to double down
        deals to them or passes
        :param chair:
        :return:
        """

        if chair.actor.type != "Dealer":
            print(f"DOUBLE DOWN: {chair.actor.name}")
            print(chair)
            if chair.doubles_down():
                chair.deal_to(self.shoe.deal())
                print(chair)

    @staticmethod
    def print_cards(hand):
        """
        provides a visual representation of the player hand
        :return:
        """
        frame = Tv.card_subframe(hand)
        for f_line in frame:
            print(f_line)

    def _query_hits(self, chair):
        """
        asks player if they want to hit
        :param chair: chair with player being queried
        :return:
        """
        continue_round = True
        if chair.actor.type == "Dealer":
            chair.deal_to(self.shoe.deal())

        print(
            f"\n|--------------------------|\n TURN: ---- {chair.actor.name} ----"
        )

        if chair.did_double:
            print(
                f"--- {chair.actor} doubled down. Bet = {chair.bet} Cards = {chair.hand}"
            )

        if not chair.did_double:
            while chair.status() == "alive" and continue_round is True:
                print(chair.hand)
                self.print_cards(chair.hand)
                hit = continue_round = chair.player_hits()
                if hit:
                    chair.deal_to(self.shoe.deal())

        print(chair)
        self.print_cards(chair.hand)

        if chair.status() == 'win':
            print("21! WINNER!!!!!")

    def _check_winner(self, chair):
        """
        checks if a hand meets winning states
        if it does it pays out
        at the end resets hand
        :param chair:
        :return:
        """

        score = chair.hand.get_value()
        dealer_score = self.seats[-1].hand.get_value()

        print("----checking winners----")

        if chair.actor.type != "Dealer":
            print(chair)
            if score == 21:
                chair.pay_out()
                print("BLACKJACK!!!!\n")
            elif score > 21:
                print(f"lost ${chair.bet}\n")
            elif score < 21:
                if score > dealer_score or dealer_score > 21:
                    chair.pay_out()
                    print(f"{chair.actor.name} is a winner! ${chair.bet}\n")
                else:
                    print(f"lost ${chair.bet}\n")
            elif score == dealer_score:
                chair.return_funds()
                print("Matched dealer. Funds Returned\n")
            else:
                print(f"lost ${chair.bet}")

            print(f"Player bank is now: {chair.actor.bank}\n")

    @staticmethod
    def continue_query(chair) -> bool:
        """
        does player want to continue playing the game?
        :param chair:
        :return:
        """
        return chair.actor.query_bool("Continue?")

        # import os
        # def clear_screen():
        #     os.system('clear')


if __name__ == '__main__':
    player_1 = Player("Jacob")
    player_2 = Player("Rosa")
    table = Table([player_1, player_2])
