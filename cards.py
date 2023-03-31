import json
import random as rd
from card import Card


class Deck:

    def __init__(self, cards):
        self._deck = cards

    @property
    def deck(self):
        return self._deck

    def deck_copy(self):
        return self._deck.copy()

    def add_card(self, card):
        self._deck.append(card)

    def shuffle_cards(self):
        rd.shuffle(self._deck)

    def give_card(self):
        return self._deck.pop()

    def get_card(self, index):
        return self._deck.pop(index)

    def rd_card(self):
        num = rd.randint(0, len(self._deck)-1)
        return self._deck.pop(num)

    def is_empty(self):
        if not self._deck:
            return True
        else:
            return False

    def read_cards(self):
        file = 'cards.json'
        try:
            with open(file) as f:
                data = json.load(f)

            for card in data['cards']:
                new_card = Card(card['Character'], card['Value'], card['Strength'], card['Energy'], card['Jokenpo'])
                self._deck.append(new_card)

        except IOError:
            print('File could not be read.')

    def __str__(self):
        for card in self._deck:
            print(card.__str__())
