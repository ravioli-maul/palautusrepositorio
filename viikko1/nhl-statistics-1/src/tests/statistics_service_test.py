import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
             PlayerReaderStub()
             )
        print(self.stats)

    def test_players_of_team(self):
        players = self.stats.team("PIT")
        
        self.assertEqual(len(players), 1)

# Sisäinen, testaako itse?
    #def test_sort_by_points(self):
    #     pass

    def test_search_found(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")

    def test_search_not_found(self):
        player = self.stats.search("Luukkainen")

        self.assertIsNone(player)
    
    def test_top_players(self):
        top_players = self.stats.top(3)

        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")
