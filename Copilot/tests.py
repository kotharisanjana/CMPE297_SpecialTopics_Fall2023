import unittest
from ludo import LudoGame

class TestLudoGame(unittest.TestCase):
    def setUp(self):
        self.game = LudoGame()

    def test_move_piece(self):
        # Test moving a piece
        self.game.move_piece(0, 0, 3)
        self.assertEqual(self.game.piece_position[0][0], 3)

    def test_check_board_bounds(self):
        # Test moving a piece off the end of the board
        self.game.move_piece(0, 0, 52)
        self.assertEqual(self.game.piece_position[0][0], 0)

    def test_check_capture(self):
        # Test capturing an opponent's piece
        self.game.move_piece(0, 0, 3)
        self.game.move_piece(1, 0, 3)
        self.assertEqual(self.game.piece_position[0][0], 0)

    def test_print_board(self):
        # Test printing the board
        self.game.move_piece(0, 0, 3)
        self.game.print_board()
        self.assertEqual(self.game.board[3], 1)

if __name__ == '__main__':
    unittest.main()