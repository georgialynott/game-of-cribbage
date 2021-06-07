# testing behaviour of `Card` class, and enums `Rank` and `Suit`

from game_mechanics import Rank, Suit, Card

foo_rank = Rank['ACE']
foo_suit = Suit['HEARTS']

print(foo_rank) # expect: Rank.ACE
print(foo_suit) # expect: Suit.HEARTS

print(Card(foo_rank, foo_suit)) # expect: Card(A <\u2665>)

print(Card(Rank['THREE'], Suit['DIAMONDS'])) # expect: Card(3 <\u2666>)
print(Card(Rank['KING'], Suit['CLUBS'])) # expect: Card(K <\u2663>)
print(Card(Rank['TEN'], Suit['SPADES'])) # expect: Card(10 <\u2660>)

print(Card(Rank['KING'], Suit['CLUBS']).value) # expect: 10