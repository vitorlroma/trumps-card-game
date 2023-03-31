from cards import Deck


class Player:
    def __init__(self, nickname, lista):
        self._nickname = nickname
        self._matches_played = 0
        self._matches_won = 0
        self._success_rate = 0.0
        self._cards = Deck(lista)

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, nick):
        self._nickname = nick

    @property
    def matches_played(self):
        return self._matches_played

    @property
    def matches_won(self):
        return self._matches_won

    @property
    def success_rate(self):
        return self._success_rate

    @property
    def cards(self):
        return self._cards

    def show_player_hand(self):
        self._cards.__str__()

    def update_player(self, won):
        self._cards = Deck([])
        self._matches_played += 1
        if won:
            self._matches_won += 1
        self._success_rate = self._matches_won / self._matches_played

    def __str__(self):
        return f'Nickname: {self.nickname};\nMatches played: {self.matches_played};' \
               f'\nMatches won: {self.matches_won};\nSucces rate: {self.success_rate*100}%'
