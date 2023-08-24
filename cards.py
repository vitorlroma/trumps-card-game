import json
import random as rd
from card import Card


class Deck:
    def __init__(self):
        self.__deck = []

    @property
    def deck(self):
        return self.__deck

    def deck_shuffled(self):
        return rd.shuffle(self.__deck.copy())

    def add_card(self, card):
        self.__deck.append(card)

    def give_card(self):
        return self.__deck.pop()

    def get_card(self, index):
        return self.__deck.pop(index)

    def rd_card(self):
        num = rd.randint(0, len(self.__deck)-1)
        return self.__deck.pop(num)

    def is_empty(self):
        if not self.__deck:
            return True
        else:
            return False

    def read_cards(self):
        arq = 'cards.json'
        try:
            with open(arq) as f:
                data = json.load(f)

            for card in data['cards']:
                new_card = Card(card['Character'], card['Value'], card['Strength'], card['Energy'], card['Jokenpo'])
                self.__deck.append(new_card)

        except IOError:
            print('File could not be read.')

    def __str__(self):
        for card in self.__deck:
            print(card.__str__())
