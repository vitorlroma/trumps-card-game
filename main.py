import players
import cards
import json
import game as gm


def winner(p1, p2, num):
    if num == 1:
        print('O jogador 1 venceu!!!')
        p1.update_player(p1, True)
        p2.update_player(p2, False)
    elif num == 2:
        print('O jogador 2 venceu!!!')
        p1.update_player(p1, False)
        p2.update_player(p2, True)
    elif num == 0:
        print('The game ended in a draw')


def login(players_list):
    nick = input('Login.\nType nickname: ')
    player = players_list.search_player(nick)
    if player is not None:
        return player

    answer = input('Player not found.\n Wish to register?"Y" or "N"')
    if answer == "Y":
        return players_list.add_player(nick)

    return None


def menu(players_list, deck):
    answer = int(input('Type:\n[1]Play;\n[2]Register player;\n[3]Exit.\n'))
    if answer == 1:
        mode = int(input('[1]Manual;\n[2]Random.\n'))
        player1 = login(players_list)
        player2 = login(players_list)
        gm.play(deck.get_deck(), player1, player2, mode)
    elif answer == 2:
        nick = input('Register player.\nType nickname:')
        players_list.add_player(nick)
    elif answer == 3:
        pass
    else:
        print('Undefined answer.\n')

    return answer


def read_cards(deck):
    file = 'cards.json'
    try:
        with open(file) as f:
            data = json.load(f)

        for card in data['cards']:
            new_card = cards.Card(card['Character'], card['Value'], card['Strength'], card['Energy'], card['Jokenpo'])
            deck.add_card(new_card)

    except IOError:
        print('File could not be read.')


def main():
    answer = 0
    players_list = players.Players()
    players_list.read_players()
    deck = cards.Deck()

    while answer != 3:
        menu(players_list, deck)

    players_list.players_bin()

if __name__ == '__main__':
    main()
