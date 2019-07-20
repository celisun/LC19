# generic deck of cards for games ? yes, design generic deck and extend it
# asusme 52 cards (2-10, jack, queen, king, ace and 4 suits? y
# assume all inputs valid or do we need to validate them? valid

from enum import Enum
from abc import ABC, abstractmethod

class Suit(Enum):
    HEART = 0
    DIAMOND = 1
    CLUBS = 2
    SPADE = 3

class Card(ABC):
    def __init__(self, value, suit):
        self._value = value
        self.suit = suit
        self.is_available = True

    @property
    @abstractmethod
    def value(self):
        pass

    @value.setter
    @abstractmethod
    def value(self, other):
        pass

class BlackJackCard(Card):
    def __init(self, value, suit):
        super(BlackJackCard, self).__init__(value, suit)

    def is_ace(self):
        return self._value == 1

    def is_faced_card(self):
        return 10 < self._value <= 13

    @property
    def value(self):
        if self.is_ace():
            return 1
        elif self.is_face_card():
            return 10
        else:
            return self._value

    @value.setter
    def value(self, new_value):
        if 1 <= new_value <= 13:
            self._value = new_value
        else:
            raise ValueError("invalid")

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def score(self):
        total_value = 0
        for c in self.cards:
            total_value += c.value
        return total_value

    def place_card(self, i):
        card = self.card[i] if 0 <= i < len(self.cards) else None
        del self.cards[i]
        return card

class BlackJackHand(Hand):

    BLACKJACK = 21

    def __init__(self, cards):
        super(BlackJackHand, self).__init__(cards)

    def score(self):

    def possible_scores(self):

class Deck(object):
    def __init__(self, cards):
        self.cards = cards
        self.deal_i = 0

    def remaining_cards(self):
        return len(self.cards) - self.deal_i

    def deal_card(self):
        try:
            card = self.cards[self.deal_i]
            card.is_available = False
            self.deal_i += 1
        except IndexError:
            return None
        return card
    def shuffle(self):
    def reset_and_shuffle(self):
