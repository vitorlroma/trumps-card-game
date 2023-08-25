class Game:
    def __init__(self, player1, player2, deck, game_type):
        self.__player_one = player1
        self.__player_two = player2
        self.__cards = deck
        self.__game_type = game_type
        self.__score = [0, 0]

        print(self.__cards.__str__())

    @property
    def player_one(self):
        return self.__player_one

    @property
    def player_two(self):
        return self.__player_two

    @property
    def cards(self):
        return self.__cards

    @property
    def game_type(self):
        return self.__game_type

    def __give_hands(self):
        for _ in range(5):
            self.__player_one.cards.add_card(self.__cards.give_card())
            self.__player_two.cards.add_card(self.__cards.give_card())

    def __update_score(self, round_winner):
        if round_winner == 1:
            self.__score[0] += 1
        elif round_winner == 2:
            self.__score[1] += 1
        else:
            print('\nDraw\n')

    def __round_aftermath(self, winner):
        if winner == 1:
            self.__player_two.cards.add_card(self.__cards.give_card())
        elif winner == 2:
            self.__player_one.cards.add_card(self.__cards.give_card())
        else:
            self.__player_one.cards.add_card(self.__cards.give_card())
            self.__player_two.cards.add_card(self.__cards.give_card())

    def __verify_winner(self):
        if self.__player_one.cards.is_empty():
            return 1
        elif self.__player_two.cards.is_empty():
            return 2
        else:
            return tie_breaker(self.__player_one.cards, self.__player_two.cards, 1)

    def __aftermath(self, winner):
        if winner == 1:
            self.__player_one.update_player(True)
            self.__player_two.update_player(False)
        elif winner == 2:
            self.__player_two.update_player(True)
            self.__player_one.update_player(False)
        else:
            self.__player_one.update_player(False)
            self.__player_two.update_player(False)

    def match(self):
        self.__give_hands()
        for rounds in range(10):
            print(f'\tScore:\n{self.__player_one.nickname}: {self.__score[0]} '
                  f'x {self.__player_two.nickname}: {self.__score[1]}')

            dispute = choose_dispute(rounds)

            card1, card2 = None, None

            while card1 is None:
                card1 = choose_card(self.__player_one, self.__game_type)
            while card2 is None:
                card2 = choose_card(self.__player_two, self.__game_type)

            print(f'{card1}\nX\n{card2}')

            round_winner = duel(dispute, card1, card2)
            self.__update_score(round_winner)
            self.__round_aftermath(round_winner)

            if self.__player_one.cards.is_empty() or self.__player_one.cards.is_empty():
                break

        winner = self.__verify_winner()
        self.__aftermath(winner)

        if winner == 1:
            print(f'{self.__player_one.nickname} venceu\n!!!')
        elif winner == 2:
            print(f'{self.__player_two.nickname} venceu\n!!!')
        else:
            print(f'The game ended in a draw.\n')


def choose_dispute(cond):
    if cond % 2 == 0:
        dispute = int(input('Player 1 chooses dispute.\nType the number:'
                            '\n\t[1]Value;\n\t[2]Strength;\n\t[3]Energia;\n\t[4]Jokenpo.'))
    else:
        dispute = int(input('Player 2 chooses dispute.\nType the number:'
                            '\n\t[1]Value;\n\t[2]Strength;\n\t[3]Energy;\n\t[4]Jokenpo.'))

    return dispute


def choose_card(player, game_type):
    try:
        if game_type == 2:
            card = player.cards.rd_card()
        else:
            print(f'\n{player.nickname} chooses his card: ')
            player.show_player_hand()
            num = int(input("Pick the number of the card: "))
            card = player.cards.get_card(num - 1)

        return card
    except IndexError:
        print('You don\'t have this many cards.')
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
