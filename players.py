import pickle as pk


class Player:
    def __init__(self, nickname):
        self.__nickname = nickname
        self.__matches_played = 0
        self.__matches_won = 0
        self.__succes_rate = 0.0
        self.__cards = []

    def get_cards(self):
        return self.__cards

    def update_player(self, won):
        self.matches_played += 1
        if won:
            self.matches_won += 1
            self.succes_rate = self.matches_won / self.matches_played

    @str
    def show_player(p):
        print(f'Nick: {p.nickname};\nMatches played: {p.matches_played};'
              f'\nMatches won: {p.matches_won};\nSucces rate: {p.succes_rate}')


class Players:
    def __init__(self):
        self.players = []

    def add_player(self, nick):
        p = Player(nick)
        self.players.append(p)
        print(f'Player {p.nickname} registered.\n')
        return p

    def search_player(self, nick):
        for player in self.players:
            if nick == player.nickname:
                return player
        return None

    def read_players(self):
        file = 'players.dat'
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
