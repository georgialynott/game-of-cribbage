# Testing the `game_mechanics` module 

# IMPORTS
from game_mechanics import Card, Deck, Player

# Create a new deck
deck = Deck()
deck.shuffle()

# Create players and deal each a hand of 6
player_1 = Player(input('Player 1 enter name: '), deck.draw(6))
player_2 = Player(input('Player 2 enter name: '), deck.draw(6))

print(player_1)
print(player_2)

# Each player discards two cards to the crib
crib = []
print(player_1.name)
player_1_discard = [int(input('Choose 1st card to discard to crib: ')),
                    int(input('Choose 2nd card to discard to crib: '))]
print(player_2.name)
player_2_discard = [int(input('Choose 1st card to discard to crib: ')),
                    int(input('Choose 2nd card to discard to crib: '))]
crib.extend(player_1.discard(player_1_discard))
crib.extend(player_2.discard(player_2_discard))
print('Crib: ', crib)
print(player_1.name, player_1.hand)
print(player_2.name, player_2.hand)

# Turn over starter card
starter_card = deck.draw(1)
print('Starter ', starter_card)