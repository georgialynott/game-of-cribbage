# This module sets up classes for playing cards, hands and players
# and the rules for creating runs, pairs etc. to score points in cribbage

# IMPORTS
from itertools import chain
from enum import Enum, auto
import random

# CLASSES
class Rank(Enum):
    ACE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    TEN = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()


class Suit(Enum):
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()


class Card:
    """ A playing card in a standard 52-card deck with
        a "rank" (2 - 10, (J)ack, (Q)ueen, (K)ing, or (A)ce), 
        a "suit" (Clubs, Diamonds, Hearts or Spades) and
        a value used for scoring (Aces = 1; J, Q, or K = 10; else = number on card))
        """
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        SUITS_UNICODE = {'CLUBS': '\u2663',
                         'DIAMONDS': '\u2666', 
                         'HEARTS': '\u2665' , 
                         'SPADES': '\u2660'}
        CARD_CHARACTERS = {'ACE': 'A',
                           'JACK': 'J',
                           'QUEEN': 'Q',
                           'KING': 'K'}
        if self.rank.name in CARD_CHARACTERS:
            rank_str = CARD_CHARACTERS[self.rank.name]
        else:
            rank_str = self.rank.value
        return '|{r} {s}|'.format(r=rank_str, s=SUITS_UNICODE[self.suit.name])

    def value(self):
        if self.rank.value > 10:
            return 10 # court cards have value 10
        else:
            return self.rank.value


class Deck:
    """ A standard 52-card deck with 4 suits of 13 ranks each """
    def __init__(self):
        self.cards = []
        for s in range(1, 5):
            for r in range(1, 14):
               self.cards.append(Card(Rank(r), Suit(s)))

    def __repr__(self):
        return 'Deck({c})'.format(c=self.cards)

    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.cards)
    
    def draw(self, n: int):
        """Draws n cards from the top of the deck"""
        draw_cards = self.cards[:n]
        self.cards[:n] = [] # remove cards drawn from deck
        return draw_cards

class Player:
    """Stores current score and cards in hand of a player"""
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.score = 0
        self.played_cards = []
        self.go_flag = 0
        
    def __repr__(self):
        return 'Player({n}, score: {s}, {h})'.format(n=self.name,
                                              s=self.score, 
                                              h=self.hand)

    def peg(self, points: int):
        """Adds points to cumulative score"""
        self.score += points
        
    def discard(self, card_pos: int):
        """Discards card(s) at `card_pos` from the player's hand"""
        return list(self.hand.pop(i) for i in sorted(card_pos, reverse=True))

    def play_card(self, card_pos: int):
        """Plays a card 'card_pos'from the player's hand, without
            discarding the card"""
        card_played = self.hand.pop(card_pos)
        self.played_cards.append(card_played)
        return card_played

