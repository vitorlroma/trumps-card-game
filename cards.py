import json
import random as rd
import operator


class Card:
    def __init__(self, character, value, strength, energy, jokenpo):
        self.character = character
        self.value = value
        self.strength = strength
        self.energy = energy
        self.jokenpo = jokenpo

    @str
    def show_card(card):
        print(f'Character: {card.character};\nValue: {card.value};'
              f'\nStrength: {card.strength};\nJokenpo: {card.jokenpo}')


class Deck:
    def __init__(self):
        self.__deck = []

    def get_deck(self):
        return self.__deck.copy()

    def add_card(self, card):
        self.deck.append(card)

    def shuffle_cards(self):
        rd.shuffle(self.deck)

    def give_card(self):
        return self.deck.pop()

    @staticmethod
    def rearrange_cards(player_hand, mode, key):
        if mode == 1:
            player_hand.sort(key=(operator.attrgetter('character')))
        elif key == 1:
            player_hand.sort(key=(operator.attrgetter('value')))
        elif key == 2:
            player_hand.sort(key=(operator.attrgetter('strength')))
        elif key == 3:
            player_hand.sort(key=(operator.attrgetter('energy')))
        elif key == 4:
            Card.shuffle_cards(player_hand)


    @staticmethod
    def aftermath(deck, p1c, p2c, winner):
        p1c.pop()
        p2c.pop()
        if winner == 1:
            Card.give_card(deck, p2c)
        elif winner == 2:
            Card.give_card(deck, p1c)
        elif winner == 0:
            Card.give_card(deck, p1c)
            Card.give_card(deck, p2c)
