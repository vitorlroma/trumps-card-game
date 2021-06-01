from Players import Player as pl
from Cards import Card as ca
import game as gm


def winner(p1, p2, num):
    if num == 1:
        print('O jogador 1 venceu!!!')
        p1.update_player(p1, True)
        p2.update_player(p2, False)
    elif num == 2:
        print('O jogador 2 venceu!!!')
        p1.update_player(p1, False)
        p2.update_player(p2, True)
    elif num == 0:
        print('The game ended in a draw')


def play(deck, p1, p2, mode):
    index = 0
    score = [0, 0]
    ca.shuffle_cards(deck)
    p1_cards = []
    p2_cards = []
    ca.give_hands(deck, p1_cards, p2_cards)
    while index in range(10):
        dispute = gm.choose_dispute(index)
        ca.rearrange_cards(p1_cards, mode, dispute)
        ca.rearrange_cards(p2_cards, mode, dispute)
        print(f'\tScore:\n{p1.nickname}: {score[0]} x {p2.nickname}: {score[1]}')
        print('Player 1 chooses his card: ')
        gm.show_player_cards(p1_cards)
        card1 = gm.choose_card(p1_cards, mode)
        print('Player 2 chooses his card:')
        gm.show_player_cards(p2_cards)
        card2 = gm.choose_card(p2_cards, mode)
        round_winner = gm.duel(dispute, card1, card2)
        gm.update_score(score, round_winner)
        ca.aftermath(deck, p1_cards, p2_cards, round_winner)
        if not p1_cards:
            winner(p1, p2, 1)
            return
        elif not p2_cards:
            winner(p1, p2, 2)
            return

    winner(gm.tie_breaker(p1_cards, p2_cards, 1))
    

def menu(players, deck):
    answer = int(input('Type:\n[1]Play;\n[2]Register player;\n[3]Exit.\n'))
    if answer == 1:
        mode = int(input('[1]Manual;\n[2]Random.\n'))
        player1 = pl.verify_player(players)
        player2 = pl.verify_player(players)
        play(deck, player1, player2, mode)
    elif answer == 2:
        nick = input('Registering player.\nType nickname:')
        pl.register_player(players, nick)
    elif answer == 3:
        pass
    else:
        print('Undefined answer.\n')

    return answer

def main():
    answer = 0
    players_list = []
    deck = []
 
    pl.read_players(players_list)
    ca.read_cards(deck)

    while answer != 3:
        menu(players_list, deck)
    
if __name__ == '__main__':
    main()
