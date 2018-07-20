from Players import Player
import random


##
# A player who uses Reinforcement learning to learn from experience to improve his playing skills.
# @author Andrea Schuch
class Learner(Player):
    learning_rate = 0.3
    discount_factor = 0.1

    def __init__(self, name='L'):
        super().__init__(name)
        self.rewards = {}
        self.history = {}
        self.random_exploration = False

    ##
    # Determines the player's next move, at the current state of the game.
    # @param game The game.
    # @return The move chosen by the player.
    def next_move(self, game):
        self.look(game)
        board = game.board
        available_moves = game.available_moves()

        if self.random_exploration:
            move = random.choice(available_moves)
        else:
            move = max(available_moves, key=lambda move: self.get_reward(move, game.board), default=0)
        return move

    ##
    # Looking at the board, the learner adds missing moves to his internal history.
    # Must be called before every next_move and learn, if another player may have taken a new move.
    # @param game The game.
    # @return The move chosen by the player.
    def look(self, game):
            for row in range(game.board_size()):
                for column in range(game.board_size()):
                    player = game.board[row][column]
                    if (player):
                        try:
                            if (row, column) not in self.history[player]:
                                self.history[player].insert(0,(row, column))
                        except KeyError:
                            self.history[player] = [(row, column)]

    ##
    # Looking at the board, the learner adds missing moves to his internal history.
    # Should be called after every end-of-game.
    # @param game The game.
    # @param reward The reward that should associated with the current state of the game
    # (e.g. 100 if the learner is winning, -100 if the learner is loosing, 0 for a draw).
    # @param last_player The player who made the last move in the game.
    def learn(self, game, reward, last_player):
        self.look(game)
        if last_player != self:
            last_player_history = self.history[last_player.name]
            last_player_player_last_move = last_player_history.pop()
            self.history[last_player] = last_player_history
            game.board[last_player_player_last_move[0]][last_player_player_last_move[1]] = None
        for index, action in enumerate(self.history[self.name]):
            game.board[action[0]][action[1]] = None #remove my move from board to get the state prior to my move
            state = tuple(tuple(x) for x in game.board)
            prev_reward = self.get_reward(action, game.board)
            new_reward = prev_reward + self.learning_rate * (self.discount_factor * reward - prev_reward)
            self.set_reward(new_reward, action, state)
            for player in self.history.keys(): # remove my opponents move from board and history
                if player!=self.name:
                    try:
                        history_item = self.history[player][index]
                        game.board[history_item[0]][history_item[1]] = None
                    except IndexError:
                        pass
            reward = new_reward
        self.history = {}

    ##
    # Retrieves the reward for a particular action at the given state of the game.
    # @param action The specified action (move).
    # @param board The current state of the game.
    def get_reward(self, action, board):
        state = tuple(tuple(x) for x in board)
        try:
            return self.rewards[state][action]
        except KeyError:
            return 0
    ##
    # Saves the reward for a particular action at the given state of the game.
    # (For internal use).
    # @param action The specified action (move).
    # @param action The reward to be stored for the action.
    # @param board The current state of the game.
    def set_reward(self, reward, action, board):
        state = tuple(tuple(x) for x in board)
        try:
            reward_by_state = self.rewards[state]
        except KeyError:
            reward_by_state = {}
        reward_by_state[action] = reward
        self.rewards[state] = reward_by_state