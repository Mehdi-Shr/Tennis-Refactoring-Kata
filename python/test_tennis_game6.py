import unittest

class TestTennisGame6(unittest.TestCase):

    def setUp(self):
        self.game = TennisGame6Part2("Player1", "Player2")

    def test_invalid_player_names(self):
        with self.assertRaises(ValueError):
            TennisGame6Part2("", "Player2")
        with self.assertRaises(ValueError):
            TennisGame6Part2("Player1", "")
        with self.assertRaises(ValueError):
            TennisGame6Part2(123, "Player2")
        with self.assertRaises(ValueError):
            TennisGame6Part2("Player1", 456)

    def test_won_point(self):
        self.game.won_point("Player1")
        self.assertEqual(self.game.player1Score, 1)
        self.game.won_point("Player2")
        self.assertEqual(self.game.player2Score, 1)

    def test_tie_score(self):
        self.game.won_point("Player1")
        self.game.won_point("Player2")
        self.assertEqual(self.game.score(), "Fifteen-All")

    def test_end_game_score(self):
        self.game.player1Score = 4
        self.game.player2Score = 3
        self.assert
