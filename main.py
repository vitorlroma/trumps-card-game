from players import Players
from cards import Deck
from game import Game


class Start:
    def __init__(self):
        self.__players_list = Players()
        self.__cards = Deck()
        self.__player_one = None
        self.__player_two = None

    def __login(self, nick):
        player = self.__players_list.search_player(nick)
        if player is None:
            answer = input('\nWish to register?"Y" or "N"')
            if answer == "Y" or answer == "y":
                player = self.__players_list.add_player(nick)

        if self.__player_one is None:
            self.__player_one = player
        elif self.__player_two is None:
            self.__player_two = player

    def __play(self):
        cond = False
        while not cond:
            try:
                game_type = int(input('[1]Manual;\n[2]Random.\n'))
                cond = bool(game_type == 1 or game_type == 2)
            except ValueError:
                print('Invalid input.')

        while self.__player_one is None or self.__player_two is None:
            nick = input('Type your nickname: ')
            self.__login(nick)

        game = Game(self.__player_one, self.__player_two, self.__cards.deck(), game_type)
        game.match()

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
            elif answer == 4:
                self.__players_list.players_bin()
        except ValueError:
            print('Invalid input.')

        return answer


def main():
    answer = 0
    start = Start()
    start.read_data()

    while answer != 4:
        answer = start.menu()


if __name__ == '__main__':
    main()
