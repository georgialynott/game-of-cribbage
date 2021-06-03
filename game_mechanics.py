# This module sets up classes for playing cards, hands and players
# and the rules for creating runs, pairs etc. to score points in cribbage

# IMPORTS
from typing import Union
from itertools import chain

# GLOBAL CONSTANTS
FACE_CARD_VALUES = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}
SUITS_UNICODE = {'C': '\u2663', 'D': '\u2666', 'H': '\u2665' , 'S': '\u2660'}

# CLASSES
class Card:
    """ A playing card in a standard 52-card deck with
        a "rank" (2 - 10, (J)ack, (Q)ueen, (K)ing, or (A)ce), 
        a "suit" (Clubs, Diamonds, Hearts or Spades) and
        a value used for scoring (Aces = 1; J, Q, or K = 10; else = number on card))
        """
    def __init__(self, rank: Union[int, str], suit: str):
        self.rank = rank
        self.suit = suit.capitalize()
        # determine card value for scoring purposes
        self.value()

    def __repr__(self):
        return 'Card({r} {s})'.format(r=self.rank, s=SUITS_UNICODE[self.suit[0]])

    def value(self):
        if isinstance(self.rank, str):
            self.value = FACE_CARD_VALUES[self.rank]
        else:
            self.value = self.rank


class Deck:
    """ A standard 52-card deck with 4 suits of 13 ranks each """
    def __init__(self):
        self.cards = []
        self.build()

    def __repr__(self):
        return 'Deck({c})'.format(c=self.cards)

    def build(self):
        for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            for r in chain(['A'], range(2, 11), ['J', 'Q', 'K']):
               self.cards.append(Card(r, s))
