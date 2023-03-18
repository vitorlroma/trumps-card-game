import json
from players import Players
from card import Card
from cards import Deck
from game import Game


def login(players_list):
    nick = input('Login.\nType nickname: ')
    player = players_list.search_player(nick)
    if player is not None:
        return player

    answer = input('Player not found.\n Wish to register?"Y" or "N"')
    if answer == "Y":
        return players_list.add_player(nick)

    return None


def menu(players_list, cards):
    try:
        answer = int(input('Type:\n[1]Play;\n[2]Register player;\n[3]Exit.\n'))
        if answer == 1:
            game_type = int(input('[1]Manual;\n[2]Random.\n'))
            player1 = login(players_list)
            player2 = login(players_list)
            if player1 and player2:
                game = Game(player1, player2, cards, game_type)
                game.match()
        elif answer == 2:
            nick = input('Register player.\nType nickname:')
            players_list.add_player(nick)
        elif answer == 3:
            pass
        else:
            print('Undefined answer.\n')
    except ValueError:
        print('Undefined answer.\n')

    return answer


def read_cards(cards):
    file = 'cards.json'
    try:
        with open(file) as f:
            data = json.load(f)

        for card in data['cards']:
            new_card = Card(card['Character'], card['Value'], card['Strength'], card['Energy'], card['Jokenpo'])
            cards.append(new_card)

    except IOError:
        print('File could not be read.')


def main():
    answer = 0
    players_list = Players()
    players_list.read_players()
    cards = []
    read_cards(cards)
    cards = Deck(cards)

    while answer != 3:
        answer = menu(players_list, cards)

    players_list.players_bin()


if __name__ == '__main__':
    main()
