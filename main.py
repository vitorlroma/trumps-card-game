from players import Players
from cards import Deck
from game import Game


class Start:
    def __init__(self):
        self.__players_list = Players()
        self.__cards = Deck()
        self.__game = Game()

    def __login(self, nick):
        player = self.__players_list.search_player(nick)
        if player is None:
            answer = input('\nWish to register?"Y" or "N"')
            if answer == "Y" or answer == "y":
                player = self.__players_list.add_player(nick)

        if player is not None and self.__game.player1 is None:
            self.__game.player1(player)
        elif player is not None and self.__game.player2 is not None:
            self.__game.player2(player)

    def __play(self):
        cond = False
        while not cond:
            try:
                game_type = int(input('[1]Manual;\n[2]Random.\n'))
                cond = bool(game_type == 1 or game_type == 2)
            except ValueError:
                print('Invalid input.')

        nick = input('Type your nickname: ')
        self.__login(nick)
        nick = input('Type your nickname: ')
        self.__login(nick)

        self.__game.cards(self.__cards.deck_shuffled())
        self.__game.match()

    def read_data(self):
        self.__players_list.read_players()
        self.__cards.read_cards()

    def menu(self):
        answer = 0
        try:
            answer = int(input('Type:\n[1]Play;\n[2]Register player;\n[3]Check profile;\n[4]Exit.\n'))
            if answer == 1:
                self.__play()
            elif answer == 2:
                nick = input('Register player.\nType nickname:')
                self.__players_list.add_player(nick)
            elif answer == 3:
                nick = input('\nType nickname:')
                print(f'\n{self.__players_list.search_player(nick)}\n')
        except ValueError:
            print('Invalid input.')

        return answer


def main():
    answer = 0
    start = Start()
    start.read_data()

    while answer != 4:
        answer = start.menu()

    # players_list.players_bin()


if __name__ == '__main__':
    main()
