class TennisGame:
    SCORE_NAMES = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty"
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_player1 = 0
        self.score_player2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score_player1 = self.score_player1 + 1
        else:
            self.score_player2 = self.score_player2 + 1

    def is_tied(self):
        return self.score_player1 == self.score_player2

    def is_endgame(self):
        difference = abs(self.score_player1 - self.score_player2)
        return max(self.score_player1, self.score_player2) >= 4 and difference >= 1

    def get_score(self):
        if self.is_tied():
            return self.score_when_tied()
        if self.is_endgame():
            return self.score_when_endgame()
        return self.score_in_play()

    def score_in_play(self):
        return self.SCORE_NAMES.get(self.score_player1, "") +\
              "-" + self.SCORE_NAMES.get(self.score_player2, "")

    def score_when_tied(self):
        return "Deuce" if self.score_player1 >= 3 else self.SCORE_NAMES[self.score_player1] + "-All"

    def score_when_endgame(self):
        difference = self.score_player1 - self.score_player2
        if difference == 1:
            return "Advantage " + self.player1_name
        if difference == -1:
            return "Advantage " + self.player2_name
        if difference >= 2:
            return "Win for " + self.player1_name
        return "Win for " + self.player2_name
