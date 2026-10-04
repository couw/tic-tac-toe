import unittest
from app import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_initial_board(self):
        self.assertEqual(self.game.board, [TicTacToe.EMPTY] * 9)
        self.assertEqual(len(self.game.get_available_moves()), 9)

    def test_get_available_moves(self):
        self.game.board[0] = TicTacToe.CROSS
        self.game.board[4] = TicTacToe.NOUGHT
        available_moves = self.game.get_available_moves()
        self.assertEqual(len(available_moves), 7)
        self.assertNotIn(0, available_moves)
        self.assertNotIn(4, available_moves)

    def test_check_winner_horizontal(self):
        # Test horizontal win (top row)
        self.game.board[0] = TicTacToe.CROSS
        self.game.board[1] = TicTacToe.CROSS
        self.game.board[2] = TicTacToe.CROSS
        self.assertTrue(self.game.check_winner(TicTacToe.CROSS))
        self.assertFalse(self.game.check_winner(TicTacToe.NOUGHT))

    def test_check_winner_vertical(self):
        # Test vertical win (middle column)
        self.game.board[1] = TicTacToe.NOUGHT
        self.game.board[4] = TicTacToe.NOUGHT
        self.game.board[7] = TicTacToe.NOUGHT
        self.assertTrue(self.game.check_winner(TicTacToe.NOUGHT))
        self.assertFalse(self.game.check_winner(TicTacToe.CROSS))

    def test_check_winner_diagonal(self):
        # Test diagonal win
        self.game.board[0] = TicTacToe.CROSS
        self.game.board[4] = TicTacToe.CROSS
        self.game.board[8] = TicTacToe.CROSS
        self.assertTrue(self.game.check_winner(TicTacToe.CROSS))

    def test_is_draw(self):
        # Test when not draw
        self.game.board[0] = TicTacToe.CROSS
        self.assertFalse(self.game.is_draw())

        # Test full board
        self.game.board = [
            TicTacToe.CROSS, TicTacToe.NOUGHT, TicTacToe.CROSS,
            TicTacToe.CROSS, TicTacToe.NOUGHT, TicTacToe.CROSS,
            TicTacToe.NOUGHT, TicTacToe.CROSS, TicTacToe.NOUGHT
        ]
        self.assertTrue(self.game.is_draw())

if __name__ == '__main__':
    unittest.main()
