# Testing the `game_mechanics` module 

# IMPORTS
from game_mechanics import Card, Deck, Player

# Create a new deck
deck = Deck()
deck.shuffle()

# Create players with user-input names
player_1 = Player(input('Player 1 enter name: '))
player_2 = Player(input('Player 2 enter name: '))
print(player_1)
print(player_2)

# Create counter for rounds
round_number = 0

# Begin loop over rounds until either player reaches score of 121
while player_1.score & player_2.score < 121:

    # Start new round and print current scores
    round_number += 1
    print('Round {r}\n{p1}: {s1}, {p2}: {s2}'.format(r = round_number, 
                                                       p1 = player_1.name, 
                                                       s1 = player_1.score, 
                                                       p2 = player_2.name, 
                                                       s2 = player_2.score))

    # Select dealer based on round
    dealer = [player_1, player_2][round_number%2]

    # Deal each player a hand of 6
    player_1.hand = deck.draw(6)
    player_2.hand = deck.draw(6)
    print(player_1.name, player_1.hand)
    print(player_2.name, player_2.hand)

    # Each player discards two cards to the crib
    crib = []
    # Get discarded cards from players
    print(player_1.name)
    player_1_discard = [int(input('Choose 1st card to discard to crib: '))-1,
                    int(input('Choose 2nd card to discard to crib: '))-1]
    print(player_2.name)
    player_2_discard = [int(input('Choose 1st card to discard to crib: '))-1,
                    int(input('Choose 2nd card to discard to crib: '))-1]
    # Add discarded cards to crib
    crib.extend(player_1.discard(player_1_discard))
    crib.extend(player_2.discard(player_2_discard))
    print('Crib: ', crib)
    # Print updated player hands
    print(player_1.name, player_1.hand)
    print(player_2.name, player_2.hand)

    # Turn over starter card
    starter_card = deck.draw(1)[0]
    print('Starter ', starter_card)
    # Check if starter card is a Jack
    if starter_card.rank == 'J':
        dealer.peg(2) # dealer pegs 2 points for "his heels"
    
    # THE PLAY
    # --------
    # Starting with the dealers, players take turns placing cards, 
    # beginning with the non-dealer, face-up and adding their scores
    # up to a cumlative value of 31. If a player cannot play a card
    # without going over 31, they say "Go". The other player must then
    # place any remaining cards they can from their hand, without
    # exceeding 31. Play then restarts with the player who called 
    # "Go" playing first.

    # Begin loop for "The Play"
    # while player_1.hand is not [] & player_2.hand is not []:
    player_1.play(int(input('Choose card to play: '))-1)
    print(player_1.played_cards)
    player_2.play(int(input('Choose card to play: '))-1)
    print(player_2.played_cards)
    