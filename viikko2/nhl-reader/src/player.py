class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.totals = self.goals + self.assists

    def __str__(self):
        return f'{self.name:22} {self.team:5} {self.goals:2} + {self.assists:2} = {self.totals:3}'
