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
A player object
contains unique id, name, bank and type
type can be user, dealer or AI
dealer and AI as subclasses
provides queries to parse response
response parse is how AI can make decisions
"""


class Player:
    """
    docstring
    """

    # possible positive player boolean answers
    with open('blackjackgame/affirm.txt', 'r') as file:
        lines = file.readlines()
        affirmative = [line.rstrip() for line in lines]
    # possible negative player boolean answers
    with open("blackjackgame/neg.txt", 'r') as file:
        lines = file.readlines()
        negative = [line.rstrip() for line in lines]

    def __init__(self, name: str = '', *, player_type='user'):
        """
        sets attributes
        player_type only needed for AI
        :param name:
        :param player_type:
        """
        self.unique_id = ''
        self.name = name
        self.bank = 10000.00
        self.type = player_type

    def __str__(self):
        """
        Str representation of user
        :return:
        """
        return f"{self.name} : ${self.balance()}"

    def set_id(self, id_inp: str):
        """
        sets player_id
        :param id_inp:
        :return:
        """
        self.unique_id = id_inp

    def edit_bank(self, amount: float) -> float:
        """
        edits bank
        does not allow negative numbers
        to be called by outside forces not by player
        :param amount: positive or negative number
        :return: new bank balance float
        """
        if self.bank + amount < 0:
            raise f"<overdraw error> Requested withdrawal: {amount} | available funds: {self.bank}"

        self.bank += amount
        return self.balance()

    def balance(self) -> float:
        """
        bank balance
        :return: a fload of the balance
        """
        return self.bank

    @staticmethod
    def query_bool(query: str) -> bool:
        """
        queries user for true/false - yes/no
        a very weak language interpretation
        build specifically for answers to blackjack
        :param query: prints the question posed to player
        :return: player's choice
        """

        # prime loop with invalid value
        answer = -1

        # keeps user in loop until valid answer
        # searches user input for matching string.
        # removes whitespaces, non-alpha, and capitalization
        while answer is not True and answer is not False:
            answer = ''.join(filter(str.isalpha, input(query).lower()))
            if answer in Player.affirmative:
                answer = True
            elif answer in Player.negative:
                answer = False
            else:
                print("invalid input")

        return answer

    def query_float(self, query) -> float:
        """
        Queries user for float
        :param query: string to ask user
        :return: provided float
        """
        user_input = -1

        while user_input < 0:

            # cleans string
            # removes $ , and whitespace
            # 10,000 10000 and $10,000 are equivalent
            user_input = input(query).strip(' $').replace(',', '')

            # parses user input for valid float
            if self.is_float(user_input):
                user_input = round(float(user_input), 2)
                if user_input >= 0:
                    return user_input
                # else:
                print("invalid input")
            # else:
            print("non numeric input. try again")
            user_input = -1

    @staticmethod
    def is_float(inp: str) -> bool:
        """
        checks if string is a float
        :param inp: a string
        :return: bool
        """
        try:
            float(inp)
            return True
        except ValueError:
            return False

    @staticmethod
    def message(message: str):
        """
        called by table to print non query message
        :param message:
        :return:
        """
        print(message)

    @staticmethod
    def parse_query(query):
        """
        called by table to plint non query message
        :param query:
        :return:
        """
        print(query)


if __name__ == '__main__':
    dude = Player('Jacob')

    CONT = True

    while CONT:
        cont = dude.query_float("how much\n")
        print(cont)
