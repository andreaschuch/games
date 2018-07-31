from enum import Enum
import random


##
# Type of players to distinguish between
# - human players who operate the game via an interface and
# - machine players who play automatically.
# @author Andrea Schuch
class PlayerTypes(Enum):
    HUMAN =1
    MACHINE =2


##
# A player for a game (such as TicTacToe).
# @author Andrea Schuch
class Player:

    ##
    # Constructs a player.
    # @param name The player's name. Used for marking the board.
    # @param type The player's type, i.e. PlayerTypes.HUMAN for human players, and PlayerTypes.MACHINE for automated players.
    def __init__(self, name='P', type=PlayerTypes.MACHINE):
        self.name = name
        self.type = type


##
# A human player who is operated buy a user via a GUI interface.
# @author Andrea Schuch
class HumanPlayer(Player):

    ##
    # Constructs a human player.
    # @param name The player's name. Used for marking the board.
    def __init__(self, name='H'):
        super().__init__(name, PlayerTypes.HUMAN)


##
# An automated player who chooses his moves randomly.
# @author Andrea Schuch
class RandomPlayer(Player):

    ##
    # Constructs a random player.
    # @param name The player's name. Used for marking the board.
    def __init__(self,name='R'):
        super().__init__(name, PlayerTypes.MACHINE)

    ##
    # Determines the player's next move, at the current state of the game.
    # The random player takes a random choice from all available moves in the current state of a game.
    # @param game The game.
    # @return The move chosen by the player.
    def next_move(self, game):
        return random.choice(game.available_moves())

class DeterministicPlayer(Player):
    ##
    # Constructs a deterministic player.
    # @param name The player's name. Used for marking the board.
    def __init__(self,name='D'):
        super().__init__(name, PlayerTypes.MACHINE)

    ##
    # Determines the player's next move, at the current state of the game.
    # The deterministic player always takes the first choice of all available moves in the current state of a game.
    # @param game The game.
    # @return The move chosen by the player.
    def next_move(self, game):
        return game.available_moves()[0]