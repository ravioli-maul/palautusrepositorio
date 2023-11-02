import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player('Semenko', 'EDM', 4, 12),
            Player('Lemieux', 'PIT', 45, 54),
            Player('Kurri',   'EDM', 37, 53),
            Player('Yzerman', 'DET', 42, 56),
            Player('Gretzky', 'EDM', 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
             PlayerReaderStub()
             )
        print(self.stats)

    def test_players_of_team(self):
        players = self.stats.team('PIT')
        
        self.assertEqual(len(players), 1)

    def test_search_found(self):
        player = self.stats.search('Kurri')

        self.assertEqual(player.name, 'Kurri')

    def test_search_not_found(self):
        player = self.stats.search('Luukkainen')

        self.assertIsNone(player)

# Maybe fix this in code later
#    def test_top_players_too_many(self):
#        top_players = self.stats.top(10)

#        self.assertEqual(len(top_players), 5)

    def test_top_players_default(self):
        top_players = self.stats.top(3)
        names = [player.name for player in top_players]
        correct_names = ['Gretzky', 'Lemieux', 'Yzerman']

        self.assertEqual(len(top_players), 3)
        self.assertEqual(names, correct_names)

    def test_top_players_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        names = [player.name for player in top_players]
        correct_names = ['Gretzky', 'Lemieux', 'Yzerman']

        self.assertEqual(len(top_players), 3)
        self.assertEqual(names, correct_names)

    def test_top_players_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        names = [player.name for player in top_players]
        correct_names = ['Lemieux', 'Yzerman', 'Kurri']

        self.assertEqual(len(top_players), 3)
        self.assertEqual(names, correct_names)

    def test_top_players_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        names = [player.name for player in top_players]
        correct_names = ['Gretzky', 'Yzerman', 'Lemieux']

        self.assertEqual(len(top_players), 3)
        self.assertEqual(names, correct_names)
