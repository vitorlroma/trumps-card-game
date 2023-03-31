import pickle as pk
from player import Player


class Players:
    def __init__(self):
        self.players = []

    def add_player(self, nick):
        lista = []
        p = Player(nick, lista)
        self.players.append(p)
        print(f'Player {p.nickname} registered.\n')
        return p

    def search_player(self, nick):
        for player in self.players:
            if nick == player.nickname:
                return player
        return 'Player not found.'

    def read_players(self):
        file = 'Players.dat'
        try:
            with open(file, 'rb') as f:
                self.players = pk.load(f)
        except IOError:
            print('File could not be read.')

    def players_bin(self):
        file = 'Players.dat'
        try:
            with open(file, 'wb') as f:
                pk.dump(self.players, f)
        except IOError:
            print('File could not be read.')
