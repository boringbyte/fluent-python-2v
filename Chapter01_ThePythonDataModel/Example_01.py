# A deck as a sequence of playing cards

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_suits(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    deck = FrenchDeck()
    print('--1. length')
    print(len(deck))
    print('--2. item selection')
    print(deck[0])
    print(deck[-1])
    print()
    print('--2. Random choice selection')
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
    print()
    print('--3. List slice')
    print(deck[:3])
    print('--4. for loop support')
    for card in deck[:3]:
        print(card)
