
# Broad Requirements:

Multiplayer

Uses Named Tuples

Use Object Serialization

# modules/classes

## Players:
  
### Properties:
  - Bank
  - Hand? (or is this part of the table/game object)
  - 

### Actions:

- Buy In

- optional bonus action (before action)
  - Double Down

- Hit
- Stand
- Bet
- quit 

    
### Dealer is a special player - part of table?:

### Properties:
-      
### Actions:
- Hit
- Stand
- Flip
- Decision

Dealer?
- Automation/Decision



## Cards

### Properties: 

### Actions: 


## Table



### Properties:
- chair
  - properties:
    - player
    - bet
    - bust(bool)
    - stand(bool)  
- turn
- shoe
  - shuffle 
  - deal  
  - cut 
  - cut card 


### Actions:
- render table
- get seats
- start game
- end game
- ask for bets 
- pay out


### Shoe (is this an object or property belonging to table?)


# Game flow:
- user starts game:
  - 

- instantiate table

for player in player_list
- Buy In
- deal_table
- for player in playerlist
  - check if player can double down (bool)
  - Ask if player wants to double down (bool) 
  -  if player does double down
    - double bet (if possible)
    - deal_card(player, 1, face_up = true)
    - stand  
- For player in PLayer_list
  - while does not stand or does not bust or hand not equal 21
  - < print probability of cards that will get 21 (or under)?
  - 

