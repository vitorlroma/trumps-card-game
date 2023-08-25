from cards import Deck


class Player:
    def __init__(self, nickname):
        self.__nickname = nickname
        self.__matches_played = 0
        self.__matches_won = 0
        self.__success_rate = 0.0
        self.__cards = Deck()

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, nick):
        self.__nickname = nick

    @property
    def matches_played(self):
        return self.__matches_played

    @property
    def matches_won(self):
        return self.__matches_won

    @property
    def success_rate(self):
        return self.__success_rate

    @property
    def cards(self):
        return self.__cards

    def show_player_hand(self):
        self.__cards.__str__()

    def update_player(self, won):
        self.__cards = Deck()
        self.__matches_played += 1
        if won:
            self.__matches_won += 1
        self.__success_rate = self.__matches_won / self.__matches_played

    def __str__(self):
        return f'Nickname: {self.__nickname};\nMatches played: {self.__matches_played};' \
               f'\nMatches won: {self.__matches_won};\nSucces rate: {self.__success_rate*100}%'
