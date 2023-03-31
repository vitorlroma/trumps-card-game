from players import Players
from cards import Deck
from game import Game


def error():
    print('Invalid input.')


def login(players_list):
    nick = input('Login.\nType nickname: ')
    player = players_list.search_player(nick)
    if player is not None:
        return player

    answer = input('\nWish to register?"Y" or "N"')
    if answer == "Y" or answer == "y":
        return players_list.add_player(nick)

    return None


def play(players, cards):
    cond = False
    while not cond:
        try:
            game_type = int(input('[1]Manual;\n[2]Random.\n'))
            cond = bool(game_type == 1 or game_type == 2)
        except ValueError:
            error()

    player1, player2 = None, None
    while player1 is None:
        player1 = login(players)
    while player2 is None:
        player2 = login(players)
    game = Game(player1, player2, cards, game_type)
    game.match()


def menu(players_list, cards):
    answer = 0
    try:
        answer = int(input('Type:\n[1]Play;\n[2]Register player;\n[3]Check profile;\n[4]Exit.\n'))
        if answer == 1:
            play(players_list, cards)
        elif answer == 2:
            nick = input('Register player.\nType nickname:')
            players_list.add_player(nick)
        elif answer == 3:
            nick = input('\nType nickname:')
            print(f'\n{players_list.search_player(nick)}\n')
        elif answer == 4:
            pass
    except ValueError:
        error()

    return answer


def main():
    answer = 0
    players_list = Players()
    players_list.read_players()
    cards = Deck([])
    cards.read_cards()

    while answer != 4:
        answer = menu(players_list, cards)

    players_list.players_bin()


if __name__ == '__main__':
    main()
