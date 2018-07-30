import unittest
from Learner import Learner
from Players import Player
from TicTacToe import TicTacToe
from Players import RandomPlayer


##
# Test cases for the class "Learner".
# @author Andrea Schuch
class TestLearner(unittest.TestCase):

    def test_next_move_init(self):
        self.learner = Learner()
        tictactoe = TicTacToe()
        self.assertEqual(0, self.learner.get_reward((0,0), tictactoe.board))

    def test_set_reward(self):
        reward = 100
        self.learner = Learner()
        tictactoe = TicTacToe()
        action = tictactoe.available_moves()[0]
        self.learner.set_reward(reward, action, tictactoe.board)
        self.assertEqual(reward, self.learner.get_reward(action, tictactoe.board))

    def test_look_player(self):
        self.learner = Learner()
        tictactoe = TicTacToe()
        action = tictactoe.available_moves()[0]
        tictactoe.play(action[0], action[1], self.learner)
        self.learner.look(tictactoe)
        self.assertEqual(1, len(self.learner.history[self.learner.name]))
        self.assertEqual(action, self.learner.history[self.learner.name][0])

        self.learner.look(tictactoe)
        self.assertEqual(1, len(self.learner.history[self.learner.name]))
        self.assertEqual(action, self.learner.history[self.learner.name][0])

    def test_look_other_player(self):
        self.learner = Learner()
        self.other_player = RandomPlayer()
        tictactoe = TicTacToe()
        action = tictactoe.available_moves()[0]
        tictactoe.play(action[0], action[1], self.other_player)
        self.learner.look(tictactoe)
        self.assertEqual(1, len(self.learner.history[self.other_player.name]))
        self.assertEqual(action, self.learner.history[self.other_player.name][0])

    def test_look_both_players(self):
        self.learner = Learner()
        self.other_player = RandomPlayer()
        tictactoe = TicTacToe()

        action1 = tictactoe.available_moves()[0]
        tictactoe.play(action1[0], action1[1], self.learner)
        self.learner.look(tictactoe)
        self.assertEqual(1, len(self.learner.history[self.learner.name]))
        self.assertEqual(action1, self.learner.history[self.learner.name][0])

        action2 = tictactoe.available_moves()[0]
        tictactoe.play(action2[0], action2[1], self.other_player)
        self.learner.look(tictactoe)
        self.assertEqual(1, len(self.learner.history[self.other_player.name]))
        self.assertEqual(action2, self.learner.history[self.other_player.name][0])

    def test_play(self):
        self.learner = Learner()
        self.tictactoe = TicTacToe()
        action = self.tictactoe.available_moves()[0]
        self.tictactoe.play(action[0], action[1], self.learner)

    def test_learn_single(self):
        self.learner = Learner('X')
        self.other_player = Player('O')
        self.tictactoe = TicTacToe()

        fields=[(0,0),(0,1),(0,2)]

        for field in fields:
            self.tictactoe.play(*field,self.learner)

        self.assertEquals(fields, self.tictactoe.is_winner(self.learner))
        self.learner.learn(self.tictactoe, 100, self.learner)
        print(self.learner.rewards)

        self.tictactoe = TicTacToe()
        while (self.tictactoe.available_moves() and not self.tictactoe.is_winner(self.learner) and not self.tictactoe.is_winner(self.other_player)):
            self.tictactoe.play(*self.learner.next_move(self.tictactoe),self.learner)

        print(self.tictactoe.board)

        self.assertFalse(self.tictactoe.is_winner(self.other_player))
        self.assertEquals(fields, self.tictactoe.is_winner(self.learner))

    def test_learn_single_starting(self):
        self.learner = Learner()
        self.other_player = Player()
        self.tictactoe = TicTacToe()

        fields=[(0,0),(0,1),(0,2)]
        other_fields = [(1,0),(1,1)]

        for field in range(len(fields)):
            self.tictactoe.play(*fields[field],self.learner)
            try:
                self.tictactoe.play(*other_fields[field], self.other_player)
            except(IndexError):
                pass
            self.learner.look(self.tictactoe)

        self.assertEquals(fields, self.tictactoe.is_winner(self.learner))
        self.learner.learn(self.tictactoe, 100, self.learner)
        print(self.learner.rewards)

        self.tictactoe = TicTacToe()
        while (self.tictactoe.available_moves() and not self.tictactoe.is_winner(self.learner) and not self.tictactoe.is_winner(self.other_player)):
            self.tictactoe.play(*self.learner.next_move(self.tictactoe),self.learner)
            if (other_fields):
                self.tictactoe.play(*other_fields.pop(0), self.other_player)

        print(self.tictactoe.board)

        self.assertFalse(self.tictactoe.is_winner(self.other_player))
        self.assertEquals(fields, self.tictactoe.is_winner(self.learner))

    def test_learn_single_otherstarting(self):
        self.learner = Learner()
        self.other_player = Player()
        self.tictactoe = TicTacToe()

        fields=[(0,0),(0,1),(0,2)]
        other_fields = [(1,0),(1,1),(2,2)]

        for field in range(len(fields)):
            self.tictactoe.play(*fields[field],self.learner)
            try:
                self.tictactoe.play(*other_fields[field], self.other_player)
            except(IndexError):
                pass

        self.assertEquals(fields, self.tictactoe.is_winner(self.learner))
        self.learner.learn(self.tictactoe, 100, self.learner)
        print(self.learner.rewards)

        self.tictactoe = TicTacToe()
        while (self.tictactoe.available_moves() and not self.tictactoe.is_winner(self.learner) and not self.tictactoe.is_winner(self.other_player)):
            self.tictactoe.play(*other_fields.pop(0), self.other_player)
            self.tictactoe.play(*self.learner.next_move(self.tictactoe),self.learner)


        print(self.tictactoe.board)

        self.assertFalse(self.tictactoe.is_winner(self.other_player))
        self.assertEquals(fields, self.tictactoe.is_winner(self.learner))

if __name__ == '__main__':
    unittest.main()