# testing behaviour of `Card` class, and enums `Rank` and `Suit`

from game_mechanics import Rank, Suit, Card

foo_rank = Rank['TWO']
foo_suit = Suit['HEARTS']

print(foo_rank) # expect: Rank.TWO
print(foo_suit) # expect: Suit.HEARTS

print(Card(foo_rank, foo_suit)) # expect: Card(TWO <\u2665>)
