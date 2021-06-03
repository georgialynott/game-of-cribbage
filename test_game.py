# Testing the `game_mechanics` module 

# IMPORTS
from game_mechanics import Card, Deck, Player

# Create a new deck
deck = Deck()
deck.shuffle()

# Create players and deal each a hand of 6
player_1 = Player('Georgia', deck.draw(6))
player_2 = Player('Matt', deck.draw(6))

print(player_1)
print(player_2)

# Each player discards two cards to the crib
crib = []
crib.append(player_1.discard([1, 2]))
