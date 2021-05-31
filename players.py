class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.matches_played = 0
        self.matches_won = 0
        self.succes_rate = 0.0
     
    def __str__(self):
        '''
        Como usar:
        obj = Player("nickname")
        print(obj)
        '''
        return f'Nick: {self.nickname};\nMatches played: {self.matches_played};'
              f'\nMatches won: {self.matches_won};\nSucces rate: {self.succes_rate}'
   
    @staticmethod
    def register_player(players_list, nick):
        p = Player(nick)
        players_list.append(p)
        print(f'Jogador {p.nickname} cadastrado.\n')
    
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
        print('Jogador não cadastrado.\n')
        Player.register_player(players_list, nick)
        return Player.search_player(players_list, nick)

  # def read_players():
#       file = 'jogadores.dat'
    #   try:
    #       with open(file, 'rb') as f:
    #           lista = pk.load(arquivo)
    #   except IOError:
    #       print('Arquivo não pode ser acessado.')
    
    #     return lista

    # def jogadores_bin(jogadores):
    #     file = 'jogadores.dat'
    #     with open(file, 'ab') as f:
    #         pk.dump(jogadores, f)
