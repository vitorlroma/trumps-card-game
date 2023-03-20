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
    def cards(self):
        return self._cards

    def show_player_hand(self):
        self._cards.print_cards()

    def update_player(self, won):
        self._cards = None
        self._matches_played += 1
        if won:
            self._matches_won += 1
            self._success_rate = self._matches_won / self._matches_played

    def __str__(self):
        return f'Nickname: {self._nickname};\nMatches played: {self._matches_played};' \
               f'\nMatches won: {self._matches_won};\nSucces rate: {self._success_rate}'
