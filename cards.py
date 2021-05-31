import random as rd
import operator


class Card:
    def __init__(self):
        self.character = ''
        self.value = 0
        self.strength = 0.0
        self.energy = 0.0
        self.jokenpo = ''
    
    def __str__(self):
        return f'Character: {self.character};\nValue: {self.value};'
        + f'\nStrength: {self.strength};\nJokenpo: {self.jokenpo}'
    
    @staticmethod
    def show_card(card):
        print(f'Character: {card.character};\nValue: {card.value};'
            f'\nStrength: {card.strength};\nJokenpo: {card.jokenpo}')

    @staticmethod
    def setting_deck(cards, deck):
        for i in range(len(cards)):
            line = cards[i].split(sep=';')
            c = Card()
            c.character= line[0]
            c.value = line[1]
            c.strenght = line[2]
            c.energy = line[3]
            c.jokenpo = line[4]
            deck.append(c)

    @staticmethod
    def shuffle_cards(deck):
        return rd.shuffle(deck)

    @staticmethod
    def give_hands(deck, player1, player2):
        for i in range(10):
            aux = deck.pop()
            if i % 2 == 0:
                player1.cartas.append(aux)
            if i % 2 == 1:
                player2.cartas.append(aux)

    @staticmethod
    def rearrange_cards(player_hand, mode, key):
        if mode == 1:
            player_hand.sort(key=(operator.attrgetter('personagem')))
        elif key == 1:
            player_hand.sort(key=(operator.attrgetter('valor')))
        elif key == 2:
            player_hand.sort(key=(operator.attrgetter('forca')))
        elif key == 3:
            player_hand.sort(key=(operator.attrgetter('energia')))
        elif key == 4:
            Card.shuffle_cards(player_hand)

    @staticmethod
    def give_card(deck, player_hand):
        aux = deck.pop()
        player_hand.append(aux)

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
    
    def read_cards(deck):
        file = 'Cartas.txt'
        
        with open(file, 'r') as c:
            lista = c.read()[1:].splitlines()
        
        Card.setting_deck(lista, deck)
        
