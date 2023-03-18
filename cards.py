import json
import random as rd
import operator


class Deck:

    def __init__(self, cards):
        self._deck = cards

    def get_deck(self):
        return self._deck.copy()

    def add_card(self, card):
        self._deck.append(card)

    def shuffle_cards(self):
        rd.shuffle(self._deck)

    def give_card(self):
        return self._deck.pop()

    def get_card(self, index):
        return self._deck.pop(index)

    def rearrange_cards(self, game_type, key):
        if game_type == 1:
            self._deck.sort(key=(operator.attrgetter('character')))
        elif key == 1:
            self._deck.sort(key=(operator.attrgetter('value')))
        elif key == 2:
            self._deck.sort(key=(operator.attrgetter('strength')))
        elif key == 3:
            self._deck.sort(key=(operator.attrgetter('energy')))
        elif key == 4:
            self._deck.shuffle_cards()

    def print_cards(self):
        for card in self._deck:
            print(card.__str__())
