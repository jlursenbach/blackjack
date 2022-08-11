# Use Cases:

```

{
"ID": "UC-00",
"Name": "Shoe",

"Description": "A Shoe is a collection of x number of decks. Inherits Deck",

"Primary Actor": "System",

"Preconditions": ["Cards must exist",
                  "Decks must exist",
                  ],

"Postconditions": ["a collection of decks",
                   "Shoe inherits all attributes of deck", 
                   "Number of decks is variable"],
"Main Success Scenario (flow)": {1: "decide how many decks are contained within the shoe",
                                 2: "instantiate deck (a default template object to copy?)",
                                 3: "add a deck to current shoe",
                                 4: "change how many decks are stored in shoe (in default)"
                                 5: "re-instantiate shoe with x decks (default to default num shoe decks)"
                                 6: "randomize number of decks in shoe?"
                                    }
}


{
  "Name": "US-00",
  "Primary Actor": "System",
  Description:
    "Container for multiple decks."
}

{
"Class": "Shoe",

"Description": "A Shoe is a collection of x number of decks. Inherits Deck",

"Responsibility": ["instantiate_deck()",
                   "add_deck()",
                   "shoe_size()",
                   "reset_shoe()",
                   "-- rand_shoe_size(range) --",
                   ],

"Collaborator": ["Deck",
                 "Table",
                 "Seat",]

}         

```

```
{
"ID": "UC-01",
"Name": "Deck",

"Description": "A standard deck has 52 cars + 1 optional joker. 4 suits, 13 card values (Ace though King)",

"Primary Actor": "System",

"Preconditions": ["cards must exist",
                  "cards must be definable",
                  ],

"Postconditions": ["cards defined with 4 suits, 13 values",
                   "cards have an order",
                   "cards exist in a container", 
                   "cards can be dealt",
                   "deck can be shuffled", 
                   "deck can be cut",
                   "add cut card",
                   "deck can be reset (cards put back in)",
                   "(optional) peek at deck",
                   "(optional) look at deck contents",
                   "(optional) count cards in deck",
                   "(optional) cards have an image"],
"Main Success Scenario (flow)": {1: "deck is instantiated",
                                 2: "deck is shuffled",
                                 3: "deck is cut",
                                 4: "cards are dealt until cut card is passed",
                                 5: "restart from flow state 1",
                                    }
}

{
  "Name": "Deck",
  "Primary Actor": "System",
  Description:
    "Group of cards defined as a standard deck. Can cut, shuffle, and deal."
}

{
"Class": "Deck",

"Description": "Group of cards defined as a standard deck. Can cut, shuffle, and deal.",

"Responsibility": ["new_deck()",
                   "shuffle()",
                   "cut(range)",
                   "deal(card_count)",
                   "-- peek()",
                   "-- contents()",
                   "-- size()",
                   "-- set_card_face()",
                   " '--' = optional ",
                   ],

"Collaborator": ["Card",
                 "Shoe",]

}            
```

```
{
"ID": "UC-02",
"Name": "Card",

"Description": "A card is an object containing some data. It has a name, and 2 sides. It is possible for both side to contain information, however generally there is a front and back, and usually the back contains no special infomation. Cards generally exist in groups. Card faces generally have images, but this is optional",

"Primary Actor": "System",

"Preconditions": ["None",
                  ],

"Postconditions": ["A low space object with a front and back that holds information.",
                   "card is immutible once set",
                    ],
"Main Success Scenario (flow)": {1: "cards are instantiated",
                                 3: "values are assigned to cards",
                                 2: "cards can be assigned to a group",
                                 4: "cards can be read",
                                 5: "cards can be flipped",
                                    }
}

{
  "Name": "Card",
  "Primary Actor": "System",
  Description:
    "A object with 2 'faces', each containing some varying degree of value and/or information. Is generally grouped with other cards."
}

{
"Class": "Card",

"Description": "A object with 2 'faces', each containing some varying degree of value and/or information. Is generally grouped with other cards.",

"Responsibility": ["<Responsibility_1>",],

"Collaborator": ["Deck",
                 "seat",
                 "table_visualization",
                  ]

}            
```

```
{
"ID": "UC-03",
"Name": "Player",

"Description": "A player occupies a seat at the game, and makes decisions - (answers query). Players have a bank with a limited amount of funds (10,000 to start in this game). The dealer has an unlimited bank. Each player has a name, and their bank total is stored in a local file. Currently, there are 3 potential types of players: User, Dealer, Bot. These may exist in a subclass?",

"Primary Actor": "User or system",

"Preconditions": ["None?",
                  ],

"Postconditions": ["A player object exists",
                   "player has a bank",
                   "player is capable of answering queries and/or making decisions",
                   "player has name and/or id",
                   "player info is persistant and stored",
                   "a player can be AI or user controlled",
                   ],
"Main Success Scenario (flow)": {1: "user is queried for player name or id",
                                 2: "user enters name/idk",
                                 3: "system checks if name/id exists", 
                                 4: "if name/id exists, existing info can be loaded",
                                 5: "user authentification?",
                                 3: "if not a player object can be instantiated with name, ID and bank",
                                 4: "bank can be accessed to add or remove funds",
                                 5: "bank balance can be accessed",
                                 6: "all changes are immediately saved"
                                 7: "player object reads query",
                                 8: "player makes choice",
                                 9: "player logs out or leaves",
                                    }
}

{
  "Name": "Player",
  "Primary Actor": "User or System",
  Description:
    "An occupant at a seat, which keeps a bank, and possibly a persistant account. Recieves queries and makes decisions. Can be controled by an AI"
}

{
"Class": "Player",

"Description": "A player occupies a seat at the table, and makes decisions - (answers query). Players have a bank with a limited amount of funds (10,000 to start in this game). The dealer has an unlimited bank. Each player has a name, and their bank total is stored in a local file. Currently, there are 3 potential types of players: User, Dealer, Bot. These may exist in a subclass?"",

"Responsibility": ["instantiate_player()",
                   "print_query()?",
                   "add_funds()",
                   "remove_funds()",
                   "balance()",
                   "save_player()",
                   "respond()",
                   "read_query()?",
                   "make_choice()? <- if user, take in response, if AI, get response?",
                   ],

"Collaborator": ["Seat",]

}            
```

```
{
"ID": "UC-04",
"Name": "AI",

"Description": "AI are players with automated decision making. Subclass of player. Default AI player is Dealer. Dealer always takes last seat. Multiple additional AI could be added. All other players' hands (win or loose) are based on the value in the dealer hand.",

"Primary Actor": "System",

"Preconditions": ["player class exists",
                  "player class decisions can be automated",
                  "table and game rules exist in order to make decisions",
                  ],

"Postconditions": ["An automated user object",
                   "AI player can be added to table seat",
                   "Dealer is special case",],

"Main Success Scenario (flow)": {1: "table is instantiated with dealer object ",
                                 2: "other AI may or may not be added",
                                 3: "gameplay starts",
                                 4: "table queries player one at a time",
                                 5: "AI recieves query ",
                                 6: "AI processes query",
                                 7: "AI provides response",
                                 8: "AI can be removed from table (quit)?",
                                    }
}

{
  "Name": "AI",
  "Primary Actor": "System",
  Description:
    "Decision tree or system for automated players"
}

{
"Class": "<class_name>",

"Description": "<class_description>",

"Responsibility": ["<Responsibility_1>",],

"Collaborator": ["seat",
                 "table? <- read Dealer hand? <- should this be a general player function (so player can query dealer hand)?",]

}            
```

```
{
"ID": "UC-05",
"Name": "<Table>",

"Description": "The game loop happens on the table. Players can join table and buy in. Every table has a dealer and a shoe that contains x number of decks. The table also has 5 seats that represent spaces for the players to fill. Seat 5 is occupied by the dealer. ",

"Primary Actor": "System",

"Preconditions": ["Shoe",
                  "Deck",
                  "Card",
                  "Player",
                  "Seat",
                  "Hand",
                  "Playing Game",
                  ],

"Postconditions": ["X seats (default at 5)",
                   "Dealer in last/final seat",
                   "Shoe with x cards",
                   "Shoe can be dealt to seats",
                   "Seats participate in game loop",
                   "All rules of game are contained in game loop",
                   "Offers queries to seats",
                   "Recieves responses", 
                   "Reacts accordingly",
                   "(Bool Default ON) Fills an empty bank with $10,000? <- should this rule be in Player?"],
"Main Success Scenario (flow)": {1: "Table instantiates with 5 seats, a dealer in 'seat 5' and a shoe",
                                 2: "Each seat must buy in to participate in round",
                                 3: "Cards are dealt to every player. Dealer has 1 card face down",
                                 4: "Everyone can see the hands on table",
                                 5: "Players are each asked if they want to double down", 
                                 6: "Query recieved",
                                 7: "Query Response - yes means double bet 1 more card dealt, and stand",
                                 8: "Each player participates in bet, stand, bust loop unti all players complete turns",
                                 9: "pay outs are calculated",
                                 10: "pay outs provided",
                                 11: "if shoe cut card has been passed durring last round, reshuffle and cut"
                                 12: "At any point player query includes option to leave table (Should seat provide this instead of table?)",
                                 13: "At end of every round, if there is an empty seat query is offered to fill seat with a new player before buy in",
                                 14: "restart from flow state 2",

                                    }
}

{
  "Name": "Table",
  "Primary Actor": "System",
  Description:
    "Game exists on table. Most object controled by or interact with table. Defines rules and shapes gamestate"
}

{
"Class": "Table",

"Description": "The game loop happens on the table. Players can join table and buy in. Every table has a dealer and a shoe that contains x number of decks. The table also has 5 seats that represent spaces for the players to fill. Seat 5 is occupied by the dealer. ",

"Responsibility": ["instantiate_table(seats=5, <player_1=NULL, player_2=NULL, player_3=NULL, player_4=NULL, dealer> <- is this a good way?)",
                   "new_shoe(deck_count=8, joker=FALSE)",
                   "get_players()?",
                   "round_the_table(function() <- (buy_ins, double_downs, bets, pay_outs)",
                   "query_buy_in(seat)",
                   "query_double_down()",
                   "query_turn() <- hit/stand loop",
                   "deal(chair)",
                   "get_chair_state()",
                   "check_shoe()",
                   "pay_out()",
                   "clean_table()",
                   "is_21()->BOOL <after deal if player is 21 they stand> <is this in chair not atable?>",
                   "table_state()<-returns a dict",
                   ],

"Collaborator": ["Shoe",
                 "Chair",
                 ]

}            
```
```
optional if everything else is done: "hand visualization" <- prints larger visualization of a hand for current user
```
```
{
"ID": "UC-06",
"Name": "Table Visualization",

"Description": "Reads objects in game and their states, prints table state",

"Primary Actor": "System",

"Preconditions": ["Table",
                  "Card",
                  "Player",
                  "Seat",
                  "Hand",
                  "Playing game",],

"Postconditions": ["a container holding x cards",],
"Main Success Scenario (flow)": {1: "empty hand instantiated",
                                 2: "card(s) added to hand",
                                 3: "view hand",
                                 4: "empty hand",
                                 5: "return value of hand?",
                                    }
}



{
  "Name": "Table visualization",
  "Primary Actor": "System",
  Description:
    "Prints current table state in visual manner for user access. (should this also print queries? - probably)"
}

{
"Class": "Table visualization",

"Description": "Prints current table state in visual manner for user access. (should this also print queries? - probably)",

"Responsibility": ["Read table state()",
                   "table_to_string() <- turns table state in to a dict of strings (one for each line)",
                   "print_table()",
                   "print_query()",
                   "print_hand()",
                   "print()",],

"Collaborator": ["Table",
                 "Chair",
                 "Hand",]
}            
```

```
{
"ID": "UC-06",
"Name": "Seat",

"Description": "A seat is a space that is taken up at the table. A seat contains a player, a hand, and an active bet, as well as the state of gameplay for the player sitting at that seat. Seats can be empty or full. **Contained within table class?**",

"Primary Actor": "User",

"Preconditions": ["Player? <- not needed to instantiate seat, but needed for use of seat",
                  "Table? <- required for seat to communicate with game",
                  "Card <- fills hand",
                  ],

"Postconditions": ["Seat container with spot for player, hand, bet",
                   "Seat can recieve queries from table and respond*",
                   "Seat can relay queries to player and recieve response*",
                   "Seat can recieve cash from table (in form of pay out)*",
                   "Seat can recieve cash from Player (in form of buy in)*",
                   "*items with asterisc*: is it a good or bad idea for seat to act as intermediary? Should it be included as part of table class instead?",
                   "Are queries and answers sent through a menu system? pyDict?",],
"Main Success Scenario (flow)": {1: "Empty seat instantiated",
                                 2: "Player joins seat",
                                 3: "Table sends queries to seat",
                                 4: "Seat recieves bets, cards, and payout",
                                 5: "Player eventually leavs",
                                 6: "Empty seat always has empty hadn and bet"
                                 7: "Empty seat responds to all queries with '-1' "
                                    }
}

{
  "Name": "Seat",
  "Primary Actor": "System",
  Description:
    "Gamestate for each individual player is stored in their seat."
}

{
"Class": "Seat",

"Description": "A seat is a space that is taken up at the table. A seat contains a player, a hand, and an active bet, as well as the state of gameplay for the player sitting at that seat. Seats can be empty or full. **Contained within table class?**",

"Responsibility": ["join_seat()",
                   "query()",
                   "reply()",
                   "set_bet()",
                   "hit()",
                   "stand()",
                   "seat_status()",
                   "leave_table()",
                   "empty()",
                   ],

"Collaborator": ["Table",
                 "Player",
                 "Hand",
                 "Seat <- other seat objects?",
                 "Card",]

}            
```

```
{
"ID": "UC-07",
"Name": "Hand",

"Description": "A container holding x cards.",

"Primary Actor": "System",

"Preconditions": ["Seat (owns hand)",
                  "Card"],

"Postconditions": ["a container holding x cards",],
"Main Success Scenario (flow)": {1: "empty hand instantiated",
                                 2: "card(s) added to hand",
                                 3: "view hand",
                                 4: "empty hand",
                                 5: "return value of hand?",
                                    }
}

{
  "Name": "Hand",
  "Primary Actor": "System",
  Description:
    "Container for cards. Owned by Seat"
}

{
"Class": "Hand",

"Description": "A container holding x cards.",

"Responsibility": ["clear_hand()",
                   "view_hand()",
                   "value()",
                   "get_card() <- is this right?",
                   ],

"Collaborator": ["Seat",]

}            
```

```
{
"ID": "UC-08",
"Name": "Menu",

"Description": "Menu for user interface when not in game loop. Loads user(s), chooses game, exits game, offers game info",

"Primary Actor": "User",

"Preconditions": ["User access",
                  ],

"Postconditions": ["a menu",],
"Main Success Scenario (flow)": {1: "Welcome Screen",
                                 2: "Load Players",
                                 3: "Modify Players",
                                 3: "Choose Game (put load players after this?)",
                                 4: "Goodbye Screen",
                                 5: "Game Info Screen"
                                 6: "enter game loop",
                                 7: "return from game loop screen?",
                                 7: "Intellectual Property Info",
                                    }
}

{
  "Name": "Menu",
  "Primary Actor": "User",
  Description:
    "Menu accessed by user outside of the game"
}

{
"Class": "Menu",

"Description": "Menu for user interface when not in game loop. Loads user(s), chooses game, exits game, offers game info",

"Responsibility": ["TBD",],

"Collaborator": ["User",
                 "Table",
                 "user_database?"]

}            
```
