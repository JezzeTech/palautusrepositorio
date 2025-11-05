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
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_existing_player(self):
        self.assertEqual(self.stats.search("Kurri").name, "Kurri")

    def test_player_not_found(self):
        self.assertIsNone(self.stats.search("Selänne"))

    def test_team_returns_all_players_from_correct_team(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)

    def test_team_not_exists(self):
        self.assertEqual(self.stats.team("NYR"), [])

    def test_top_in_points(self):
        top_players = self.stats.top(1)
        self.assertEqual(top_players[0].name, "Gretzky")