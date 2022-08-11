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
Contains all player profiles
Allows user to create a player
delete
load to a game
save to file
return from file
"""

import pickle
from blackjackgame.player import Player


class PlayerBox:
    """
    A box for players
    """

    def __init__(self):
        """
        sets up the box
        could inherit dict
        didn't see a reason
        """
        self.players = {}
        self.load_player_file()

    def print_players(self):
        """
        prints all players in box
        :return:
        """
        print("PLAYER DATABASE:\n--------------------------")
        for value in self.players.values():
            print(f"ID: {value.unique_id} - {value}")
        print("--------------------------")

    @staticmethod
    def new_player() -> Player:
        """
        creates a new player object
        :return:
        """
        # prime loop
        accepted = False
        name = ''

        # allows user to correct typos
        while not accepted:
            name = input("What is the player name?")
            accepted = Player.query_bool(f"Name: {name}\nIs this correct?")

        # creates default player if no name
        # avoids crashes
        if name != '':
            return Player(name)
        return Player("DEFAULT PLAYER")

    def add_player(self):
        """
        # creates a new player object then adds to dict
        :return:
        """
        self.add(self.new_player())

    def add(self, actor: Player):
        """
        adds a player to the dict
        if name is equivalent to existing id
        prompts for new name
        :param actor: Player object
        :return: None
        """
        if actor.unique_id:
            self.players.update({actor.unique_id: actor})
        else:
            self.set_player_id(actor)
            self.players.update({actor.unique_id: actor})
        self.save_player_file()

    def set_player_id(self, actor: Player, id_inp=None) -> str:
        """
        assigns a player ID to a Player object
        defaults to the player name
        :param actor: Player object
        :param id_inp: str of ID
        :return: the new ID
        """
        if id_inp:
            new_id = id_inp
        else:
            new_id = actor.name

        if new_id not in self.players.keys():
            actor.set_id(new_id)
            self.save_player_file()
        else:
            while new_id in self.players.keys():
                new_id = input(
                    f"A player with ID: '{new_id}' already exists. \n"
                    f"Please enter a new ID\n"
                    f"If you want to cancel input 'x' \n"
                )
                if new_id.lower() != 'x':
                    actor.set_id(new_id)
                    self.save_player_file()

        return new_id

    def update_player(self, actor: Player):
        """
        changes player object with matching ID
        :param actor:
        :return:
        """
        self.players.update({actor.unique_id: actor})
        self.save_player_file()

    def delete_player(self):
        """
        deletes a player with id matching str input
        takes the input from terminal
        :return:
        """
        self.delete(input("Name:"))

    def delete(self, player_id: str) -> bool:
        """
        deletes a player with id matching str input
        input comes from parameter
        checks for ID
        :param player_id: str of a unique ID
        :return: bool success or not
        """
        if player_id in self.players:
            self.players.pop(player_id)
            self.save_player_file()
            return True

        print(f"the ID: '{player_id}' does not exist")
        return False

    def return_player_list(self) -> list:
        """
        returns a list of all unique ID's
        :return:
        """
        return list(self.players.keys())

    def save_player_file(self, *, filename: str = None) -> bool:
        """
        saves player dict to a pickle file
        default blackjack_players.pickle
        can use custom filename
        :return: (bool) successful save
        """
        if filename:
            save_file = f"{filename}.pickle"
        else:
            save_file = "blackjack_players.pickle"

        with open(save_file, 'wb') as file_dump:
            pickle.dump(
                self.players, file_dump, protocol=pickle.HIGHEST_PROTOCOL
            )
        print("Player File Saved")
        return True

    def load_player_file(self, *, filename: str = None) -> bool:
        """
        loads player dict from file
        uses default str
        can customize
        :param filename: custom filename (not needed)
        :return: (bool) successful load
        """
        if filename:
            save_file = f"{filename}.pickle"
        else:
            save_file = "blackjack_players.pickle"
        try:
            with open(save_file, 'rb') as file_loader:
                self.players = pickle.load(file_loader)
                print("Successful Load")
            return True
        except pickle.UnpicklingError as error:
            print(f"file load error: {error}")
            return False
        except FileNotFoundError as error:
            print(f"ERROR::{error}")
            return False

    def get_player(self, player_id) -> Player:
        """
        returns player object with unique ID matching input
        :param player_id: str of unique id
        :return: Player object
        """
        actor = False
        while not actor:
            actor = self.players.get(player_id)

        return actor


if __name__ == "__main__":
    box = PlayerBox()

    box.save_player_file(filename="test_save")
