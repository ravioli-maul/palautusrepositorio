from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        all_players = self.reader.get_players()
        players = [Player(player) for player in all_players\
                    if player['nationality'] == nationality]
        players.sort(key=lambda player: player.totals, reverse=True)
        return players
    