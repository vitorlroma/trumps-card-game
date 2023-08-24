import pickle as pk
from player import Player


class Players:
    def __init__(self):
        self.__players = []

    def add_player(self, nick):
        p = Player(nick)
        self.__players.append(p)
        print(f'Player {p.nickname} registered.\n')
        return p

    def search_player(self, nick):
        for player in self.__players:
            if nick == player.nickname:
                return player

        print('Player not found.')
        return None

    def read_players(self):
        arq = 'Players.dat'
        try:
            with open(arq, 'rb') as f:
                self.__players = pk.load(f)
        except IOError:
            print('File could not be read.')

    def players_bin(self):
        arq = 'Players.dat'
        try:
            with open(arq, 'wb') as f:
                pk.dump(self.__players, f)
        except IOError:
            print('File could not be read.')