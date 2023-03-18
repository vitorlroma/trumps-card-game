from cards import Deck


class Game:
    def __init__(self, player1, player2, cards, game_type):
        self._player1 = player1
        self._player2 = player2
        self._cards = Deck(cards.get_deck())
        self._game_type = game_type
        self._score = [0, 0]

    def give_hands(self):
        for i in range(5):
            self._player1.cards.add_card(self._cards.give_card())
            self._player2.cards.add_card(self._cards.give_card())

    def choose_dispute(self, cond):
        if cond % 2 == 0:
            dispute = int(input('Player 1 chooses dispute.\nType the number:'
                                '\n\t[1]Value;\n\t[2]Strength;\n\t[3]Energia;\n\t[4]Jokenpo.'))
        else:
            dispute = int(input('Player 2 chooses dispute.\nType the number:'
                                '\n\t[1]Value;\n\t[2]Strength;\n\t[3]Energy;\n\t[4]Jokenpo.'))

        self._player1.cards.rearrange_cards(self._game_type, dispute)
        self._player2.cards.rearrange_cards(self._game_type, dispute)

        return dispute

    def update_score(self, round_winner):
        if round_winner == 1:
            self._score[0] += 1
        elif round_winner == 2:
            self._score[1] += 1

    def aftermath(self, winner):
        if winner == 1:
            self._player2.cards.add_card(self._cards.give_card)
        elif winner == 2:
            self._player1.cards.add_card(self._cards.give_card)
        elif winner == 0:
            self._player1.cards.add_card(self._cards.give_card)
            self._player2.cards.add_card(self._cards.give_card)

    def verify_end_game(self):
        if not self._player1.cards():
            self._player1.update_player(True)
        elif not self._player2.cards():
            self._player2.update_player(True)

    def match(self):
        self._cards.shuffle_cards()
        self.give_hands()
        for rounds in range(10):
            print(f'\tScore:\n{self._player1.nickname}: {self._score[0]} x {self._player2.nickname}: {self._score[1]}')

            dispute = self.choose_dispute(rounds)

            print('Player 1 chooses his card: ')
            self._player1.show_player_hand()
            num = int(input("Pick the number of the card: "))
            card1 = self._player1.cards.get_card(num - 1)
            print('Player 2 chooses his card:')
            self._player2.show_player_hand()
            num = int(input("Pick the number of the card: "))
            card2 = self._player1.cards.get_card(num - 1)

            winner = duel(dispute, card1, card2)
            self.aftermath(winner)


def duel(dispute, card1, card2):
    if dispute == 1:
        return comparison(card1.value, card2.value)
    elif dispute == 2:
        return comparison(card1.strength, card2.strength)
    elif dispute == 3:
        return comparison(card1.energy, card2.energy)
    elif dispute == 4:
        return jokenpo(card1.jokenpo, card2.jokenpo)


def comparison(value1, value2):
    if value1 < value2:
        return 2
    elif value1 > value2:
        return 1
    elif value1 == value2:
        return 0


def jokenpo(value1, value2):
    if (value1 == 'Paper' and value2 == 'Scissors'
            or value1 == 'Rock' and value2 == 'Paper'
            or value1 == 'Scissors' and value2 == 'Rock'):
        return 2
    elif (value1 == 'Rock' and value2 == 'Scissors'
          or value1 == 'Scissors' and value2 == 'Paper'
          or value1 == 'Paper' and value2 == 'Rock'):
        return 1
    elif value1 == value2:
        return 0


def tie_breaker(p1c, p2c, attribute):
    sum1 = sum_of_cards(p1c, attribute)
    sum2 = sum_of_cards(p2c, attribute)
    if sum1 < sum2:
        return 1
    elif sum2 < sum1:
        return 2
    elif sum1 == sum2:
        return tie_breaker(p1c, p2c, attribute + 1)
    elif attribute == 4:
        return 0


def sum_of_cards(player_cards, attribute):
    total = 0
    for card in player_cards:
        if attribute == 1:
            total += card.value
        elif attribute == 2:
            total += card.strength
        elif attribute == 3:
            total += card.energy
        elif attribute == 4:
            break
    return total
