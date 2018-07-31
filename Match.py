from Players import PlayerTypes
from Players import RandomPlayer
from Players import HumanPlayer
from Gui import KtinterGui, CommandlineGui
from Gui import CommandlineGui
from TicTacToe import TicTacToe
from Learner import Learner
from Players import Player


##
# Class for playing a match of a game. The following functionalities are supported
# 1. Playing a game manually using different graphical interfaces.
# 2. Having machine players competing against one another.
# 3. Manually playing against a machine player.
# @author Andrea Schuch

class Match:
    ##
    # @var game Internal representation of the game.

    ## @var gui Internal representation of the gui.
    ## @var players Internal representation of the players.


    ## Creates a match of a specified game.
    # @param gui Gui for displaying the games, and for interaction with human players. Must be instantiated if there is at least one human among the players.
    # If all players are players of type PlayerTypes.MACHINE, the gui can be lef None to speed up the game's execution.
    # @param game The game to be played.
    # @param players List of players (can be human or machine players).
    def __init__(self, gui, game, players=[Player('X'), Player('O')]):
        self.game = game
        self.gui = gui
        self.players = players
        self.current_player_number = 0
        self.winner = None

        for player in self.players:
            if type(player) == Learner:
                player.history = {}

        if self.gui:
            self.gui.start()

    ## Retrieves the current player. If the game has already ended, the last player will be returned.
    # @return The current player.
    def current_player(self):
        return self.players[self.current_player_number]

    ## Should always be called after the current player has completed his turn. Internally changes the current to the next player in line.
    # If the game has already ended, the current player will remain unchanged.
    # @return The next player.
    def next_player(self):
        if not self.is_game_over():
            self.current_player_number = (self.current_player_number + 1) % len(self.players)
        return self.current_player()

    ## Starts a new match and runs the game until the game-over conditions are met.
    # Machine players are asked to provide a move using @ref Player.next_move().
    # Human players' moves are collected via the gui using @ref Gui.next_move().
    # @see is_game_over() End-of-game conditions.

    def play(self):
        self.winner = None
        while not self.is_game_over():
            player = self.current_player()
            if player.type == PlayerTypes.HUMAN:
                move = self.gui.next_move(player)
            elif player.type == PlayerTypes.MACHINE:
                move = player.next_move(self.game)
                self.game.play(*move, player)
                if self.gui:
                    self.gui.play_view(*move, player)
            self.next_player()
        if self.gui:
            if self.game.is_winner(self.current_player()):
                self.gui.game_over(self.current_player())
            else:
                self.gui.game_over()

    ## Checks if the game has ended. A games is over if
    # - either of the player has won
    # - or there is a draw preventing either playing from winning.
    # Sets winner variable to current_player(), if not a draw.
    # @return True if the game is over, and false otherwise.
    def is_game_over(self):
        won = self.game.is_winner(self.current_player())
        draw = not self.game.available_moves()
        if won:
            self.winner = self.current_player()
        return won or draw

if __name__ == '__main__':
    player1 = HumanPlayer('P1')
    player2 = RandomPlayer('P2')
    game = TicTacToe()
    gui = KtinterGui(game)
    match = Match(gui, game, players=[player1, player2])
    match.play()
