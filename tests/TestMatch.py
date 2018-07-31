import unittest
from Match import Match
from Players import RandomPlayer
from Players import HumanPlayer
from Players import DeterministicPlayer
from TicTacToe import TicTacToe
from Gui import KtinterGui
from Gui import CommandlineGui
from Learner import Learner

##
# Test cases for the class Match.
# @author Andrea Schuch
class TestMatch(unittest.TestCase):

    def test_2_random_players(self):
        player1 = RandomPlayer('R1')
        player2 = RandomPlayer('R2')
        game = TicTacToe()
        gui = KtinterGui(game)
        match = Match(gui, game,players=[player1, player2])
        match.play()

    def test_2_human_players(self):
        player1 = HumanPlayer('H1')
        player2 = HumanPlayer('H2')
        game = TicTacToe()
        gui = KtinterGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_random_human_players(self):
        player1 = RandomPlayer()
        player2 = HumanPlayer()
        game = TicTacToe()
        gui = KtinterGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_human_random_players(self):
        player1 = HumanPlayer()
        player2 = RandomPlayer()
        game = TicTacToe()
        gui = KtinterGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_learner_random_players(self):
        player1 = Learner()
        player2 = RandomPlayer()
        game = TicTacToe()
        gui = KtinterGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_random_learner_players(self):
        player1 = RandomPlayer()
        player2 = Learner()
        game = TicTacToe()
        gui = KtinterGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_learner_human_players(self):
        player1 = Learner()
        player2 = HumanPlayer()
        game = TicTacToe()
        gui = KtinterGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_human_learner_players(self):
        player1 = HumanPlayer()
        player2 = Learner()
        game = TicTacToe()
        gui = KtinterGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_2_random_players_cl(self):
        player1 = RandomPlayer('R1')
        player2 = RandomPlayer('R2')
        game =  TicTacToe()
        gui = CommandlineGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_2_human_players_cl(self):
        player1 = HumanPlayer('H1')
        player2 = HumanPlayer('H2')
        game = TicTacToe()
        gui = CommandlineGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()
        
    def test_random_human_players_cl(self):
        player1 = RandomPlayer()
        player2 = HumanPlayer()
        game = TicTacToe()
        gui = CommandlineGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_human_random_players_cl(self):
        player1 = HumanPlayer()
        player2 = RandomPlayer()
        game = TicTacToe()
        gui = CommandlineGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_learner_random_players_cl(self):
        player1 = Learner()
        player2 = RandomPlayer()
        game = TicTacToe()
        gui = CommandlineGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_random_learner_players_cl(self):
        player1 = RandomPlayer()
        player2 = Learner()
        game = TicTacToe()
        gui = CommandlineGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_learner_human_players_cl(self):
        player1 = Learner()
        player2 = HumanPlayer()
        game = TicTacToe()
        gui = CommandlineGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_human_learner_players_cl(self):
        player1 = HumanPlayer()
        player2 = Learner()
        game = TicTacToe()
        gui = CommandlineGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

    def test_2_deterministic_players_gui(self):
        player1 = DeterministicPlayer('D1')
        player2 = DeterministicPlayer('D2')
        game =  TicTacToe()
        gui = KtinterGui(game)
        match = Match(gui, game, players=[player1, player2])
        match.play()

if __name__ == '__main__':
    unittest.main()