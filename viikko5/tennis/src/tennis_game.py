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

    def get_score(self):
        score = ""
        temp_score = 0

        if self.score_player1 == self.score_player2:
            if self.score_player1 == 0:
                score = "Love-All"
            elif self.score_player1 == 1:
                score = "Fifteen-All"
            elif self.score_player1 == 2:
                score = "Thirty-All"
            else:
                score = "Deuce"
        elif self.score_player1 >= 4 or self.score_player2 >= 4:
            minus_result = self.score_player1 - self. score_player2

            if minus_result == 1:
                score = f"Advantage {self.player1_name}"
            elif minus_result == -1:
                score = f"Advantage {self.player2_name}"
            elif minus_result >= 2:
                score = f"Win for {self.player1_name}"
            else:
                score = f"Win for {self.player2_name}"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.score_player1
                else:
                    score += "-"
                    temp_score = self.score_player2

                score += self.SCORE_NAMES[temp_score]

        return score
