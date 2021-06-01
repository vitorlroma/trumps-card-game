from Cards import Card as ca
import random as rd

def choose_dispute(cond):
    if cond % 2 == 0:
        key = int(input('Player 1 chooses dispute.\nType the number:'
                        '\n\t[1]Value;\n\t[2]Strength;\n\t[3]Energia;\n\t[4]Jokenpo.'))
    elif cond % 2 == 1:
        key = int(input('Player 2 chooses dispute.\nType the number:'
                        '\n\t[1]Value;\n\t[2]Strength;\n\t[3]Energy;\n\t[4]Jokenpo.'))
    return key

def show_player_hand(p_cards):
    for card in p_cards:
        ca.show_card(card)

def choose_card(player_hand, mode):
    if mode == 1:
        num = int(input('Type the number of the card you choose: '))
        return player_hand[(num - 1)]
    elif mode == 2:
        num = rd.randint(1, len(player_hand))
        return player_hand[(num - 1)]


def duel(dispute, card1, card2):
    if dispute == 1:
        return comparison(card1.value, card2.value)
    elif dispute == 2:
        return comparison(card1.strength, card2.strength)
    elif dispute == 3:
        return comparison(card1.energy, card2.energy)
    elif dispute == 4:
        return jokenpo(card1.jokenpo, card2.jokenpo)
    
def update_score(score, round_winner):
    if round_winner == 1:
        score[0] += 1
    elif round_winner == 2:
        score[1] += 1


def comparison(value1, value2):
    if value1 < value2:
        return 2
    elif value1 > value2:
        return 1
    elif value1 == value2:
        return 0


def jokenpo(value1, value2):
    if  (value1 == 'Paper' and value2 == 'Scissors'
        or value1 == 'Rock' and value2 == 'Paper'
        or value1 == 'Scissors' and value2 == 'Rock'):
        return 2
    elif  (value1 == 'Rock' and value2 == 'Scissors'
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
