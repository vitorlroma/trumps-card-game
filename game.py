from cards import Deck


class Game:
    def __init__(self, player1, player2, cards, game_type):
        self._player1 = player1
        self._player2 = player2
        self._cards = Deck(cards.deck_copy())
        self._game_type = game_type
        self._score = [0, 0]

    def give_hands(self):
        for i in range(5):
            self._player1.cards.add_card(self._cards.give_card())
            self._player2.cards.add_card(self._cards.give_card())

    def update_score(self, round_winner):
        if round_winner == 1:
            self._score[0] += 1
        elif round_winner == 2:
            self._score[1] += 1
        else:
            print('\nDraw\n')

    def round_aftermath(self, winner):
        if winner == 1:
            self._player2.cards.add_card(self._cards.give_card())
        elif winner == 2:
            self._player1.cards.add_card(self._cards.give_card())
        else:
            self._player1.cards.add_card(self._cards.give_card())
            self._player2.cards.add_card(self._cards.give_card())

    def verify_end_game(self):
        if self._player1.cards.is_empty():
            return 1
        elif self._player2.cards.is_empty():
            return 2
        else:
            return tie_breaker(self._player1.cards, self._player2.cards, 1)

    def aftermath(self, winner):
        if winner == 1:
            self._player1.update_player(True)
            self._player2.update_player(False)
        elif winner == 2:
            self._player2.update_player(True)
            self._player1.update_player(False)
        else:
            self._player1.update_player(False)
            self._player2.update_player(False)

    def match(self):
        self._cards.shuffle_cards()
        self.give_hands()
        for rounds in range(10):
            print(f'\tScore:\n{self._player1.nickname}: {self._score[0]} x {self._player2.nickname}: {self._score[1]}')

            dispute = choose_dispute(rounds)

            card1, card2 = None, None

            while card1 is None:
                card1 = choose_card(self._player1, self._game_type)
            while card2 is None:
                card2 = choose_card(self._player2, self._game_type)

            round_winner = duel(dispute, card1, card2)
            self.update_score(round_winner)
            self.round_aftermath(round_winner)

            if self._player1.cards.is_empty() or self._player1.cards.is_empty():
                break

        winner = self.verify_end_game()
        self.aftermath(winner)

        if winner == 1:
            print(f'{self._player1.nickname} venceu!!!')
        elif winner == 2:
            print(f'{self._player2.nickname} venceu!!!')
        else:
            print(f'The game ended in a draw.')


def choose_dispute(cond):
    if cond % 2 == 0:
        dispute = int(input('Player 1 chooses dispute.\nType the number:'
                            '\n\t[1]Value;\n\t[2]Strength;\n\t[3]Energia;\n\t[4]Jokenpo.'))
    else:
        dispute = int(input('Player 2 chooses dispute.\nType the number:'
                            '\n\t[1]Value;\n\t[2]Strength;\n\t[3]Energy;\n\t[4]Jokenpo.'))

    return dispute


def choose_card(player, game_type):
    if game_type == 2:
        return player.cards.rd_card()
    try:
        print(f'\n{player.nickname} chooses his card: ')
        player.show_player_hand()
        num = int(input("Pick the number of the card: "))
        card = player.cards.get_card(num - 1)
        print(f'\n{card.__str__()}\n')
        return card
    except IndexError:
        print('Invalid input.')
        return None


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
    cards = player_cards.deck
    total = 0
    for card in cards:
        if attribute == 1:
            total += card.value
        elif attribute == 2:
            total += card.strength
        elif attribute == 3:
            total += card.energy
        elif attribute == 4:
            break
    return total
