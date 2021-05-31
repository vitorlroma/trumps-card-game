import pickle as pk


class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.matches_played = 0
        self.matches_won = 0
        self.succes_rate = 0.0
    
    @staticmethod
    def show_player(p):
        print(f'Nick: {p.nickname};\nMatches played: {p.matches_played};'
              f'\nMatches won: {p.matches_won};\nSucces rate: {p.succes_rate}')
    
    @staticmethod
    def register_player(players_list, nick):
        p = Player(nick)
        players_list.append(p)
        print(f'Player {p.nickname} registered.\n')
    
    @staticmethod
    def update_player(player, bool):
        player.matches_played += 1
        if bool:
            player.matches_won += 1
            player.succes_rate = player.matches_won/player.matches_played

    @staticmethod
    def search_player(players, nick):
        for player in players:
            if nick == player.nickname:
                return player
            else:
                continue
        return None    

    @staticmethod
    def verify_player(players_list):
        nick = input('Login.\nType nickname: ')
        player = Player.search_player(players_list, nick)
        if player:
            Player.show_player(player)
            return player
        print('Unregistered player.\n')
        answer = input('Wish to register? Yes or No')
        if answer == "yes" or answer == "Yes":
            Player.register_player(players_list, nick)
        elif answer == "no" or answer == "No":
            Player.verify_player(players_list)
        return Player.search_player(players_list, nick)

    def read_players(players):
        file = 'Players.dat'
        try:
            with open(file, 'rb') as f:
                aux_list = pk.load(f)
        except IOError:
          print('File could not be read.')
    
        return aux_list

    def players_bin(jogadores):
        file = 'Players.dat'
        try:
            with open(file, 'ab') as f:
                pk.dump(jogadores, f)
        except IOError:
            print('File could not be read.')