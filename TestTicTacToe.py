import unittest
from TicTacToe import TicTacToe
from Players import Player

##
# Test cases for the class "TicTacToe".
# @author Andrea Schuch
class TestTicTacToe(unittest.TestCase):

    #todo: try writing decorator for unittests: print test summary, print board, print analysis


    def setUp(self):
        self.tictactoe = TicTacToe()
        #self.tictactoe.print_board()

    def test_is_winner_negative(self):
        player = Player('X')
        row = column = 1
        self.tictactoe.play(row, column, player)
        self.assertFalse(self.tictactoe.is_winner(player))
        print('test_is_winner_negative:')
        self.tictactoe.print_board()

    def test_play_retrieve(self):
        player = Player('X')
        row = column = 1
        self.tictactoe.play(row, column, player)
        self.assertIsNotNone(self.tictactoe.retrieve(row,column))
        self.assertEqual(self.tictactoe.retrieve(row,column), 'X')
        print('test_play_retrieve:')
        self.tictactoe.print_board()

    def test_play_retrieve_boundary(self):
        player = Player('X')
        row = column = self.tictactoe.board_size() - 1
        self.tictactoe.play(row, column, player)
        self.assertIsNotNone(self.tictactoe.retrieve(row,column))
        self.assertEqual(self.tictactoe.retrieve(row, column), player.name)
        print('test_play_retrieve_boundary:')
        self.tictactoe.print_board()

    def test_is_winner_row(self):
        player = Player('X')
        row = 0
        fields = [(row, column) for column in range(self.tictactoe.board_size())]
        for field in fields:
            self.tictactoe.play(*field, player)
        self.assertTrue(self.tictactoe.is_winner(player))
        self.assertEqual(fields, self.tictactoe.is_winner(player))
        print('test_is_winner_row:')
        self.tictactoe.print_board()

    def test_is_winner_column(self):
        player = Player('X')
        column = 0
        fields = [(row, column) for row in range(self.tictactoe.board_size())]
        for field in fields:
            self.tictactoe.play(*field, player)
        self.assertTrue(self.tictactoe.is_winner(player))
        self.assertEqual(fields, self.tictactoe.is_winner(player))
        print('test_is_winner_column:')
        self.tictactoe.print_board()

    def test_is_winner_diagonal1(self):
        player = Player('X')
        fields = [(0, 0), (1, 1), (2, 2) ]
        for field in fields:
            self.tictactoe.play(*field, player)
        self.assertTrue(self.tictactoe.is_winner(player))
        self.assertEqual(fields, self.tictactoe.is_winner(player))
        print('test_is_winner_diagonal1:')
        self.tictactoe.print_board()

    def test_is_winner_diagonal2(self):
        player = Player('X')
        fields = [(0, 2), (1, 1), (2, 0)]
        for field in fields:
            self.tictactoe.play(*field, player)
        self.assertTrue(self.tictactoe.is_winner(player))
        self.assertEqual(fields, self.tictactoe.is_winner(player))
        print('test_is_winner_diagonal2:')
        self.tictactoe.print_board()

    def test_available_moves(self):
        player = Player('X')
        test_position = (1,1)
        self.tictactoe.play(*test_position, player)
        available_moves = self.tictactoe.available_moves()
        self.assertTrue(available_moves)
        self.assertNotIn(test_position,available_moves )
        print('test_available_moves:')
        self.tictactoe.print_board()

    def test_available_moves_none(self):
        player = Player('X')
        for row in range(self.tictactoe.board_size()):
            for column in range (self.tictactoe.board_size()):
                self.tictactoe.play(row, column, player)
        self.assertFalse(self.tictactoe.available_moves())
        print('test_available_moves_none:')
        self.tictactoe.print_board()

    def test_available_moves_border(self):
        player = Player('X')
        for row in range(self.tictactoe.board_size()-1):
            for column in range (self.tictactoe.board_size()-1):
                self.tictactoe.play(row, column, player)

        available_moves = self.tictactoe.available_moves()

        for position in range(self.tictactoe.board_size()):
            self.assertIn((position, self.tictactoe.board_size()-1),available_moves)
            self.assertIn((self.tictactoe.board_size()-1, position),available_moves)
        print('test_available_moves_border:')
        self.tictactoe.print_board()

if __name__ == '__main__':
    unittest.main()
